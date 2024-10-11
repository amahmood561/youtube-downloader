# main.py
import argparse
from downloader.video_downloader import download_video, download_audio, download_playlist

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="URL of the YouTube video or playlist")
    parser.add_argument("--output", help="Output directory", default="downloads")
    parser.add_argument("--resolution", help="Video resolution (e.g., 720p, 1080p)", default="720p")
    parser.add_argument("--audio", help="Download audio only", action="store_true")
    parser.add_argument("--playlist", help="Download entire playlist", action="store_true")
    
    args = parser.parse_args()

    if args.playlist:
        download_playlist(args.url, args.output, args.resolution)
    elif args.audio:
        download_audio(args.url, args.output)
    else:
        download_video(args.url, args.output, args.resolution)

if __name__ == "__main__":
    main()
