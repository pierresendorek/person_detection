import argparse

# For help :
# python main.py -h

from src.pipeline import VideoProcessingPipeline

parser = argparse.ArgumentParser(description='Draw a rectangle around people in a video.')
parser.add_argument('--input-file', metavar='N', type=str, required=True,
                    help='input mp4 file')
parser.add_argument('--output-folder', metavar='N', type=str, required=True,
                    help='output folder where the mp4 and the frames will be written')

args = parser.parse_args()

video_processing_pipeline = VideoProcessingPipeline()
video_processing_pipeline.process(**vars(args))

