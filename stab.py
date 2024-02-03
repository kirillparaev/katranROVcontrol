from PyQt6.QtCore import *
from PyQt6.QtGui import *
import numpy as np
import cv2


class Worker1(QThread):  # камера
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.history = 10
        self.max_points = 10
        self.old_points = np.empty((0, 1, 2), dtype=np.float32)
        self.old_gray = None


    ImageUpdate = pyqtSignal(QImage)

    @staticmethod
    def movingAverage(curve, radius):
        window_size = 2 * radius + 1
        # Определение фильтра
        f = np.ones(window_size) / window_size
        # Добавление отступов к границам
        curve_pad = np.lib.pad(curve, (radius, radius), 'edge')
        # Применение свертки
        curve_smoothed = np.convolve(curve_pad, f, mode='same')
        return curve_smoothed


    def run(self):
        self.ThreadActive = True
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while self.ThreadActive:
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if self.old_gray is None:
                    self.old_gray = gray
                    self.old_points = cv2.goodFeaturesToTrack(self.old_gray, self.max_points, 0.01, 10)
                    continue

                new_points, status, error = cv2.calcOpticalFlowPyrLK(self.old_gray, gray, self.old_points, None)

                good_new = new_points[status == 1]
                good_old = self.old_points[status == 1]

                dx = np.mean(good_new[:, 0, 0] - good_old[:, 0, 0])
                dy = np.mean(good_new[:, 0, 1] - good_old[:, 0, 1])

                self.old_points = good_new.reshape(-1, 1, 2)
                self.old_gray = gray

                FlippedImage = cv2.flip(self.old_gray, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                           QImage.Format.Format_RGB888)
                # image scales here
                Pic = ConvertToQtFormat.scaled(1920, 1080, Qt.AspectRatioMode.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()