# -*- coding: utf-8 -*-
"""YT_Transcript.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zsQXPrFGx1Az09hHTnjxumiqm2za08VF
"""

import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'youtube-transcript-api'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytube'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'chardet'])

# prompt: With pytube create a function that has as input a URL and then outputs the YouTube video ID

import pytube

def get_video_id(url):
  yt = pytube.YouTube(url)
  return yt.video_id

# your_custom_script.py

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_text_transcript(video_id,file_name_txt):
  # Must be a single transcript.
  transcript = YouTubeTranscriptApi.get_transcript(video_id)

  formatter = TextFormatter()

  # .format_transcript(transcript) turns the transcript into a Text string.
  text_formatted = formatter.format_transcript(transcript)


  # Now we can write it out to a file.
  with open(file_name_txt, 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)
  return text_file

# prompt: Create a script that uses system arguments to request a URL, a text file name, and then the code calls the precious cells functions to output a transcript file

import sys

# Get the URL, text file name, and video ID from the command line arguments.
url = sys.argv[1]
file_name_txt = sys.argv[2]
video_id = get_video_id(url)

#url = "https://youtu.be/0LNQxT9LvM0?si=tErSMtgH06I7NCvx"
#file_name_txt = "test1.txt"
#video_id = get_video_id(url)

# Get the text transcript and write it to the specified file.
text_file = get_text_transcript(video_id, file_name_txt)

# Print a message to indicate that the transcript has been saved.
print("Transcript saved to", text_file.name)
