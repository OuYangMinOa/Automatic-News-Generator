# uploadtoyt
from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api.Channel    import Channel

from utils.MyLog        import logger
from utils.openai       import prompt_openai

import dotenv
import os

dotenv.load_dotenv()

channel = Channel()
channel.login("client_scret.json", "credentials.storage")


def upload_yt(today_date, lang):
    try:
        today_floder    = os.path.join("News",today_date)
        video_path      = os.path.join(today_floder,f"Final_{lang}.mp4")
        time_stamp_path = os.path.join(today_floder,f"Final_{lang}.txt")

        with open(time_stamp_path,"r",encoding="utf8") as f:
            discription  =  f.read()

        title = f"【News】{today_date} " + discription.split("\n")[4].split('\t')[1]

        this_title_content_ = discription.split('\n')[4].split('\t')[1]

        ## youtube title limits 100 words
        if (len(title)>100):
            title = f"【News】{today_date} " + prompt_openai(f"Q:Please reduce the following words :{this_title_content_}\nA:")

        print("\t",title)
        video = LocalVideo(file_path=video_path)
        video.set_title(title)
        video.set_description(discription)
        video.set_category('news')
        video.set_privacy_status("public") # private
        video.set_embeddable(True)
        video.self_declared_made_for_kids = False    
        video = channel.upload_video(video)        
        channel.add_video_to_playlist(os.getenv("PLAYLIST"),video)    
        print("\tVideo Id:",video.id)
        print(f"[*] {today_date} Everything complete.\n")
    except Exception as e:
        logge.error(e)