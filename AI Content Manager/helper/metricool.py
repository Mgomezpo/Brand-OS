#!/usr/bin/env python3
"""
Metricool MCP CLI helper for AI Content Manager.
Allows executing Metricool MCP tools via stdio bridge with cached OAuth credentials.

Usage:
    python helper/metricool.py list
    python helper/metricool.py call getBrandSettings
    python helper/metricool.py call getBestTimeToPostByNetwork '{"network":"INSTAGRAM"}'
    python helper/metricool.py call getScheduledPosts '{"from":"2026-10-08T00:00:00","to":"2026-10-15T23:59:59"}'
"""
import sys
import json
import subprocess

SERVER_URL = "https://ai.metricool.com/mcp"

def call_mcp_tool(tool_name: str, arguments: dict = None):
    arguments = arguments or {}
    req1 = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "metricool-cli-helper", "version": "1.0"}
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

    cmd = ["cmd.exe", "/c", "npx", "-y", "mcp-remote", SERVER_URL]
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
                    # Parse inner text if JSON
                    content = result.get("content", [])
                    if content and content[0].get("type") == "text":
                        text = content[0].get("text", "")
                        try:
                            parsed = json.loads(text)
                            return parsed
                        except Exception:
                            return text
                    return result
            except json.JSONDecodeError:
                continue
    finally:
        proc.terminate()

def list_tools():
    req1 = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "metricool-cli-helper", "version": "1.0"}
        }
    }) + "\n"

    req2 = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }) + "\n"

    cmd = ["cmd.exe", "/c", "npx", "-y", "mcp-remote", SERVER_URL]
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
                    tools = data.get("result", {}).get("tools", [])
                    return tools
            except json.JSONDecodeError:
                continue
    finally:
        proc.terminate()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "list":
        tools = list_tools()
        print(json.dumps(tools, indent=2, ensure_ascii=False))
    elif cmd == "call":
        if len(sys.argv) < 3:
            print("Error: tool name required. e.g. python helper/metricool.py call getBrandSettings")
            sys.exit(1)
        t_name = sys.argv[2]
        args = {}
        if len(sys.argv) >= 4:
            args = json.loads(sys.argv[3])
        res = call_mcp_tool(t_name, args)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
