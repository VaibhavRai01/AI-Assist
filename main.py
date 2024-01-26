import random
import webbrowser
import openai
from openai import OpenAI
import speech_recognition as sr
import os
import win32com.client
from config import apikey

chatstr = ""


def chat(query):
    global chatstr
    chatstr += f"Vaibhav: {query}\n Bestie: "
    client = OpenAI(api_key=apikey)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response.choices[0].text)
    chatstr += response.choices[0].text
    return response.choices[0].text


def ai(prompt):
    text = f"OpenAI response for :{query} \n \n"
    client = OpenAI(api_key=apikey)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    print(response.choices[0].text)
    text += response.choices[0].text
    with open(f"Openai/prompt- {random.randint(1, 1234567)}.txt", "w") as f:
        f.write(text)


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "can't understand what you are saying"


if __name__ == '__main__':
    print('PyCharm')
    say("hello vaibhav ")
    while True:
        print("listening..")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.gooogle.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open postman".lower() in query.lower():
            postman_path = r"C:\Users\VAIBHAV RAI\AppData\Local\Postman\Postman.exe"
            os.system(f"start \"\" \"{postman_path}\"")

        elif "open club intro".lower() in query.lower():
            postman_path = r"C:\Users\VAIBHAV RAI\OneDrive\Desktop\vaibhav\club-intro.MOV"
            os.system(f"start \"\" \"{postman_path}\"")

        elif "open ai".lower() in query.lower():
            ai(prompt=query)

        elif "exit".lower() in query.lower():
            exit()
        else:
            chat(query)
        # say(query)
