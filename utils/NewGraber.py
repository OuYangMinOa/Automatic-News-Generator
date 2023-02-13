# Grab news
from datetime import datetime,timedelta
from bs4      import BeautifuSoup


from urllib.request import urlretrieve, Request, urlopen, quote
from utils.Openai   import prompt_openai
from utils.info     import News_folder


import requests as rq
import openai
import json
import time
import os


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
    Grab your news here
    '''

    save_floder, last_day_floder = build_floder()




   for title_, this_new_Content in grab_result:
        # this_url : your carl website

        this_floder = os.path.join(save_floder,os.path.basename(this_url))  #  your carl website
        text_path   = os.path.join(this_floder,"word.txt")
        title_path  = os.path.join(this_floder,"title.txt")

        word = "Please summarize the text below and provide a brief verbal press release:\n" + this_new_Content
        print("\tword length :",len(word))
        this_new_Content = prompt_openai(word)

        print(this_new_Content,"\n\tLength :",len(this_new_Content))
        with open(text_path,'w',encoding="utf8") as f:
            f.write(this_new_Content)

        with open(title_path,'w',encoding="utf8") as f:
            f.write( title_)
        print("="*50)

        time.sleep(20)


   all_news_floders = []   #  all news folder in this arr

   return save_floder, all_news_floders




































