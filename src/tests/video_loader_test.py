import unittest

from src.video_loader import VideoLoader


class TestVideoLoader(unittest.TestCase):
    def test_exception_if_load_failed(self):
        # Given : nothing
        # When
        with self.assertRaises(Exception) as context:
            VideoLoader("")
        # Then
        self.assertTrue("Error opening video stream or file" in str(context.exception))



