# variables that will use
import os
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)


News_folder = "News"
os.makedirs(news_folder, exist_ok=True)


Proxy_file = os.path.join(data_folder,"Proxy.npy")