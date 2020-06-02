from igramscraper.instagram import Instagram
import random_proxy

instagram = Instagram()

account = instagram.get_account('cars')


def insta_proxy_requests():
	while:
		try:
			proxy = random_proxy.get_proxy()
			r = instagram.set_proxies(proxy, timeout=5)
			break
		except:
			pass
	return r

