# Grab news
from datetime import datetime,timedelta
from bs4      import BeautifuSoup


from urllib.request import urlretrieve, Request, urlopen, quote
from utils.info     import News_folder

import requests as rq
import os
import json
import openai
import time


def remove_num_comma(word):
    need_remove = []
    output = ""
    for i in range(1,len(word)-1):
        if (word[i]=="," and word[i-1].isnumeric() and word[i+1].isnumeric()):
            need_remove.append(i)
            print(f"\tComma remove : {word[i-2:i+3]}")
        else:
            output += word[i]
    return output



def build_floder():

    today_date = datetime.now().strftime("%Y-%m-%d")
    save_floder = f"{News_folder}/{today_date}"

    yesterday_date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
    last_day_floder = f"{News_folder}/{yesterday_date}"
    
    os.makedirs(save_floder,exist_ok=True)

    return save_floder,last_day_floder


def spider():
    '''
    Your spider that grab news here
    '''

    save_floder, last_day_floder = build_floder()
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}


   all_news_floders = []   #  all news in this video

   return save_floder, all_news_floders




































