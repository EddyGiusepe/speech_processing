'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo: https://levelup.gitconnected.com/simple-example-of-speech-to-text-a86fff4ab626


'''
Google Speech to Text em Python


O reconhecimento de fala (ou Speech To Text) ainda está longe de ser perfeito. No entanto, a biblioteca SpeechRecognition
fornece uma maneira fácil de interagir com muitas APIs de conversão de fala em texto. Neste script, mostraremos como usar a biblioteca
Python SpeechRecognition (https://pypi.org/project/SpeechRecognition/) para começar a converter facilmente o idioma falado em nossos
arquivos de áudio para texto.
'''


'''
Speech To Text with SpeechRecognition

SpeechRecognition é uma biblioteca para realizar reconhecimento de fala, com suporte para diversos engines e APIs, online e offline.

Suporte para mecanismo de reconhecimento de fala/API:

* CMU Sphinx (funciona offline) --> https://cmusphinx.github.io/wiki/
* Google Speech Recognition 
* Google Cloud Speech API --> https://cloud.google.com/speech-to-text?hl=pt-br
* Wit.ai --> https://wit.ai/
* Microsoft Azure Speech  --> https://azure.microsoft.com/en-us/products/cognitive-services/speech-services/
* Microsoft Bing Voice Recognition (Deprecated)  --> https://azure.microsoft.com/pt-br/products/cognitive-services/speech-services/
* Houndify API  --> https://www.soundhound.com/
* IBM Speech to Text --> https://www.ibm.com/lets-create/
* Snowboy Hotword Detection (works offline)
'''

'''
Para o nosso exemplo, usaremos o recognize_google, porém também existem algumas outras opções como recognize_bing(), recognize_wit(). O arquivo
.wav de áudio que usaremos para este exemplo pode ser encontrado aqui (https://drive.google.com/file/d/15Y8rAL2p9b6N4vf8FV1NxTwmPtFafO1Z/view).
Observe que o recognize_google permite 50 chamadas gratuitas por dia.
'''


# Importo a biblioteca de ASR (Reconhecimento de Fala)
import speech_recognition as sr

# Crie uma instância da classe Recognizer
recognizer = sr.Recognizer()

# Defino o threshold de energia
'''
Representa a amplitude mínima de um sinal de áudio que é considerado como um sinal de fala. Ele é usado para separar o sinal de fala do ruído
ou outros sons de fundo, como respiração ou barulho ambiente. Qualquer trecho com energia abaixo desse valor é ignorado e tratado como
ruído ou silêncio. O valor do Energy Threshold varia de acordo com a sensibilidade do sistema de reconhecimento de fala ou a natureza do áudio.
'''
recognizer.energy_threshold = 300

# Converter áudio para AudioFile 
clean_support_call = sr.AudioFile("/home/eddygiusepe/1_Eddy_Giusepe/speech_processing/Google_Speech_to_Text_in_Python/audio_2text.wav")

# Converter AudioFile para AudioData 
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcrever AudioData para texto 
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="pt-BR") # language = "pt-BR"   e   language="en-US"   

print("A seguir mostramos a Transcrição: ")
print('')
print(text)


'''
Speech to Text with Noisy Audio

Às vezes, temos que lidar com arquivos de áudio barulhentos (Noisy audio). Podemos usar a função "adjust_for_ambient_noise()"
de "Recognizer" para anular o ruído de fundo. Usaremos este texto de áudio (https://drive.google.com/file/d/1dM0gG4plX628CdPT35stwRqvvgmT717W/view)
para o nosso exemplo.
'''
# Importando a biblioteca de speech_recognition
import speech_recognition as sr
recognizer = sr.Recognizer()

# Convert áudio para AudioFile
noisy_support_call = sr.AudioFile("/home/eddygiusepe/1_Eddy_Giusepe/speech_processing/Google_Speech_to_Text_in_Python/audio_2text.wav")

# Grave o áudio da noisy_support_call
with noisy_support_call as source:
 # Ajusto o threshold de recognizer energy para ruído ambiente (ambient noise)
    recognizer.adjust_for_ambient_noise(source, duration=0.7)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcrição
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="pt-BR")

print("Transcrição de áudio com RUÍDO: ")
print('')
print(text)
