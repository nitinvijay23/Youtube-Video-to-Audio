
# coding: utf-8

# In[2]:

import pafy
import os
import moviepy.editor as mp


print("[+] Welcome to Youtube video to mp3 convertor.")
download_url = input("URL :")

#download_url  ='https://www.youtube.com/watch?v=jebJ9itYTJE'
video = pafy.new(download_url)
best = video.streams
file_name = video.streams[0]
print(file_name)

directory = "downloaded-music"
if not os.path.exists(directory):
    os.makedirs(directory)
x = file_name.download(filepath = directory)

clip = mp.VideoFileClip(x)
#printclip.size
clip.audio.write_audiofile(x + ".mp3")

#os.remove(x)


# In[ ]:



