"""
离线语音引擎
    1.运行前需要安装第三方库 pyttsx3，可使用以下命令进行安装：
        pip install pyttsx3
    2.若安装过程中出现超时问题，可使用国内镜像源进行安装，命令如下：
        pip install -i https://mirrors.aliyun.com/pypi/simple/ pyttsx3
"""
import pyttsx3

"""
该函数用于使用 pyttsx3 库将传入的文本转换为语音并播放。
    1.参数:
        text (str): 要转换为语音的文本内容。
"""
def speak_text(text = "初心学习python,语雀找到我 https://www.yuque.com/chuxin-cs"):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
