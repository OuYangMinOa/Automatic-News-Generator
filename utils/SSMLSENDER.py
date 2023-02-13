from datetime import datetime

import websocket as websoc
import argparse
import requests
import asyncio
import time
import re
import uuid


def hr_cr(hr):
    corrected = (hr - 1) % 24
    return str(corrected)

# Add zeros in the right places i.e 22:1:5 -> 22:01:05
def fr(input_string):
    corr = ''
    i = 2 - len(input_string)
    while (i > 0):
        corr += '0'
        i -= 1
    return corr + input_string

# Generate X-Timestamp all correctly formatted
def getXTime():
    now = datetime.now()
    return fr(str(now.year)) + '-' + fr(str(now.month)) + '-' + fr(str(now.day)) + 'T' + fr(hr_cr(int(now.hour))) + ':' + fr(str(now.minute)) + ':' + fr(str(now.second)) + '.' + str(now.microsecond)[:3] + 'Z'

# Async function for actually communicating with the websocket
def transferMsTTSData(SSML_text, outputPath,host, port):
    req_id = uuid.uuid4().hex.upper()
    endpoint2 = f"wss://eastus.api.speech.microsoft.com/cognitiveservices/websocket/v1?TrafficType=AzureDemo&Authorization=bearer%20undefined&X-ConnectionId={req_id}"
    websocket = websoc.create_connection(endpoint2,http_proxy_host=host, http_proxy_port=port)
    payload_1 = '{"context":{"system":{"name":"SpeechSDK","version":"1.12.1-rc.1","build":"JavaScript","lang":"JavaScript","os":{"platform":"Browser/Linux x86_64","name":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0","version":"5.0 (X11)"}}}}'
    message_1 = 'Path : speech.config\r\nX-RequestId: ' + req_id + '\r\nX-Timestamp: ' + \
        getXTime() + '\r\nContent-Type: application/json\r\n\r\n' + payload_1
    websocket.send(message_1)

    payload_2 = '{"synthesis":{"audio":{"metadataOptions":{"sentenceBoundaryEnabled":false,"wordBoundaryEnabled":false},"outputFormat":"audio-16khz-32kbitrate-mono-mp3"}}}'
    message_2 = 'Path : synthesis.context\r\nX-RequestId: ' + req_id + '\r\nX-Timestamp: ' + \
        getXTime() + '\r\nContent-Type: application/json\r\n\r\n' + payload_2
    websocket.send(message_2)

    # payload_3 = '<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="' + voice + '"><mstts:express-as style="General"><prosody rate="'+spd+'%" pitch="'+ptc+'%">'+ msg_content +'</prosody></mstts:express-as></voice></speak>'
    payload_3 = SSML_text
    message_3 = 'Path: ssml\r\nX-RequestId: ' + req_id + '\r\nX-Timestamp: ' + \
        getXTime() + '\r\nContent-Type: application/ssml+xml\r\n\r\n' + payload_3
    websocket.send(message_3)

        # Checks for close connection message
    end_resp_pat = re.compile('Path:turn.end')
    audio_stream = b''
    while(True):
        response = websocket.recv()
        # Make sure the message isn't telling us to stop
        if (re.search(end_resp_pat, str(response)) == None):
            # Check if our response is text data or the audio bytes
            if type(response) == type(bytes()):
                # Extract binary data
                try:
                    needle = b'Path:audio\r\n'
                    start_ind = response.find(needle) + len(needle)
                    audio_stream += response[start_ind:]
                except:
                    pass
        else:
            break
    websocket.close()
    with open(outputPath, 'wb') as audio_out:
        audio_out.write(audio_stream)


def mainSeq2(SSML_text, outputPath,host, port):
    transferMsTTSData(SSML_text, outputPath,host, port)