#!/usr/bin/env python3
"""
Zernio MCP & REST CLI helper for AI Content Manager.
Allows executing Zernio MCP tools and managing comment->DM automations.

Usage:
    python helper/zernio.py list
    python helper/zernio.py call accounts_list
    python helper/zernio.py call profiles_list
    python helper/zernio.py call posts_list '{"status":"published"}'
    python helper/zernio.py automations list
    python helper/zernio.py automations create --name "funnel test" --keyword TEST --dm "Link: https://..."
    python helper/zernio.py automations delete <id>
"""
import sys
import os
import json
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SERVER_URL = "https://mcp.zernio.com/mcp"
API_BASE = "https://zernio.com/api/v1"

def load_env():
    env_file = REPO_ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.split("#")[0].strip())

load_env()
ZERNIO_API_KEY = os.environ.get("ZERNIO_API_KEY", "")

def get_mcp_cmd():
    if not ZERNIO_API_KEY:
        sys.exit("Error: ZERNIO_API_KEY missing in .env")
    return [
        "cmd.exe",
        "/c",
        "npx",
        "-y",
        "mcp-remote",
        SERVER_URL,
        "--header",
        f"Authorization: Bearer {ZERNIO_API_KEY}"
    ]

def call_mcp_tool(tool_name: str, arguments: dict = None):
    arguments = arguments or {}
    req1 = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "zernio-cli-helper", "version": "1.0"}
        }
    }) + "\n"

    req2 = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }) + "\n"

    cmd = get_mcp_cmd()
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    try:
        proc.stdin.write(req1)
        proc.stdin.flush()
        proc.stdin.write(req2)
        proc.stdin.flush()

        for line in proc.stdout:
            line_str = line.strip()
            if not line_str:
                continue
            try:
                data = json.loads(line_str)
                if data.get("id") == 2:
                    if "error" in data:
                        print(json.dumps(data["error"], indent=2, ensure_ascii=False), file=sys.stderr)
                        return None
                    result = data.get("result", {})
                    content = result.get("content", [])
                    if content and content[0].get("type") == "text":
                        text = content[0].get("text", "")
                        try:
                            return json.loads(text)
                        except Exception:
                            return text
                    return result
            except json.JSONDecodeError:
                continue
    finally:
        proc.terminate()

def list_mcp_tools():
    req1 = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "zernio-cli-helper", "version": "1.0"}
        }
    }) + "\n"

    req2 = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }) + "\n"

    cmd = get_mcp_cmd()
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    try:
        proc.stdin.write(req1)
        proc.stdin.flush()
        proc.stdin.write(req2)
        proc.stdin.flush()

        for line in proc.stdout:
            line_str = line.strip()
            if not line_str:
                continue
            try:
                data = json.loads(line_str)
                if data.get("id") == 2:
                    return data.get("result", {}).get("tools", [])
            except json.JSONDecodeError:
                continue
    finally:
        proc.terminate()

# REST API helpers for Comment Automations
def api_request(method, path, body=None):
    if not ZERNIO_API_KEY:
        sys.exit("ZERNIO_API_KEY missing in .env")
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {ZERNIO_API_KEY}", "Content-Type": "application/json"},
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"Zernio API {e.code} on {method} {path}: {e.read().decode(errors='replace')}")

def resolve_ids():
    pid, aid = os.environ.get("ZERNIO_PROFILE_ID"), os.environ.get("ZERNIO_ACCOUNT_ID")
    if pid and aid:
        return pid, aid
    accounts = api_request("GET", "/accounts").get("accounts", [])
    ig = next((a for a in accounts if a.get("platform") == "instagram"), None)
    if not ig:
        sys.exit("No Instagram account connected on Zernio")
    prof = ig["profileId"]
    return (prof["_id"] if isinstance(prof, dict) else prof), ig["_id"]

def handle_automations(args):
    if not args:
        print("Usage: python helper/zernio.py automations [list|create|delete]")
        return
    action = args[0].lower()
    if action == "list":
        autos = api_request("GET", "/comment-automations")
        autos = autos.get("automations", autos) if isinstance(autos, dict) else autos
        if not autos:
            print("(no automations)")
            return
        for x in autos:
            stats = x.get("stats") or {}
            print(f"{x.get('_id') or x.get('id')}  [{'ON ' if x.get('isActive', True) else 'off'}]  "
                  f"kw={','.join(x.get('keywords', []) or ['<any>'])}  "
                  f"scope={x.get('platformPostId') or 'account'}  "
                  f"sent={stats.get('sent', '?')}  name={x.get('name', '')}")
    elif action == "create":
        import argparse
        p = argparse.ArgumentParser(description="Create comment automation")
        p.add_argument("--name", required=True)
        p.add_argument("--keyword", required=True)
        p.add_argument("--dm", required=True)
        p.add_argument("--reply", default="")
        p.add_argument("--post-id", default="")
        p.add_argument("--match", default="contains", choices=["contains", "exact"])
        parsed = p.parse_args(args[1:])
        
        profile_id, account_id = resolve_ids()
        body = {
            "profileId": profile_id,
            "accountId": account_id,
            "name": parsed.name,
            "keywords": [parsed.keyword],
            "matchMode": parsed.match,
            "dmMessage": parsed.dm,
        }
        if parsed.reply:
            body["commentReply"] = parsed.reply
        if parsed.post_id:
            body["platformPostId"] = parsed.post_id
        created = api_request("POST", "/comment-automations", body)
        auto = created.get("automation", created)
        auto_id = auto.get("_id") or auto.get("id")
        print(f"OK — automation '{parsed.name}' live: keyword {parsed.keyword} ({parsed.match})")
        print(auto_id)
    elif action == "delete":
        if len(args) < 2:
            sys.exit("Error: automation id required")
        auto_id = args[1]
        api_request("DELETE", f"/comment-automations/{auto_id}")
        print(f"OK — deleted {auto_id}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "list":
        tools = list_mcp_tools()
        print(json.dumps(tools, indent=2, ensure_ascii=False))
    elif cmd == "call":
        if len(sys.argv) < 3:
            print("Error: tool name required. e.g. python helper/zernio.py call accounts_list")
            sys.exit(1)
        t_name = sys.argv[2]
        args = {}
        if len(sys.argv) >= 4:
            args = json.loads(sys.argv[3])
        res = call_mcp_tool(t_name, args)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif cmd == "automations":
        handle_automations(sys.argv[2:])
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
