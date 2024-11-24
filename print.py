import abstractive as ab
import extractive as ex
import ytranscript as yt
import vtranscript as vt
from string import punctuation

file="videoplayback (1).mp4"
text=yt.extract_ytube('https://www.youtube.com/watch?v=St48epdRDZw')
# print(text)

count=text.split()
count=count[0:1000]
print(len(count))
text=' '.join(count)