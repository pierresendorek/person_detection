from src.person_localizer import PersonLocalizer
from src.video_loader import VideoLoader
from src.video_writer import VideoWriter


class VideoProcessingPipeline:
    def __init__(self):
        self.person_localizer = PersonLocalizer(min_score_threshold=0.5)

    def process(self,
                input_file:str,
                output_folder:str):

        video_loader = VideoLoader(input_file)
        frames_per_second = video_loader.get_frames_per_second()
        video_writer = VideoWriter(output_folder=output_folder,
                                   filename=input_file.split("/")[-1],
                                   frames_per_second=frames_per_second)

        frames = video_loader.get_frame_generator()
        processed_frames = (self.person_localizer.draw_boxes_on_image(frame) for frame in frames)
        video_writer.write_video(frame_generator=processed_frames)


if __name__ == "__main__":
    input_path = "/home/pierresendorek/projets/job/aive/data/MISS DIOR – The new Eau de Parfum.mp4"
    output_path = "/home/pierresendorek/projets/job/aive/data/out.mp4"




