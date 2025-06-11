import requests, base64
from bs4 import BeautifulSoup
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

baseurl = "https://www.realtor.ca/on/ottawa/real-estate?gad_source=1&gad_campaignid=16914664984&gclid=Cj0KCQjw0qTCBhCmARIsAAj8C4anW75k4Zg86i1fYHFE-9PwSeHKsiLddBnXeCSoABCscQC3CeqXoDgaAvRhEALw_wcB"

headers = {
    "Host": "www.realtor.ca",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.google.com/",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Connection": "keep-alive",
    "Cookie": "Language=1; app_mode=1; Currency=CAD; GUID=00373170-3770-4249-b262-33b5c6c02e8e; visid_incap_2269415=8fEclLyqQMSHDpfaunirZ/TYPGgAAAAAQUIPAAAAAAD0EW07zx6kYoAgWnPmkfrG; visid_incap_3157676=872HhjH6TdmJDZ1mceUD3vXYPGgAAAAAQUIPAAAAAABNu+aCCTlky8B2RGjraEYo; ViewedListings=12; ai_user=0iAJy|2025-06-01T22:49:25.750Z; _gcl_au=1.1.1894864594.1748818166; reese84=3:YM23MNVgQ858s65mkjF9mw==:hnMk30vhzhfsAXlBypAk3a7nJhdeQAxSXPGV32d5DUIv6BaF5R309zWDpD+FQZhzUdhPEPkc5NyG512slytSMyBKrcCe7IbfHVVh/7fA3dtx7/XVbOKfIoT51ae3W5MBc0p69TylVqMjDRr9UENEwzbgY8F9/S4aPQ+Nm4TbYP63IAVZTj6XglhuRG5zGNAl912oP/jQN8EVdb3RGI5JUmHvMMdprjJnwvqQodp0vvkh4HuijD2M5QBeDM4maY16cjh84V5M7DFYkB/bTxazh1dx1iRzcoCv8nw39bfPMw+Zstyqe53paAGA6/4PVBcdT2kkxvQlIOOXWy1KzBihu+js2OQzQYVw71Po9hh5p3P1v2+Tsl3JfmgdAW7HlnnSjbEWoQXN6xRDTo0a4B+OboZjV/Iqzgncfx3AFO2JlhGX61Sc3Wpqx9ZsYlAY1qyyhkCiFkb0cxAdFC8rFsxobg==:FUJSgpTFAjqKV5HBB4juLy6GHhmdWCCdutsoKWvl1e8=; _ga_Y07J3B53QP=GS2.1.s1749672603$o7$g1$t1749674670$j60$l0$h0; _ga=GA1.2.1048082986.1748818167; _scor_uid=0e18e0d190ac460992f9973f761b351c; visid_incap_3057435=YyVdk88rSjOA+AXEJoDLMPbYPGgAAAAAQUIPAAAAAAA1gWI5Gn3WVWgP9SekeY18; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; PreferredMeasurementUnits=2; adsettings=listmobile=0&listdesktop=1&mapmobile=0&mapdesktop=1; cmsdraft=False; _gid=GA1.2.531981375.1749619195; ResidentialorCommercial=residential; visid_incap_2271082=0xKFqftHQdO2wAYu/cNx/psSSWgAAAAAQUIPAAAAAAC5+7NVw+V71Tp61gDqunXl; ll-visitor-id=c416a4c4-9221-451e-b39a-a7feebf97d5f; QSI_SI_7W245MdctqNQU0m_intercept=true; TermsOfUseAgreement=2018-06-07; __AntiXsrfToken=b546cde9fd8546a6a8c6e114c298f5f5; nlbi_2269415=/g+fK75QqDw8K1ZkCcuCgwAAAAAep9WZ49hTdud7xRK3/xX+; nlbi_2269415_2147483392=P3bmZJP2Ph7ij7GxCcuCgwAAAAAXyhWvUnPKYxTvgm10z5dW; nlbi_3057435=wos3JYmp/CsDt5zeoWGLxgAAAAC2KbeAUrQ5Sf6ZJA+7Fa3f; incap_ses_1699_2269415=G8HZG1iLsUcsZ+O13A+UF5riSWgAAAAAeEu1zUUcFkkhO9oRKt4Dew==; incap_ses_1699_3157676=lKqmOl5D61Q+1Oi13A+UF6zqSWgAAAAA8/fGJzihJ534GSj99urGHw==; nlbi_2271082=aFOSJfWrJG8VW4aRVPrQ3QAAAAAPXO43QQ1oGDbBfaWDONe7; incap_ses_1699_2271082=YzRCYDG/xD2UZ+O13A+UF5viSWgAAAAAqXSRXBfDjH3kI/MXvt5IOA==; mapZoomLevel=ZoomLevel=10; ai_session=s64vG|1749672604133|1749674669975; _gcl_aw=GCL.1749674670.Cj0KCQjw0qTCBhCmARIsAAj8C4anW75k4Zg86i1fYHFE-9PwSeHKsiLddBnXeCSoABCscQC3CeqXoDgaAvRhEALw_wcB; _gcl_gs=2.1.k1$i1749674668$u5869104; _gac_UA-12908513-11=1.1749674671.Cj0KCQjw0qTCBhCmARIsAAj8C4anW75k4Zg86i1fYHFE-9PwSeHKsiLddBnXeCSoABCscQC3CeqXoDgaAvRhEALw_wcB; _dc_gtm_UA-12908513-11=1; _gali=listViewSEOLandingPageTitle",
    "Priority": "u=0, i",
    "TE": "trailers"
}

result = requests.get(url=baseurl, headers=headers)
soup = BeautifulSoup(result.text, 'html.parser')
# print(soup)

async def main():

    file_url = f"raw:{soup}"
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=file_url, config=config)
        if result.success:
            print("Markdown Content from Local File:")
            print(result.markdown)
        else:
            print(f"Failed to crawl local file: {result.error_message}")



if __name__ == "__main__":
    asyncio.run(main())




# allProducts = soup.findAll(class_="u30d4")
# number = 0
# for product in allProducts:
#     name = product.find(class_="rgHvZc")
#     if name is not None:
#         number += 1
#         print("Product number %d:" % number)
#         print("Name : " + name.text)
#         productLink = product.find('a')
#         print("Link: " + productLink["href"][7:])
#         img = product.find('img')
#         print("Image: " + img["src"])
#         price = product.find(class_="HRLxBb")
#         print("Price " + price.text)

