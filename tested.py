from moviepy.editor import *

def convert_to_gif():
    clip = VideoFileClip(r"C:\Users\PC\Downloads\b4cac033-d6fe-469b-8d5b-e7b6d3a5f41f.mp4")
    clip = clip.subclip(0, 3)
    clip.write_gif("mygif.gif")
