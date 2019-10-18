import speech_recognition as sr
import pyttsx3
from random import choice
from confg import *

reproducao = pyttsx3.init('sapi5')

def sai_som(resposta):
  reproducao.say(resposta)
  reproducao.runAndWait()


print("Ouvindo.........")

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