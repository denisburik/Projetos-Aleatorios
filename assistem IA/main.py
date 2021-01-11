import speech_recognition as sr
import pyttsx3
from random import choice
from confg import *

reproducao = pyttsx3.init('sapi5')

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():

    while True:
        resposta_ale = choice(lista_erro)  
        rec = sr.Recognizer()
        with sr.Microphone() as s:

            rec.adjust_for_ambient_noise(s)

            while True:
                try:  
                    audio = rec.listen(s)  
                    user_name = rec.recognize_google(audio,language='pt-BR')
                    user_name = verify_name(user_name)

                    name_list_open()
                    apresentacao = "{}".format(verify_name_exist(user_name))

                    sai_som(apresentacao)

                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]

                    break

                except sr.UnknownValueError:
                    sai_som(resposta_ale)
                    #Nao esta funcinando offline
            break

    print("=" * len(apresentacao))
    print("Ouvindo...")
    while True:
        resposta_ale = choice(lista_erro)  
        rec = sr.Recognizer()
        with sr.Microphone() as s:

            rec.adjust_for_ambient_noise(s)

            while True:
                try:  
                    audio = rec.listen(s)  
                    frase = rec.recognize_google(audio,language='pt-BR')

                    print("{}".format(frase))
                    resposta = conversa[frase]

                    print("Assistente: {}".format(resposta))
                    sai_som("{}".format(resposta))

                except sr.UnknownValueError:
                    sai_som(resposta_ale)
                    #Nao esta funcinando offline




if __name__ == "__main__":
    intro()
    sai_som(introMsg)
    assistente()