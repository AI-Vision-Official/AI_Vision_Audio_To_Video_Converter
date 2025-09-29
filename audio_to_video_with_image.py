import os
import traceback
from moviepy.editor import *

def create_video_with_image(image_path, audio_path, output_path):
    try:
        audio = AudioFileClip(audio_path)
        duration = audio.duration

        image_clip = ImageClip(image_path, duration=duration)
        image_clip = image_clip.set_duration(duration)
        image_clip = image_clip.set_audio(audio)
        image_clip = image_clip.resize(height=1080)
        image_clip = image_clip.set_fps(24)
        image_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    except Exception as e:
        print(f"❌ Fout bij maken video voor {audio_path}:\n{e}")
        traceback.print_exc()

def bulk_convert_with_image(image_folder, audio_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(audio_folder):
        if file.endswith(".mp3"):
            name = os.path.splitext(file)[0]
            audio_path = os.path.join(audio_folder, file)
            output_path = os.path.join(output_folder, name + ".mp4")

            # Zoek cover image (jpg/png) met dezelfde naam
 for ext in [".jpg", ".jpeg", ".png"]:
    candidate = os.path.join(image_folder, name + ext)
    if os.path.exists(candidate):
        image_path = candidate
        break
else:
    for fallback in ["album_cover.jpg", "album_cover.jpeg", "album_cover.png"]:
        fallback_path = os.path.join(image_folder, fallback)
        if os.path.exists(fallback_path):
            image_path = fallback_path
            break
    else:
        print(f"⚠️ Geen afbeelding gevonden voor {file}. Bestand wordt overgeslagen.")
        continue

            print(f"📷 Gebruikt beeld: {os.path.basename(image_path)} voor {file}")
            create_video_with_image(image_path, audio_path, output_path)

    print("✅ Alle video's zijn succesvol gemaakt (met afbeelding).")

# Instellingen
image_folder = "mp3s"
audio_folder = "mp3s"
output_folder = "output_videos"

bulk_convert_with_image(image_folder, audio_folder, output_folder)