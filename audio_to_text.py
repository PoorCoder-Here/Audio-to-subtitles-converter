from pydub import AudioSegment

audio_file= "Chakravartin Ashoka Samrat _ Episode 125.wav"
"""audio = AudioSegment.from_wav(audio_file)
list_of_timestamps = [ 10, 20, 30, 40, 50 ,60, 70, 80, 90 ] #and so on in *seconds*

start = 0
for  idx,t in enumerate(list_of_timestamps):
    #break loop if at last element of list
    if idx == len(list_of_timestamps):
        break

    end = t * 1000 #pydub works in millisec
    print ("split at [ {}:{}] ms".format(start, end))
    audio_chunk=audio[start:end]
    audio_chunk.export( "audio_chunk_{}.wav".format(end), format="wav")

    start = end * 1000 #pydub works in millisec"""
t11=0
t22=5
i=1
while True:
    t1 = t11 * 1000 #Works in milliseconds
    t2 = t22 * 1000
    newAudio = AudioSegment.from_wav(audio_file)
    newAudio = newAudio[t1:t2]
    s="Audio part -"+str(i)+".wav"
    i+=1
    newAudio.export(s, format="wav") #Exports to a wav file in the current path.
    audio_seg = AudioSegment.from_wav(s)
    total_in_ms = len(audio_seg)
    if total_in_ms == 0:
        break
    t11=t22
    t22+=5
