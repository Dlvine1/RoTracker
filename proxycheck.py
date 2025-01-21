import requests

proxies = open('txts/proxies.txt').read().splitlines()[0:1000]

url_to_test = 'https://www.rolimons.com/itemtable'

for proxy in proxies:
    try:
        response = requests.get(url_to_test, proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working.")
        else:
            print(f"Proxy {proxy} returned status code {response.status_code}.")
    except Exception as e:
        print(f"Error testing proxy {proxy}: {e}")
