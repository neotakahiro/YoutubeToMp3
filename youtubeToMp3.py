from pytube import YouTube
from moviepy.editor import *
import os

# YouTubeのURLを入力として受け取ります
url = input("YouTubeのURLを入力してください: ")

# YouTube動画をダウンロード
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
download_path = "/Users/nagaminetakahiro/Desktop/Youtube mp3/"
stream.download(output_path=download_path)

# ダウンロードした動画をMP3に変換
video_path = os.path.join(download_path, yt.title + ".mp4")
mp3_path = os.path.join(download_path, yt.title + ".mp3")

video = AudioFileClip(video_path)
video.write_audiofile(mp3_path)

# 不要な中間ファイルを削除
os.remove(video_path)

print("ダウンロードと変換が完了しました。MP3ファイルは以下の場所に保存されました:")
print(mp3_path)


#python3 youtubeToMp3.py
#で実行。