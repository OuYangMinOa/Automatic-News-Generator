
from utils.ProxyGraber import proxies
from utils.AudioMaker  import build_audio3
from utils.VideoMaker  import build_video
from utils.info        import Proxy_file
import os


test_audio_path = "tests/test.mp3"
test_video_path = "tests/test.mp4"

def test_proxies_audio():
    p = proxies(num=20)
    p.verify_proxy()
    p.save_proxy(Proxy_file)
    assert os.path.isfile(Proxy_file)

    hosts , ports = p.get_proxies()

    for i,j in zip(hosts , ports):
        try:
            
            build_audio3("測試", save_path=test_audio_path, host=i, port=j)
            break
        except:
            pass


    assert os.path.isfile(test_audio_path)

    p.delete_proxy_file(Proxy_file)

    assert (not os.path.isfile(Proxy_file))




def test_build_video():
    build_video('測試',test_audio_path,test_video_path )

    assert os.path.isfile(test_video_path)
