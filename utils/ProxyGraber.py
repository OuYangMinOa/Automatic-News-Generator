# ProxyGraber
from multiprocessing import Pool
from tqdm.auto       import tqdm
from threading       import Thread

from utils.MyLog     import logger
from utils.info      import Proxy_file

import numpy as np
import requests
import json
import time
import bs4
import re
import os


class proxies:
    def __init__(self,url='https://www.microsoft.com/',p=6,num=-1):
        self.unverify_proxy = []
        self.proxy_list     = []

        self.url = url
        self.p   = p
        self.num = num

        self.geo_start_page = 0

        self.sslproxies()
        # self.geonode()

    def test_connect(self,proxy):

        try:
            result = requests.get(self.url,proxies={'http': proxy, 'https': proxy},timeout=5)
            self.proxy_list.append(proxy)
        except Exception as e:
            # Can't connect ( no need add in log)
            pass
        finally:
            self.pro.update(1)
            self.finish += 1

    def verify_proxy(self):
        '''
        using a thread to test all availble proxy
        '''
        self.finish = 0
        self.pro = tqdm(total=len(self.unverify_proxy))  

        for each_proxy in self.unverify_proxy:
            Thread(target=self.test_connect, args=(each_proxy,),daemon=True).start()

        while self.finish<len(self.unverify_proxy):
            time.sleep(1)
        self.pro.close()
        self.unverify_proxy = []

    def save_proxy(self,path=Proxy_file):
        if (os.path.isfile(path)):
            proxies_arr =  np.load(path)
            new_arr     = np.append(proxies_arr, self.proxy_list)
            new_arr     = np.unique(new_arr)
            np.save(path, new_arr)

            self.proxy_list = new_arr
        else:
            np.save(path, np.array(self.proxy_list))
    def delete_proxy_file(self, path=Proxy_file):
        if (os.path.isfile(path)):
            os.remove(Proxy_file)

    def get_proxies(self):
        host, port = [], []
        for each_proxy in self.proxy_list:
            this_  = each_proxy.split(":")
            host.append(this_[0])
            port.append(int(this_[1]))
        return host, port

    def sslproxies(self):
        response = requests.get("https://www.sslproxies.org/")
        self.unverify_proxy.extend(re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text))
        self.unverify_proxy = self.unverify_proxy[:self.num]


    def geonode(self):
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        for self.geonode_page in range(self.geo_start_page + 1,self.geo_start_page + 4):
            url = f'https://proxylist.geonode.com/api/proxy-list?limit=500&page={self.geonode_page}&sort_by=lastChecked&sort_type=desc'
            response = requests.get(url,headers=headers).json()
            for each_ip in response['data']:
                this_proxy = f"{each_ip['ip']}:{each_ip['port']}"
                # print(this_proxy)
                self.unverify_proxy.append(this_proxy)
            self.geo_start_page = self.geonode_page





if (__name__ == '__main__'):
    p = proxies()
    p.verify_proxy()
    p.save_proxy()