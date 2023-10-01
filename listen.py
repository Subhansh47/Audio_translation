import speech_recognition as sr
from googletrans import Translator


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening!')
        r.pause_threshold = 1
        audio = r.listen(source, 0, 3)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language='hi')

    except:
        return " "

    query = str(query).lower()
    return query


def translation(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line, 'en')
    data = result.text
    print(data)
    return data


def MicExecution():
    query = listen()
    data = translation(query)
    return data
