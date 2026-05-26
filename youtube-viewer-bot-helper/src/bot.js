const { launchBrowser, simulateView } = require('./viewer');
const config = require('./config');

async function runBot() {
    console.log('YouTube Viewer Bot Helper - Starting...');
    const browser = await launchBrowser();

    for (let i = 0; i < config.viewCount; i++) {
        console.log(`View ${i + 1} of ${config.viewCount}`);
        await simulateView(browser, config.videoUrl);
        await new Promise(r => setTimeout(r, config.delayBetweenViews));
    }

    await browser.close();
    console.log('Bot finished.');
}

runBot().catch(err => {
    console.error('Bot error:', err);
    process.exit(1);
});