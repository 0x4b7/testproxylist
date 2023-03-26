import socks
import socket

# Replace this with the location of your proxy list file
PROXY_LIST_FILE = 'proxy_list.txt'

# Replace this with the URL you want to test
TEST_URL = 'https://www.example.com/'

# Load the proxy list
with open(PROXY_LIST_FILE, 'r') as f:
    proxy_list = [line.strip() for line in f]

# Test each proxy
for proxy in proxy_list:
    # Split the proxy string into host and port
    host, port = proxy.split(':')

    # Create a SOCKS4 proxy connection
    socks.setdefaultproxy(socks.SOCKS4, host, int(port))
    socket.socket = socks.socksocket

    # Try to connect to the test URL
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(TEST_URL), 80))
        print(f'{proxy} is working')
    except Exception as e:
        print(f'{proxy} is not working: {e}')
