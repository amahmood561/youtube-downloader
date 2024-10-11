# test_video_downloader.py
import unittest
from unittest.mock import patch, MagicMock
import os
from downloader.video_downloader import download_video, download_audio, download_playlist

class TestVideoDownloader(unittest.TestCase):
    def setUp(self):
        # Setup the output directory for tests
        self.output_dir = 'test_downloads'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        # Clean up by removing the test output directory and its contents
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

    @patch('downloader.video_downloader.YouTube')
    def test_download_video(self, MockYouTube):
        # Mock YouTube object and streams
        mock_yt = MockYouTube.return_value
        mock_stream = MagicMock()
        mock_stream.download.return_value = None
        mock_yt.streams.filter.return_value.first.return_value = mock_stream

        # Call the download_video function
        download_video('http://fakeurl.com/video', output_dir=self.output_dir, resolution='720p')

        # Assertions
        mock_yt.streams.filter.assert_called_with(res='720p', file_extension='mp4')
        mock_stream.download.assert_called_with(output_path=self.output_dir)
        print("test_download_video passed.")

    @patch('downloader.video_downloader.YouTube')
    @patch('downloader.video_downloader.ffmpeg')
    def test_download_audio(self, MockFFmpeg, MockYouTube):
        # Mock YouTube object and audio stream
        mock_yt = MockYouTube.return_value
        mock_stream = MagicMock()
        mock_stream.download.return_value = 'test_audio_file'
        mock_yt.streams.filter.return_value.first.return_value = mock_stream

        # Mock ffmpeg behavior
        mock_input = MockFFmpeg.input.return_value
        mock_output = mock_input.output.return_value
        mock_output.run.return_value = None

        # Call the download_audio function
        download_audio('http://fakeurl.com/video', output_dir=self.output_dir)

        # Assertions
        mock_yt.streams.filter.assert_called_with(only_audio=True)
        mock_stream.download.assert_called_with(output_path=self.output_dir)
        MockFFmpeg.input.assert_called_with('test_audio_file')
        MockFFmpeg.input().output().run.assert_called_with(overwrite_output=True)
        print("test_download_audio passed.")

    @patch('downloader.video_downloader.Playlist')
    @patch('downloader.video_downloader.download_video')
    def test_download_playlist(self, MockDownloadVideo, MockPlaylist):
        # Mock Playlist object
        mock_playlist = MockPlaylist.return_value
        mock_playlist.video_urls = ['http://fakeurl.com/video1', 'http://fakeurl.com/video2']

        # Call the download_playlist function
        download_playlist('http://fakeurl.com/playlist', output_dir=self.output_dir, resolution='720p')

        # Assertions
        MockPlaylist.assert_called_with('http://fakeurl.com/playlist')
        self.assertEqual(MockDownloadVideo.call_count, 2)
        MockDownloadVideo.assert_any_call('http://fakeurl.com/video1', self.output_dir, '720p')
        MockDownloadVideo.assert_any_call('http://fakeurl.com/video2', self.output_dir, '720p')
        print("test_download_playlist passed.")

if __name__ == '__main__':
    unittest.main()
