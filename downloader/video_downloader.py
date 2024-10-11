# downloader/video_downloader.py
from pytube import YouTube, Playlist
import os
import ffmpeg

def download_video(url, output_dir='downloads', resolution='720p'):
    """Download a video from YouTube."""
    yt = YouTube(url)
    video_stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    
    if not video_stream:
        print(f"Resolution {resolution} not available for this video. Downloading the highest resolution instead.")
        video_stream = yt.streams.get_highest_resolution()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    video_stream.download(output_path=output_dir)
    print(f"Downloaded video: {yt.title} to {output_dir}")

def download_audio(url, output_dir='downloads'):
    """Download audio-only from a YouTube video."""
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio_file = audio_stream.download(output_path=output_dir)
    # Convert to MP3 using ffmpeg
    mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
    ffmpeg.input(audio_file).output(mp3_file).run(overwrite_output=True)
    os.remove(audio_file)  # Remove the original file after conversion
    print(f"Downloaded audio: {yt.title} to {mp3_file}")

def download_playlist(playlist_url, output_dir='downloads', resolution='720p'):
    """Download all videos from a YouTube playlist."""
    playlist = Playlist(playlist_url)
    
    print(f"Downloading playlist: {playlist.title}")
    for url in playlist.video_urls:
        download_video(url, output_dir, resolution)
    print("Playlist download complete.")
