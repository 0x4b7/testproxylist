import socks
import socket

with open("lt.txt", 'r', encoding='utf8') as f:
    proxy_list = [line.strip() for line in f]
for proxy in proxy_list:
    host, port = proxy.split(':')
    try:
        s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
        s.set_proxy(socks.SOCKS4, host ,int(port))
        s.settimeout(20)
        s.connect(("http://httpbin.org/ip", 80))
        print(s.recv(4096))
    except Exception as e:
        print(f'{proxy} is not working: {e}')


