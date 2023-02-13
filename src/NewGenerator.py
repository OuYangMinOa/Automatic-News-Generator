## make new
from utils.NewGraber    import GrabEnglishNews, GrabChineseNews
from utils.openai       import prompt_openai
from utils.AudioMaker   import build_audio3
from utils.ProxyGraber  import proxies
from utils.VideoMaker   import build_video, combined_all_video, get_video_time
from utils.MyLog        import logger
from utils.UploadYt     import upload_yt

from utils.info      import Proxy_file, WORD_LANG_DICT


import numpy as np


def change_line(words, each_line_num = 50,lang="en"):
    change_time = len(words)//each_line_num + 1
    if (change_time>1):

        start_index,temp_index = 0,1
        temp_words = ""


        if (lang=="en"):
            total_word_split = words.split(" ")
            for i in range(change_time-1):
                while len(" ".join(total_word_split[start_index:temp_index]))<each_line_num and temp_index<len(total_word_split):
                    temp_index += 1
                temp_words  = temp_words + " ".join(total_word_split[start_index:temp_index]) + "\n"
                start_index = temp_index
                temp_index += 1
            temp_words = temp_words + " ".join(total_word_split[start_index:])
            return temp_words
        else:
            total_word_split = words
            for i in range(change_time-1):
                while len(total_word_split[start_index:temp_index])<each_line_num and temp_index<len(total_word_split):
                    temp_index += 1
                temp_words  = temp_words + total_word_split[start_index:temp_index] + "\n"
                start_index = temp_index
                temp_index += 1
            temp_words = temp_words + total_word_split[start_index:]
            return temp_words
    return words

def build_w_words(words, audio_path, video_path, is_titled=False,color='white',lang = "zh-tw",image_floder=None):
    if ("&" in words):words = words.replace("&","")
    def get_audio_con():

        ################### try local ip
        try:  
            build_audio3(words,audio_path,lang=lang)
            return
        except:
            pass

        ################### try proxy ip

        p = proxies()
        p.verify_proxy()
        p.save_proxy(Proxy_file)
        hosts , ports = p.get_proxies()
        for this_host, this_port in zip(p.get_proxies()):
            try:
                print(f"[*] Tring to use proxy server {this_host}:{this_port} ...",end="  ")
                build_audio3(words,audio_path,lang=lang, host=this_host,port=this_port )
                print("Successful !")
                return
            except Exception as e:
                logger.error(e)
        logger.info("ALl proxies failed, get more proxies ...")

        ################### try more proxy ip

        while True:
            p.delete_proxy_file(Proxy_file)
            p.proxy_list = []
            p.sslproxies()
            p.geonode()
            p.verify_proxy()
            p.save_proxy(Proxy_file)

            for this_host, this_port in zip(p.get_proxies()):
                try:
                    print(f"[*] Tring to use proxy server {this_host}:{this_port} ...",end="  ")
                    build_audio3(words,audio_path,lang=lang, host=this_host,port=this_port )
                    print("Successful !")
                    return
                except:
                    pass
    if (not os.path.isfile(audio_path)):
        get_audio_con()


    words = change_line(words.strip())


    fontsize = 50
    if ("0.mp3" == os.path.basename(audio_path)):
        words = change_line(words,20, lang=lang)
        fontsize=75
        image_floder = None

    if (is_titled):
        fontsize=75
        image_floder = None

    return build_video(words,audio_path,video_path,
                width      = 1920 ,
                height     = 1080 ,
                fps        = 24   ,
                color      = color,
                fontsize   = fontsize,
                image_path = image_floder)


