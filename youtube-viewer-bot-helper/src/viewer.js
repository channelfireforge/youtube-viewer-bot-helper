const puppeteer = require('puppeteer');
const randomUseragent = require('random-useragent');

async function launchBrowser() {
    return await puppeteer.launch({ headless: 'new' });
}

async function simulateView(browser, videoUrl) {
    const page = await browser.newPage();
    const ua = randomUseragent.getRandom();
    await page.setUserAgent(ua);

    try {
        await page.goto(videoUrl, { waitUntil: 'networkidle2', timeout: 30000 });
        // Simulate watching part of the video
        await page.waitForSelector('video', { timeout: 10000 });
        await page.evaluate(() => {
            const video = document.querySelector('video');
            if (video) {
                video.currentTime = Math.random() * 30 + 10; // 10-40 seconds
            }
        });
        await new Promise(r => setTimeout(r, 5000)); // Watch for 5 seconds
    } catch (e) {
        console.warn('View simulation issue:', e.message);
    } finally {
        await page.close();
    }
}

module.exports = { launchBrowser, simulateView };