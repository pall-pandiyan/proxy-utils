"""
    contains a class named Proxy which contains methods to manipulate proxies.
"""
import os
import requests

from random import randint
from time import sleep

current_dir = os.path.dirname(__file__)

class Proxy:
    """
        Proxy class contains functions like get a random proxy for a specific protocol (http or https), and update the proxy file.
        constructor arguments:
            proxy_file_name - defalut is 'proxy_list.txt'
            proxy_update_file_name - default is 'proxy_update_list.txt'
        
        functions:
            update_proxy_list()
                updates the proxy_list file with working proxies.
                returns none
            
            random_proxy(protocol:str)
                protocol - a str containing http or https.
                returns a random proxy of given protocols.
            
            random_proxy_dict(protocols:tuple)
                protocols - a tuple containing http or https or both.
                returns a dict with proxy or proxies of given protocols.
    """
    proxy_list = [
        "23.170.248.146:3129",
        "195.110.59.82:80",
        "161.35.223.141:80",
        "128.199.202.122:3128",
        "45.79.158.235:44554",
        "47.254.153.78:8888",
        "47.244.2.19:3128",
        "146.59.199.12:80",
        "143.198.182.218:80",
        "51.38.28.127:80",
        "110.34.3.229:3128",
        "1.224.3.122:3888",
        "163.116.248.47:808",
        "75.89.101.63:80",
        "149.28.132.9:10000",
        "90.255.243.214:8888",
        "115.144.101.200:10000",
        "154.239.1.77:1981",
        "188.166.56.246:80",
        "157.230.255.230:8118",
        "137.184.154.110:443",
        "82.66.75.98:49400",
        "187.217.54.84:80",
        "51.77.119.143:8888",
        "116.202.22.13:3128",
        "5.9.224.202:8080",
        "159.138.139.32:8080",
        "179.1.95.171:999",
        "34.84.56.140:3128",
        "110.238.74.184:8080",
        "159.138.169.166:2080",
        "110.78.208.91:8000",
        "34.146.64.228:3128",
        "132.147.34.22:8111",
        "41.93.71.15:80",
        "45.118.139.196:80",
        "109.68.145.110:3128",
        "109.68.145.120:3128",
        "163.220.240.50:3128",
        "146.158.19.130:8080",
        "167.172.173.210:39253",
        "202.72.220.83:80",
        "8.219.5.240:8080",
        "143.198.56.234:443",
        "217.30.163.172:3128",
        "204.14.15.124:8080",
        "13.127.72.50:80",
        "34.66.5.144:8888",
        "87.251.81.74:8088",
        "117.54.114.32:80",
        "185.114.132.103:80",
        "80.232.242.125:9002",
        "124.13.181.7:80",
        "102.130.192.231:8080",
        "46.174.37.21:8118",
        "147.139.176.149:3128",
        "129.213.95.20:80",
        "61.220.170.133:8000",
        "35.221.104.58:3128",
        "89.107.197.164:3128",
        "204.14.15.125:8080",
        "45.172.111.90:999",
        "138.121.161.82:8097",
        "213.149.182.98:8080",
        "41.33.86.242:8080",
        "61.9.32.54:54321",
        "103.152.232.194:8080",
        "117.54.114.101:80",
        "103.148.192.83:8082",
        "114.143.242.234:80",
        "178.33.198.181:3128",
        "119.28.22.45:8089",
        "182.16.12.27:8088",
        "182.16.12.28:8088",
        "163.116.177.32:808",
        "163.116.177.31:808",
        "78.47.68.183:80",
        "103.144.161.100:8088",
        "149.129.247.230:3128",
        "147.139.163.141:3128",
        "79.172.217.106:80",
        "18.167.243.168:80",
        "137.74.65.101:80",
        "163.172.85.30:80",
        "167.114.50.144:808",
        "47.242.174.100:8000",
        "195.8.249.242:80",
        "51.75.141.46:80",
        "117.54.114.35:80",
        "103.155.197.36:8080",
        "115.241.197.126:80",
        "41.191.236.5:80",
        "143.198.33.27:81",
        "20.220.225.197:80",
        "208.87.129.44:80",
        "217.6.28.219:80",
        "90.45.141.107:80",
        "182.16.12.26:8088",
        "182.16.12.29:8088",
        "123.3.84.55:80",
        "65.108.74.94:8080",
        "80.15.76.28:80",
        "52.30.164.26:80",
        "65.108.9.181:81",
        "112.120.127.146:80",
        "112.120.41.71:80",
        "41.206.35.126:8080",
        "5.161.90.204:3128",
        "45.156.31.38:9090",
        "82.137.244.74:8080",
        "75.89.101.60:80",
        "80.48.119.28:8080",
        "8.210.83.33:80",
        "198.59.191.234:8080",
        "200.105.215.22:33630",
        "179.96.28.58:80",
        "198.49.68.80:80",
        "45.79.110.81:80",
        "147.139.193.92:3128",
        "47.243.180.142:808",
        "147.139.192.225:3128",
        "162.211.181.130:808",
        "34.100.231.110:80",
        "147.139.192.126:3128",
        "110.164.15.182:8080",
        "185.51.10.19:80",
        "103.167.135.111:80",
        "210.6.223.207:80",
        "112.217.162.5:3128",
        "212.182.90.118:80",
        "103.167.135.113:80",
        "103.167.135.117:80",
        "206.222.8.58:80",
        "165.154.243.247:80",
        "103.167.135.112:80",
        "38.91.120.190:80",
        "103.152.113.18:80",
        "154.26.134.214:80",
        "154.26.134.217:80",
        "42.98.75.138:80",
        "139.59.255.37:443",
        "124.13.181.6:80",
        "114.37.214.158:80",
        "103.197.71.7:80",
        "89.43.10.141:80",
        "54.36.239.180:5000",
        "157.254.193.139:80",
        "182.16.12.30:8088",
        "163.116.177.33:808",
        "163.116.177.48:808",
        "82.98.147.36:80",
        "13.127.4.162:3128",
        "45.250.163.18:8081",
        "96.68.234.217:8080",
        "174.70.1.210:8080",
        "41.77.188.131:80",
        "46.47.197.210:3128",
        "170.155.4.11:82",
        "167.172.41.151:80",
        "175.45.195.18:80",
        "18.190.155.129:80",
        "170.187.138.40:8009",
        "54.213.41.155:80",
        "190.5.77.211:80",
        "54.213.103.7:80",
        "129.153.163.10:80",
        "104.148.36.10:80",
        "103.86.50.169:8000",
        "80.252.5.34:7001",
        "117.121.202.62:8888",
        "144.217.7.157:9300",
        "45.8.179.241:1337",
        "185.39.50.2:1337",
        "47.241.165.133:443",
        "103.178.43.2:8181",
        "158.101.98.70:3128",
        "149.129.248.224:3128",
        "138.2.8.164:8000",
        "213.233.182.38:8000",
        "46.101.13.77:80",
        "93.84.64.137:3128",
        "118.26.110.48:8080",
        "142.93.61.46:80",
        "211.56.7.42:80",
        "13.71.80.224:80",
        "3.142.90.54:80",
        "35.202.186.72:80",
        "31.14.131.201:81",
        "54.69.130.23:80",
        "45.8.179.242:1337",
        "112.133.231.132:8000",
        "195.201.231.22:8080",
        "163.116.177.49:808",
        "163.116.177.44:808",
        "185.37.24.242:80",
        "105.112.95.133:8080",
        "109.86.182.203:3128",
        "116.101.103.63:4013",
        "36.94.47.58:4480",
        "103.105.76.65:8080",
        "175.100.35.238:8080",
        "36.67.114.242:41890",
        "185.74.20.27:9090",
        "196.44.224.46:8080",
        "36.89.158.91:4480",
        "176.192.70.58:8008",
        "217.67.190.154:3128",
        "49.0.2.242:8090",
        "169.57.1.85:8123",
        "63.250.52.82:8118",
        "65.21.161.114:42069",
        "103.118.40.119:80",
        "43.255.113.232:8082",
        "91.229.114.63:80",
        "194.87.188.114:8000",
        "20.205.42.31:80",
        "47.91.125.239:8080",
        "149.129.179.23:8080",
        "103.152.113.32:80",
        "121.1.41.162:111",
        "34.84.172.172:3128",
        "139.99.237.62:80",
        "5.102.71.22:8080",
        "128.22.123.175:80",
        "58.152.47.105:80",
        "170.187.182.17:45554",
        "146.190.123.209:80",
        "8.209.198.247:80",
        "15.206.163.248:8088",
        "205.185.126.246:3128",
        "35.221.104.199:3128",
        "20.110.99.169:80",
        "34.67.79.204:80",
        "20.111.54.16:80",
        "41.93.71.21:80",
        "103.234.55.173:80",
        "20.206.106.192:80",
        "118.27.113.167:8080",
        "140.83.32.175:80",
        "20.210.26.214:3128",
        "46.31.77.223:3128",
        "203.198.207.253:80",
        "115.68.221.147:80",
        "152.32.202.108:80",
        "126.125.40.75:8080",
        "20.210.113.32:8123",
        "20.24.43.214:8123",
        "104.223.135.178:10000",
        "207.154.230.195:8888",
        "103.167.135.110:80",
        "154.236.189.28:8080",
        "188.136.196.34:8080",
        "177.87.168.6:53281",
        "103.227.252.102:8080",
        "156.200.116.69:1981",
        "98.164.130.195:8080",
        "139.59.241.101:443",
        "201.229.250.19:8080",
        "82.99.194.30:3128",
        "45.32.69.105:3128",
        "45.121.216.219:55443",
        "43.153.34.157:3128",
        "13.212.78.140:80",
        "163.116.177.46:808",
        "92.118.232.74:80",
        "148.72.23.104:8008",
        "83.229.73.175:80",
        "41.175.26.115:80",
        "182.72.203.243:80",
        "83.229.72.174:80",
        "13.95.173.197:80",
        "216.137.184.253:80",
        "134.238.252.143:8080",
        "163.116.158.142:8081",
        "163.116.177.34:808",
        "163.116.177.30:808",
        "163.116.158.28:8081",
        "80.169.156.52:80",
        "163.116.177.51:808",
        "163.116.158.182:8081",
        "163.116.158.25:8081",
        "163.116.177.47:808",
        "45.250.163.17:8081",
        "45.250.163.19:8081",
        "163.116.177.43:808",
        "163.116.177.45:808",
        "54.184.220.95:80",
        "163.116.158.183:8081",
        "62.225.13.118:80",
        "203.150.102.189:80",
        "195.8.249.243:80",
        "54.36.122.17:8088",
        "134.158.75.49:80",
        "176.168.127.74:80",
        "117.54.114.100:80",
        "141.136.42.164:80",
        "162.0.226.218:80",
        "47.91.44.217:8000",
        "34.135.166.24:80",
        "5.189.184.6:80",
    ]


    def __init__(self, proxy_file_name='proxy_list.txt', proxy_update_file_name='proxy_update_list.txt'):
        self.proxy_file_paths = {}
        self.proxy_update_file_paths = {}
        self.protocols = ("http", "https")
        for protocol in self.protocols:
            self.proxy_file_paths[protocol] = os.path.join(current_dir, protocol + "_" + proxy_file_name)
            self.proxy_update_file_paths[protocol] = os.path.join(current_dir, protocol + "_" + proxy_update_file_name)


    def __generate_proxy_update_file(self, protocol:str="https") -> None:
        """
            gets a protocol as string (http or https) and generate proxy_update_file for the specified protocol. default protocol is https.
        """
        with open(self.proxy_update_file_paths[protocol], 'a') as proxy_update_file:
            for proxy in self.proxy_list:
                req_proxy = {
                    protocol: protocol + "://" + proxy
                }
                try:
                    res = requests.get(protocol + "://www.google.com", proxies=req_proxy, timeout=5)
                except Exception as e:
                    print("Not connected using proxy:",  protocol + "://" + proxy)
                    continue
                if res.status_code == 200:
                    print("added:",  protocol + "://" + proxy)
                    proxy_update_file.write(proxy)
                    proxy_update_file.write("\n")
                    continue
                print("Not added:",  protocol + "://" + proxy)


    def update_proxy_list(self):
        """
            update the proxy_list file with the working proxies.
        """
        print("Proxy update is in progress...")
        for protocol in self.protocols:
            if os.path.exists(self.proxy_update_file_paths[protocol]):
                print("Existing update file for '" + protocol + "' is available!")
                choice:str = input("Do you want to use it? (y/n): ").lower()
                if choice == 'y':
                    os.replace(self.proxy_update_file_paths[protocol], self.proxy_file_paths[protocol])
                    return
                os.remove(self.proxy_update_file_paths[protocol])
            self.__generate_proxy_update_file(protocol)
            os.replace(self.proxy_update_file_paths[protocol], self.proxy_file_paths[protocol])
        self.change_system_proxies()


    def random_proxy(self, protocol:str="https") -> str:
        """
            select a random proxy from proxy_list from specified protocol and returns it.
        """
        # print("proxy file path:", self.proxy_file_paths[protocol])
        if not os.path.exists(self.proxy_file_paths[protocol]):
            print("proxy file is not found!")
            return ""
    
        with open(self.proxy_file_paths[protocol]) as proxy_file:
            working_proxy_list = proxy_file.read().split('\n')
            random_proxy_index = randint(0, len(working_proxy_list)-2)
            return self.proxy_list[random_proxy_index]


    def random_proxy_dict(self, protocols:tuple=None) -> dict:
        """
            select a random proxy from proxy_list from specified protocols and returns it.
        """
        if not protocols:
            protocols = self.protocols
        proxy = {}
        for protocol in protocols:
            # print("proxy file path:", self.proxy_file_paths[protocol])
            if not (random_proxy := self.random_proxy(protocol=protocol)):
                continue
            proxy[protocol] = protocol + "://" + random_proxy
        return proxy


    def change_system_proxies(self) -> None:
        """
            change the current HTTP and HTTPS proxy to another random one.
        """
        os.environ["HTTP_PROXY"] = os.environ['http_proxy'] = self.random_proxy(protocol="http")
        os.environ["HTTPS_PROXY"] = os.environ['https_proxy'] = self.random_proxy(protocol="https")


if __name__ == "__main__":
    Proxy().update_proxy_list()
