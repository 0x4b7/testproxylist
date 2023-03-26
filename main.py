
import aiohttp
import asyncio



async def test_proxy(proxy):
    async with aiohttp.ClientSession(connector=aiohttp.SocksConnector.from_url(proxy)) as session:
        try:
            async with session.get('https://httpbin.org/ip') as response:
                if response.status == 200:
                    print(f"{proxy} is working")
                else:
                    print(f"{proxy} is not working")
        except Exception as e:
            print(f"{proxy} is not working: {e}")

async def main():
    with open('lt.txt', 'r') as f:
        file = list(f.read().split())
        proxies = ['socks4://' + a[0] + ':' + a[1] for a in zip(file[::2], file[1::2])]
    tasks = [asyncio.create_task(test_proxy(proxy)) for proxy in proxies]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())