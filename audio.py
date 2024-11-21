import speech_recognition as speech_recog
import pandas as pd

"""def speech():
    mic= speech_recog.Microphone()
    recog= speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        return recog.recognize_google(audio,language = "en-GB")

mic= speech_recog.Microphone()
recog= speech_recog.Recognizer()
with mic as audio_file:
    print("Porfavor habla")
    recog.adjust_for_ambient_noise(audio_file)
    audio= recog.listen(audio_file)
    print("Convertiremos la voz en texto . . .")
    print("As dicho : " + recog.recognize_google(audio,language = "en-GB"))"""

def speech_en():
    mic= speech_recog.Microphone()
    recog= speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        return recog.recognize_google(audio,language="en-MX")

def speech_ing():
    data = {'spanish': ['hola', 'adiós', 'gracias', 'por favor'],
        'english': ['hello', 'goodbye', 'thank you', 'please']}
    df = pd.DataFrame(data)
    mic= speech_recog.Microphone()
    recog= speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        voz = recog.recognize_google(audio,language="en-MX")
        palabras = voz.split()
        traduccion_frase = ""
        for palabra in palabras:
            translation = df.loc[df['spanish'] == palabra, 'english'].values
            if len(translation) > 0:
                traduccion_frase += translation[0] + " "
        return traduccion_frase.strip()