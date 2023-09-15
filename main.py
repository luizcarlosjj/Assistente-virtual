import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit
import wikipedia

# Selecione o audio para reconhecimento
audio = sr.Recognizer()
# Inicia a IA
maquina = pyttsx3.init()

while True:
    def executa_comando():
        try:
            with sr.Microphone() as source:
                print('Ouvindo..')
                voz = audio.listen(source) # Lista as entradas de audio
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower() # Converte as entradas de audio para minisiculo
                if 'tina' in comando:
                    comando = comando.replace('tina', '') # Troca a entrada 'tina' por nada
                    maquina.runAndWait()
        except:
            print('Microfone OFF')

        return comando

    def comando_voz_usuario():
        comando = executa_comando()
        if 'horas' in comando:
            hora = datetime.now().strftime('%H:%M')
            maquina.say('Agora são' + hora)
            maquina.runAndWait()

        elif 'dia' in comando:
            data = datetime.today()
            datatxt = f'{data.day} do {data.month}'
            maquina.say('Hoje é dia ' + datatxt)
            maquina.runAndWait()

        elif 'procure por' in comando:
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,2) 
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()

        elif 'escutar' in comando:
            musica = comando.replace('escutar', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Tocando Musica')
            maquina.runAndWait()

        elif 'enviar mensagem' in comando:
            msg = pywhatkit.sendwhatmsg_instantly('+5562984824354', 'Olá Mãe Bom dia!', 15, True, 2)
            maquina.say('Mensagem enviada!')
            maquina.runAndWait()

    comando_voz_usuario()
