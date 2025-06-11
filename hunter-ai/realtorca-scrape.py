import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="file://assets/page1.html")
        print(result)

        # Using configuration:
        browser_config = BrowserConfig(browser_type="chromium", headless=True)
        async with AsyncWebCrawler(config=browser_config) as crawler:
            crawler_config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS
            )
            result = await crawler.arun(url="file://assets/page1.html", config=crawler_config)
            print(result.markdown)
            

if __name__ == "__main__":
    asyncio.run(main())