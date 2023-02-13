# variables that will use
import os
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)


News_folder = "News"
os.makedirs(News_folder, exist_ok=True)


Proxy_file = os.path.join(data_folder,"Proxy.npy")


WORD_LANG_DICT = {
    'en'    :{'Welcome':'Welcome to today\'s news','open':Opening  , 'today_news':"Latest news" ,'Thanks':'Thank you for watching today'},
    'zh-tw' :{'Welcome':'歡迎收聽本日的新聞'        ,'open':'開場'   , 'today_news':"今日新聞"     ,'Thanks':'謝謝大家今天的收看'            }
    }





