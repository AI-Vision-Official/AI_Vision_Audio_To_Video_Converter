"""
Script: audio_to_video_with_loop.py
Beschrijving:
Maakt MP4-video’s van MP3-bestanden door een (loopende) video als visueel te gebruiken.
Zoekt naar een mp4-video met dezelfde naam als de mp3.
Als die er niet is, wordt standaard 'loop_video.mp4' gebruikt.
"""

import os
from moviepy.editor import *

def create_video_with_loop(loop_video_path, audio_path, output_path):
    audio = AudioFileClip(audio_path)
    duration = audio.duration

    loop_clip = VideoFileClip(loop_video_path)
    loop_clip = loop_clip.resize(height=1080).set_fps(24).without_audio()
    looped = loop_clip.loop(duration=duration).set_duration(duration)
    final = looped.set_audio(audio)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

def bulk_convert_with_loop(video_folder, audio_folder, output_folder, default_loop_video="loop_video.mp4"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(audio_folder):
        if file.endswith(".mp3"):
            name = os.path.splitext(file)[0]
            audio_path = os.path.join(audio_folder, file)
            output_path = os.path.join(output_folder, name + ".mp4")

            custom_loop = os.path.join(video_folder, name + ".mp4")
            loop_path = custom_loop if os.path.exists(custom_loop) else os.path.join(video_folder, default_loop_video)

            print(f"🎞️ Gebruikt video: {os.path.basename(loop_path)} voor {file}")
            create_video_with_loop(loop_path, audio_path, output_path)

    print("✅ Alle video's zijn succesvol gemaakt (met video-loop).")

# Instellingen
video_folder = "loop_videos"
audio_folder = "mp3s"
output_folder = "output_videos"

bulk_convert_with_loop(video_folder, audio_folder, output_folder)