def MakerNew(src_func, lang)
    logger.info("[*] Grabing news ...")
    today_floder, Get_News_Floder = src_func()

    logger.info(f"\n\n[*] Grab result :\n\ttoday_floder, Get_News_Floder = '{today_floder}', ", Get_News_Floder)


    today_date = datetime.now().strftime("%Y-%m-%d")

    logger.info("[*] Checking the section video ...")

    SECTION_VIDEO     = 'section'
    SECTION_VIDEOLANG = os.path.join(SECTION_VIDEO,lang)

    this_audio_floder = os.path.join(SECTION_VIDEOLANG,"audio")
    this_video_floder = os.path.join(SECTION_VIDEOLANG,"video")
    video_time_path   = os.path.join(SECTION_VIDEOLANG,"video_time.npy")
    


    ####  Fixed clips can be made only once and save the length of the movie 

    if (not os.path.isfile(video_time_path)):
        video_time_arr = [0,0]
    else:
        video_time_arr = load(video_time_path)

    if (not os.path.isdir(SECTION_VIDEO    )):os.mkdir(SECTION_VIDEO)
    if (not os.path.isdir(this_audio_floder)):os.mkdir(this_audio_floder)
    if (not os.path.isdir(this_video_floder)):os.mkdir(this_video_floder)

    start_audio  = os.path.join(this_audio_floder,"start.mp3" )
    start_video  = os.path.join(this_video_floder,"start.mp4" )


    ending_audio = os.path.join(this_audio_floder,"ending.mp3")
    ending_video = os.path.join(this_video_floder,"ending.mp4")


    ALL_time   = []
    ALL_time_stamp = [WORD_LANG_DICT[lang]['open']]


    if (not os.path.isfile(start_video  ) or video_time_arr[0] == 0): video_time_arr[0] = build_w_words(WORD_LANG_DICT[lang]['Welcome'],start_audio ,start_video ,True)
    if (not os.path.isfile(ending_video ) or video_time_arr[1] == 0): video_time_arr[1] = build_w_words(WORD_LANG_DICT[lang]['Welcome'],ending_audio,ending_video,True)
    
    np.save(video_time_path,video_time_arr)


    ALL_videos = [start_audio,        ]    
    ALL_time   = [video_time_arr[0],   ]

    logger.info("[*] Generating news video ...")
    ALL_videos.append(in_time_news_video)
    ALL_time.append(video_time_arr[2])
    ALL_time_stamp.append(WORD_LANG_DICT[lang]['today_news'])



    for j,each_news_floder in enumerate(Get_News_Floder):
        print(f"{j+1} / {len(Get_News_Floder)} : {each_news_floder}")
        this_text_path  = os.path.join(each_news_floder,"word.txt")
        this_text       = open(this_text_path,"r",encoding="utf8").read()

        this_title_path  = os.path.join(each_news_floder,"title.txt")
        this_title       = open(this_title_path,"r",encoding="utf8").read()

        this_audio_floder = os.path.join(each_news_floder,"audio")
        this_video_floder = os.path.join(each_news_floder,"video")
        this_image_floder = os.path.join(each_news_floder,"images")


        if (not os.path.isdir(this_audio_floder)):os.mkdir(this_audio_floder)
        if (not os.path.isdir(this_video_floder)):os.mkdir(this_video_floder)

        text_splited =  [this_title,]
        text_splited.extend(sent_tokenize(this_text))
        pro = tqdm(total=len(text_splited))

        num = 0
        this_sentence = ""
        total_time = 0
        for i in range(len(text_splited)):
            this_sentence += text_splited[i].strip()

            this_audio_save_path = os.path.join(this_audio_floder,f"{num}.mp3")
            this_video_save_path = os.path.join(this_video_floder,f"{num}.mp4")
            # print(num,this_sentence)
            
            if (not os.path.isfile(this_video_save_path)):
                total_time += build_w_words(this_sentence,this_audio_save_path,this_video_save_path,image_floder=this_image_floder)
            else:
                total_time += get_video_time(this_video_save_path)

            ALL_videos.append(this_video_save_path)
            num += 1
            this_sentence = ""
            pro.update(1)
        pro.close()
        ALL_time_stamp.append(this_title.strip())
        ALL_time.append(total_time)
       
    ALL_time_stamp.append(WORD_LANG_DICT[lang]['Thanks'])

    ALL_videos.append(ending_video)


    logger.info("[*] Building final video ...")

    Final_video_save_path = os.path.join(today_floder,f"Final_{lang}.mp4")

    ALL_videos = combined_all_video(ALL_videos,Final_video_save_path)

    logger.info(f"[#] Finished! save the video to {Final_video_save_path}")


    logger.info(f"【News】 {(datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')} {ALL_time_stamp[4]}")


    time_stamp_path = os.path.join(today_floder,"Final_en.txt")


    with open(time_stamp_path,"w",encoding="utf8") as f:
        start_time = 0
        total_time = 0
        for i in range(len(ALL_time)):

            total_time += ALL_time[i]
            start_time_word = str(timedelta(seconds=start_time))
            total_time_word = str(timedelta(seconds=ceil(total_time)))
            this_line = f"{start_time_word}\t{ALL_time_stamp[i]}\n"
            start_time = floor(total_time)
            print(this_line)
            f.write(this_line)
    logger.info(f"[#] Saving the video time stamp to Final.txt")


    logger.info("[*] uoloading yt")
    upload_yt(today_date,lang)


    
