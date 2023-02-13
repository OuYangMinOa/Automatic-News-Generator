# AudioMaker

from utils.SSMLSENDER import mainSeq2


def build_audio3(text,save_path="song.mp3",api="pyttsx3",lang='zh-tw', host="127.0.0.1",port=80):
    if (lang=="zh-tw"):
        this_ssml = f"""<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
        <voice name="zh-CN-YunxiNeural">
            <mstts:express-as style="chat">
                <prosody rate="0%" pitch="0%">{text}</prosody>
            </mstts:express-as>
        </voice>
    </speak>"""
        mainSeq2(this_ssml, save_path,host, port)
        return

    if (lang=="en"):
        this_ssml = f"""<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
        <voice name="en-US-BrandonNeural">
            <mstts:express-as style="chat">
                <prosody rate="0%" pitch="0%">{text}</prosody>
            </mstts:express-as>
        </voice>
    </speak>"""
        mainSeq2(this_ssml, save_path,host, port)
        return





