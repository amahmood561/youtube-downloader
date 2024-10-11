# YouTube Downloader

**YouTube Downloader** is a command-line tool for downloading YouTube videos and audio. It allows you to download videos in various resolutions, extract audio, and download entire playlists. The tool is built using Python and makes use of the `pytube` library for downloading videos and `ffmpeg` for audio conversion.

## Features

- **Download YouTube Videos**: Download videos in various resolutions (e.g., 720p, 1080p).
- **Download Audio Only**: Extract audio from YouTube videos and save it as MP3.
- **Download Playlists**: Download all videos in a playlist.
- **Command-Line Interface (CLI)**: Simple and easy-to-use command-line interface.
- **Customizable Output Directory**: Specify where to save the downloaded files.

## Prerequisites

Before you begin, make sure you have the following installed:
- **Python 3.8+**
- **FFmpeg** (for converting audio to MP3)

### Installing FFmpeg

You need to install FFmpeg for audio conversion:

- **Windows**: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add it to your PATH.
- **macOS**: Use Homebrew:
  ```bash
  brew install ffmpeg
  ```
- **Linux**: Use your package manager:
  ```bash
  sudo apt install ffmpeg
  ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can use the tool from the command line to download videos, audio, or playlists.

### 1. Download a Single Video

Download a YouTube video in the default resolution (720p):

```bash
python main.py https://www.youtube.com/watch?v=example_video_id
```

### 2. Download Audio Only

Extract audio from a YouTube video and save it as an MP3:

```bash
python main.py https://www.youtube.com/watch?v=example_video_id --audio
```

### 3. Download a Playlist

Download all videos from a YouTube playlist:

```bash
python main.py https://www.youtube.com/playlist?list=example_playlist_id --playlist
```

### 4. Specify Output Directory and Resolution

You can customize the output directory and specify the desired resolution:

```bash
python main.py https://www.youtube.com/watch?v=example_video_id --output my_videos --resolution 1080p
```

### Command-Line Arguments

- **`url`**: The URL of the YouTube video or playlist.
- **`--output`**: Output directory for saving the downloaded files (default is `downloads`).
- **`--resolution`**: Video resolution (e.g., 720p, 1080p) for video downloads (default is `720p`).
- **`--audio`**: Download audio-only (MP3 format).
- **`--playlist`**: Download all videos in a playlist.

## Example Commands

1. **Download a video in 1080p resolution**:
   ```bash
   python main.py https://www.youtube.com/watch?v=example_video_id --resolution 1080p
   ```

2. **Download audio from a video to a custom folder**:
   ```bash
   python main.py https://www.youtube.com/watch?v=example_video_id --audio --output my_audio_files
   ```

3. **Download an entire playlist in the default resolution**:
   ```bash
   python main.py https://www.youtube.com/playlist?list=example_playlist_id --playlist
   ```

## Project Structure

```
youtube-downloader/
├── downloader/
│   ├── __init__.py
│   ├── video_downloader.py        # Module for downloading videos and audio
├── requirements.txt               # List of dependencies
├── README.md                      # Project documentation
└── main.py                        # CLI for the downloader
```

## Future Enhancements

1. **Graphical User Interface (GUI)**: Add a user-friendly GUI using `tkinter` or `PyQt5`.
2. **Support for Different Formats**: Allow downloading in formats other than MP4 (e.g., AVI, MOV).
3. **Subtitle Download**: Add support for downloading subtitles.
4. **Video Conversion Options**: Provide options to convert downloaded videos to different formats.


##  Running the Tests
1. **To run the unit tests, use the following command**:
    ```bash
    python main.py https://www.youtube.com/playlist?list=example_playlist_id --playlist
    ```



## Contact

For questions or suggestions, feel free to reach out:

- **Email**: [amahmood561@gmail.com](mailto:amahmood561@gmail)
- **GitHub**: [https://github.com/amahmood561](https://github.com/amahmood561)

---

