# import aiohttp
# import asyncio
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, "http://httpbin.org/headers")
#         print(html)
# asyncio.run(main())
# tasks=asyncio.ensure_future()
import t

print(t.path())