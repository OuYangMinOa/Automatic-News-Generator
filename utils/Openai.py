## openai
import openai
from utils.MyLog import logger


my_keys = eval(os.getenv("OPENAI_TOKEN"))
openai.api_key = my_keys[key_index]
key_index = 0

def prompt_openai(word):
    time.sleep(10)
    try:
        completion = openai.Completion.create(engine="text-davinci-003",temperature= 0.5, prompt=word,max_tokens=1024)
        return remove_num_comma(completion.choices[0].text)
        
    except openai.error.RateLimitError:
        logger.info("[*] Change api key")
        key_index = (key_index+1)%3
        openai.api_key = my_keys[key_index]
        return prompt_openai(word)

    except openai.error.InvalidRequestError:
        log.warning("[*] Prompt to many words ..., Cutting down")
        return prompt_openai("\n".join(word.split('\n')[:-1]))
    except Exception as e:
        logger.error(e)
        time.sleep(10)
        return prompt_openai(word)
