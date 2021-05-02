import cv2
from typing import Generator
from os.path import join, exists
from os import makedirs


class VideoWriter:
    def __init__(self,
                 output_folder:str,
                 filename:str,
                 frames_per_second:float):
        self.output_folder = output_folder
        self.filename = filename
        self.first_frame = True
        self.video_writer = None
        self.frames_per_second = frames_per_second


    def write_video(self, frame_generator:Generator):
        frames_folder = self._check_and_create_folders()
        for index_frame, frame in enumerate(frame_generator):

            if self.first_frame == True:
                self.video_writer = cv2.VideoWriter(join(self.output_folder, self.filename), cv2.VideoWriter_fourcc(*'MP4V'),
                                                    self.frames_per_second,
                                                    (frame.shape[1], frame.shape[0]))
                self.first_frame = False

            self.video_writer.write(frame)

            cv2.imwrite(join(frames_folder, f"{index_frame}.jpg"), frame)

        # When everything done, release the video write objects
        self.video_writer.release()

    def _check_and_create_folders(self):
        if not exists(self.output_folder):
            raise FileNotFoundError
        frames_folder = join(self.output_folder, "frames")
        if not exists(frames_folder):
            makedirs(frames_folder)
        return frames_folder

