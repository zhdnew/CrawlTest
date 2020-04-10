import asyncio
from pyppeteer import launch

async def main():
    broswer = await launch()
    page = await broswer.newPage()
    await page.goto('http://www.porters.vip/features/webdriver.html')
    await page.click('.btn.btn-primary.btn-lg')
    await asyncio.sleep(1)
    await page.screenshot({'path':'webdriver.png'})
    await broswer.close()

asyncio.get_event_loop().run_until_complete(main())
