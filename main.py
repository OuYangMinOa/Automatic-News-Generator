# main.py
from utils.NewGraber  import GrabChineseNews, GrabEnglishNews
from src.NewGenerator import MakerNew


def main(hour=16, dmin=5):
    print(f"Set at everyday {hour}:00")
    while True:
        tw_time =  datetime.now().strftime("%H")
        us_time = (datetime.now()-timedelta(hours=12)).strftime("%H")
        if (now_time == str(hour)):
            print("="*100)
            print(datetime.now().strftime("%D-%H:%M"))

            
            MakerNew(GrabChineseNews, lang="zh-tw")


            print("="*100)
            print(datetime.now().strftime("%D-%H:%M"))
        if (us__time == str(hour)):
            print("="*100)
            print(datetime.now().strftime("%D-%H:%M"))


            MakerNew(GrabEnglishNews, lang="en")


            print("="*100)
            print(datetime.now().strftime("%D-%H:%M"))


        time.sleep(60*dmin)


if __name__ == '__main__':
    main()









