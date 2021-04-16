# import library
import speech_recognition as sr
from translate import Translator
from google_trans_new import google_translator
# Initialize recognizer class (for recognizing the speech)

# Reading Audio file as source
# listening the audio file and store in audio_text variable
fileno = 1
path = "Audio part -1.wav"
f = open("Ashoka Subtitles_English Episode 125.txt","w",encoding="utf-8")
start="0:0:0"
end="0:0:5"
while fileno<=249:
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_text = r.listen(source)
        print(start, end)
        #recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text,language="hi-IN")
            print('Converting audio transcripts into text ...'+path)
            temp=start+"-"+end+" "+path
            f.write(temp)
            f.write("\n")
            f.write(text)
            f.write("\n")
            print(text)
            translator = google_translator()
            translate_text = translator.translate(text, lang_src='hi', lang_tgt='ta')
            print(translate_text)
            f.write(translate_text)
            f.write("\n")
            start=end
            hour,minute,seconds = end.split(":")
            minute=int(minute)
            seconds=int(seconds)
            hour=int(hour)
            if seconds+5==60:
                minute+=1
                if minute == 60:
                    hour+=1
                    minute=0
                seconds="0"
                end = str(hour)+":"+str(minute)+":"+str(seconds)
            else:
                seconds+=5
                end = str(hour)+":"+str(minute)+":"+str(seconds)
        except:
            temp=start+"-"+end+" "+path
            text = "Either background music or couldn't recognize audio...."
            f.write(temp)
            f.write("\n")
            f.write(text)
            f.write("\n")
            print(text+path)
            start = end
            hour,minute,seconds = end.split(":")
            minute = int(minute)
            seconds = int(seconds)
            hour=int(hour)
            if seconds + 5 == 60:
                minute += 1
                if minute==60:
                    hour+=1
                    minute=0
                seconds = "0"
                end = str(hour)+":"+str(minute) + ":" + str(seconds)
            else:
                seconds += 5
                end = str(hour)+":"+str(minute) + ":" + str(seconds)
    fileno+=1
    path="Audio part -"+str(fileno)+".wav"
f.close()