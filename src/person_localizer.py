import cv2
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np

from src.index_to_category import IndexToCategory


class PersonLocalizer:

    def __init__(self, min_score_threshold):
        self.detector = hub.load("https://tfhub.dev/tensorflow/mask_rcnn/inception_resnet_v2_1024x1024/1")
        self.person_index = IndexToCategory().get_index('person')
        self.min_score_threshold = min_score_threshold

    def draw_boxes_on_image(self, image):
        res = self._get_boxes(image)
        idx = tf.where(res['detection_classes'] == self.person_index)

        person_boxes = tf.gather_nd(res['detection_boxes'], idx)
        scores = tf.gather_nd(res['detection_multiclass_scores'], idx)

        y_min = person_boxes[:, 0] * image.shape[0]
        x_min = person_boxes[:, 1] * image.shape[1]
        y_max = person_boxes[:, 2] * image.shape[0]
        x_max = person_boxes[:, 3] * image.shape[1]
        y_min, x_min, y_max, x_max = [np.round(z.numpy()) for z in [y_min, x_min, y_max, x_max]]

        for i in range(len(y_min)):
            if scores[i, 1] > self.min_score_threshold:
                cv2.rectangle(image, (x_min[i], y_min[i]), (x_max[i], y_max[i]), color=[255, 255, 255], thickness=3)

        return image

    def _get_boxes(self, image:np.array):
            image_tf = tf.convert_to_tensor(image, dtype=tf.uint8)
            image_tf = tf.expand_dims(image_tf, 0)
            return self._call_nn(image_tf)

    def _call_nn(self, image_tensor):
        assert image_tensor.shape[0] == 1
        detector_output = self.detector(image_tensor)
        return detector_output







