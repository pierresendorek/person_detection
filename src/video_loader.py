import cv2
from glob import glob

class VideoLoader:
    def __init__(self, video_mp4_path:str):
        self.video_mp4_path = video_mp4_path
        self.cap = cv2.VideoCapture(self.video_mp4_path)
        if (self.cap.isOpened() == False):
            raise Exception("Error opening video stream or file")

    def get_frame_generator(self):
        # Check if camera opened successfully

        # Read until video is completed
        while (self.cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if ret == True:

                yield(frame)
            else:
                break

        # When everything done, release the video capture object
        self.cap.release()

    def get_frames_per_second(self):
        return self.cap.get(cv2.CAP_PROP_FPS)



if __name__ == "__main__":
    data_loader = VideoLoader("/home/pierresendorek/projets/job/aive/data/MISS DIOR – The new Eau de Parfum.mp4")
    frames = data_loader.get_frame_generator()
    print(data_loader.get_frames_per_second())
    #for i, frame in enumerate(frames):
    #    print(i, frame.shape)

