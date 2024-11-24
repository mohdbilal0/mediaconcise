import moviepy.editor as mp
import speech_recognition as sr
import whisper
import warnings
import os

def extract_vid(vid):
    # try:
    video=mp.VideoFileClip(vid)
    audio_file=video.audio
    audio_file.write_audiofile("temp.wav")


    warnings.filterwarnings('ignore')
    model = whisper.load_model("base")
    result = model.transcribe("temp.wav")
    text=str(result["text"])
    
        
    # except Exception as e:
    #     print(e)
    return text