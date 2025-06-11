import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from bs4 import MarkupResemblesLocatorWarning, BeautifulSoup
import warnings
    
async def main():
    
    filehandle = open("C:/Users/raymo/Github/ai-tools/hunter-ai/assets/page1.html")
    
    soup = BeautifulSoup(filehandle)
    # print(soup)

    local_file_path = "C:/Users/raymo/Github/ai-tools/hunter-ai/assets/page2.htm"  # Replace with your file path
    # file_url = f"file://{local_file_path}"
    file_url = f"raw:{soup}"
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=file_url, config=config)
        if result.success:
            print("Markdown Content from Local File:")
            print(result.markdown)
        else:
            print(f"Failed to crawl local file: {result.error_message}")

        # # Using configuration:
        browser_config = BrowserConfig(browser_type="chromium", headless=False)
        async with AsyncWebCrawler(config=browser_config) as crawler:
            crawler_config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS
            )
            result = await crawler.arun(url=file_url, config=crawler_config)
            print(result.markdown)
            

if __name__ == "__main__":
    asyncio.run(main())