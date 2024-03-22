import numpy as np
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import cv2
from vidstab import VidStab, layer_blend
import numpy as np
import time

class Worker1(QThread):  # камера
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        displacement = 0  # Начальное смещение курсора
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                height, width, _ = frame.shape
                # Движение курсора вдоль линии
                displacement += 1
                if displacement > 180:
                    displacement = -180
                self.draw_hud(frame, width, height, displacement)
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0],
                                           QImage.Format.Format_RGB888)
                self.ImageUpdate.emit(ConvertToQtFormat)

    def stop(self):
        self.ThreadActive = False
        self.quit()

    def draw_hud(self, frame, width, height, displacement):
        # Отрисовка линейки
        line_color = (0, 255, 0)
        line_thickness = 2
        cv2.line(frame, (width // 2, 15), (width // 2, 0), line_color, line_thickness)

        # Отрисовка подписей на линейке
        step = 30
        for i in range(-180, 180, step):
            x = width // 2 + int((i / 180.0) * (width // 2))
            # Проверка, чтобы метка не выходила за пределы кадра
            if 0 <= x < width:
                cv2.line(frame, (x, 10), (x, 0), line_color, line_thickness)
                cv2.putText(frame, str(i), (x - 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, line_color, 1)

        # Отрисовка конусообразного курсора
        cursor_size = 10
        cursor_color = (0, 0, 255)
        cursor_position = width // 2 + int((displacement / 180.0) * (width // 2))
        cv2.polylines(frame, [np.array([[cursor_position, 15], [cursor_position - cursor_size, cursor_size * 2],
                                        [cursor_position + cursor_size, cursor_size * 2]])], True, cursor_color, 2)