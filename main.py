import aiohttp
import asyncio
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector


async def test_proxy(proxy):
    async with aiohttp.ClientSession(connector= ProxyConnector.from_url(proxy )) as session:
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
        file = f.read()
        proxies = ['socks4://' + p.split(':')[0] + ':' + p.split(':')[1] for p in file.split()]

    tasks = [asyncio.create_task(test_proxy(proxy)) for proxy in proxies]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
