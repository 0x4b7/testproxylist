import requests

url = r'https://check-host.net/ip'
headers = {'user-agent': 'Mozilla/'
                         '5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/'
                         '20091102 Firefox/'
                         '3.5.5 (.NET CLR 3.5.30729)'}
with open("lt.txt", 'r', encoding='utf8') as f:
    proxy_list = [line.strip() for line in f]
for proxy in proxy_list:
    host, port = proxy.split(':')
    proxy_dic = {
        "http": f'socks4://{host}:{port}',
        "https": f'socks4://{host}:{port}'
    }

    print(proxy_dic)
    try:
        res = requests.get(url, headers=headers, proxies=proxy_dic)
        print(res.status_code, res.text)
    except Exception as e:
        print(f'{proxy} is not working: {e}')

    print("end")

#"http": f'socks4://{host}:{port}',
