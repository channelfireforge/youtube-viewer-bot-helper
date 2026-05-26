const { launchBrowser, simulateView } = require('../src/viewer');
const config = require('../src/config');

async function testSimulateView() {
    console.log('Running test: simulate a single view...');
    const browser = await launchBrowser();
    try {
        await simulateView(browser, config.videoUrl);
        console.log('Test passed: view simulation completed without crash.');
    } catch (err) {
        console.error('Test failed:', err.message);
    } finally {
        await browser.close();
    }
}

testSimulateView();