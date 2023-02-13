# make video 
from moviepy.editor import *
from moviepy.config import change_settings
import numpy as np
import glob
import os

change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"})

def build_video(text_cont  = ""   , 
                song_path  = ""   ,
                save_path  = ""   ,
                width      = 1920 ,
                height     = 1080 ,
                fps        = 60   ,
                color      = 'white', 
                fontsize   = 25   ,
                image_path = None ):

    # 創建函數 make_frame 用於創建影格
    def make_frame(t):
        frame = np.zeros((height, width, 3))
        return frame

    # 創建一個音檔緩衝區
    audio = AudioFileClip(song_path)

    # 創建影片
    clip = VideoClip(make_frame, duration=audio.duration)
    clip.fps = fps
    clip.write_videofile(save_path, verbose=False, logger=None ,codec='h264_nvenc')  # h264_qsv   h264_nvenc

    if (image_path):
        is_title_clip = False
        try:    
            now_clip_num     = int(os.path.basename(song_path).replace('.mp3',''))
            if (now_clip_num == 0): is_title_clip = True
        except: 
            now_clip_num     = 0

        if (not is_title_clip):
            try:
                all_images_path          = glob.glob(image_path+'/*.png')
                if (len(all_images_path)!= 0):
                    try:    
                        this_image_path = all_images_path[now_clip_num]
                    except: 
                        this_image_path = all_images_path[-1]
                else:
                    this_image_path = np.random.choice(glob.glob('pic/*.png'))
            except:
                this_image_path = np.random.choice(glob.glob('pic/*.png'))
            try:
                image      = ImageClip(this_image_path).set_duration(audio.duration).set_pos(("center",100))
                new_height = 800-fontsize*len(text_cont.split("\n"))
                new_width  = int(new_height/image.size[1] * image.size[0])

                if (new_width>1920):
                    new_height = int(1720/new_width * new_height)
                    new_width  = 1720
                
                image = image.resize(height=new_height,width=new_width)
                clip = CompositeVideoClip([clip, image])
            except:
                image_path = None

    # 創建一個文字緩衝區 
    if (image_path):
        txt = TextClip(text_cont,color=color,font="SourceHanSerifTC-Medium.otf",fontsize=fontsize).set_duration(audio.duration).set_position(('center',980 - fontsize*len(text_cont.split("\n"))) )

    else:
        txt = TextClip(text_cont,color=color,font="SourceHanSerifTC-Medium.otf",fontsize=fontsize).set_duration(audio.duration).set_position('center' )
        

    # 將音檔和文字合併
    clip.audio = CompositeAudioClip([audio])

    # 將影片和音檔合併
    video = CompositeVideoClip([clip, txt])

    # 輸出成檔案
    video.write_videofile(save_path, verbose=False, logger=None,codec='h264_nvenc')
    
    return audio.duration

def combined_all_video(video_arr,save_path=""):
    clips = []
    for i in video_arr:
        clips.append(VideoFileClip(i))
    video = concatenate_videoclips(clips)
    video.write_videofile(save_path, verbose=False, logger=None,codec='h264_nvenc')

def get_video_time(save_path):
    video = VideoFileClip(save_path)
    return video.duration
