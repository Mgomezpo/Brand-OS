// Simple carousel capture — screenshots each .slide element to PNG
// Usage: node capture.mjs <carousel.html> [outDir]

const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require('playwright');
const { pathToFileURL } = require('node:url');

const [, , htmlArg, outArg] = process.argv;
if (!htmlArg) {
  console.error('usage: node capture.mjs <carousel.html> [outDir]');
  process.exit(1);
}
const htmlPath = path.resolve(htmlArg);
if (!fs.existsSync(htmlPath)) {
  console.error(`not found: ${htmlPath}`);
  process.exit(1);
}
const outDir = path.resolve(outArg || path.join(path.dirname(htmlPath), 'slides'));
fs.mkdirSync(outDir, { recursive: true });

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({
      viewport: { width: 1080, height: 1440 },
      deviceScaleFactor: 2,
    });
    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);

    const slides = page.locator('.slide');
    const n = await slides.count();
    if (n === 0) {
      console.error('No `.slide` elements found.');
      process.exit(1);
    }
    for (let i = 0; i < n; i++) {
      const num = String(i + 1).padStart(2, '0');
      const box = await slides.nth(i).boundingBox();
      if (!box || Math.round(box.width) !== 1080 || Math.round(box.height) !== 1440) {
        console.warn(`⚠ slide ${num} is ${Math.round(box?.width)}×${Math.round(box?.height)}, expected 1080×1440`);
      }
      await slides.nth(i).screenshot({ path: path.join(outDir, `slide-${num}.png`) });
      console.log(`slide-${num}.png`);
    }
    console.log(`\n${n} slides → ${outDir}`);
  } finally {
    await browser.close();
  }
})();