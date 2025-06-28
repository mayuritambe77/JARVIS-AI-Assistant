import speech_recognition as sr
import wikipedia 
import openai
import win32com.client
import webbrowser
import openai
import datetime

from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    openai.api_key = apikey
    client = openai.OpenAI(api_key=apikey)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "user", "content": "Write an email to my boss for resignation"}
        ],
        temperature=0.7,
        max_tokens=256
    )
#todo: wrap this inside try catch block
print(response[0],text)

def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=0) as source:  # Replace 0 with your mic index
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(query)
            return query
        except Exception as e:
            return "some error occured...sorry from JARVIS"



    except Exception as e:
        print("Error:", e)
        return "None"


# Main logic
if __name__ == "__main__":
    print("Welcome to JARVIS Assistant")
    # todo:This helps to open websites based on your command
    while True:
        print("listening...")
        text = takeCommand()
        speaker.speak(text)
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.youtube.com"],]
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                speaker.Speak(f"opening {site[0]} sir")
                webbrowser.open(site[0])

            #todo:This shows the current time
            if "the time".lower() in text.lower():
                now = datetime.datetime.now()
                hour = now.strftime("%H")
                minute = now.strftime("%M")
                speaker.Speak(f"The time is {hour} hour and {minute} minutes")

            if "openai".lower() in text.lower():
                ai(prompt=text)




            









