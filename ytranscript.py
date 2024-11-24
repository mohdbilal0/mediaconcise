
import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def extract_ytube(link):
    youtube_video_url=link
    video_id = youtube_video_url.split("=")[1]
    text=YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ""
    for i in text:
        transcript += " " + i["text"]
    return transcript

