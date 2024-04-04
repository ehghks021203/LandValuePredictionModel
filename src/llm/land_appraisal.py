import openai
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import Chatbot

# ChatGPT Setting
openai.api_key = Chatbot.OPENAI_KEY

def create(land_info: str, sys_msg="") -> str:
    messages = []
    if sys_msg == "":
        sys_msg = f"""
            너는 이제부터 토지의 가치를 평가하는 감정평가사야. 주어진 정보를 바탕으로 평가된 토지 가격이 어떻게 산출되었는지 논리적으로 설명해야해.
            모든 설명을 마치고 마지막에는 제곱미터당 가격과 토지면적과 곱한 가격을 모두 말해줘야해.
        
        """

    messages.append({"role":"system", "content":sys_msg})
    messages.append({"role":"user", "content":land_info})

    chatbot = openai.ChatCompletion.create(
        model = Chatbot.MODEL,
        messages = messages
    )
    bot_msg = chatbot["choices"][0]["message"]["content"]
    return bot_msg

if __name__ == "__main__":
    create()