import random_proxy as proxy

test = proxy.proxy_requests('https://instagram.com')
print(test.content)
