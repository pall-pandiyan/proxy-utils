"""
    Contains change_proxies() which changes current proxies.
    If run as a main module it will change once every 10 mins.
"""
import os

from proxy import Proxy
from time import sleep

p = Proxy()


def change_proxies():
    """
        change the current HTTP and HTTPS proxy to another random one.
    """
    os.environ["HTTP_PROXY"] = os.environ['http_proxy'] = p.random_proxy(protocol="http")
    os.environ["HTTPS_PROXY"] = os.environ['https_proxy'] = p.random_proxy(protocol="https")


if __name__ == '__main__':
    while True:
        change_proxies()
        # wait some time to change the proxies again!
        sleep(600)
