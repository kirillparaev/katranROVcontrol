import xinput
import UDP
from threading import Thread
from ui import *
import time
from PyQt6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon, QKeySequence, QPixmap
import resources_rc

class ExtendedUI(Ui_MainWindow):
    # Класс-наследник окна, создаваемого qt designer.
    # Использовать для любых изменений класса-родителя.
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # окно без рамки
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


    def updateUI(self, state):
        if state:
            self.label_padNotDetected.setText("")

            if state.gamepad.buttons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            elif state.gamepad.buttons & 0b0001000000000000:  # крестик\A - погрузить робота
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.gamepad.buttons & 0b100000000000000:  # квадрат\Х - открыть манипулятор
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                time.sleep(0.005)
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            elif state.gamepad.buttons & 0b10000000000000:  # круг\В - закрыть манипулятор
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                time.sleep(0.005)
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.gamepad.buttons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси по часовой стрелке
                self.checkBox_RB_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_RB_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.gamepad.buttons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси против часовой стрелки
                self.checkBox_LB_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_LB_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            self.horizontalSlider_RT.setSliderPosition(state.gamepad.right_trigger)
            self.horizontalSlider_LT.setSliderPosition(state.gamepad.left_trigger)

    def debug_updatePacketUI(self):
        time.sleep(0.02)  # задержка 20 мс
        self.packet_1st_byte.setText(str(rov_UDP.th_vertical_0))
        self.packet_2nd_byte.setText(str(rov_UDP.th_vertical_1))
        time.sleep(0.001)
        self.packet_3rd_byte.setText(str(rov_UDP.th_horizontal_0))
        time.sleep(0.001)
        self.packet_4th_byte.setText(str(rov_UDP.th_horizontal_1))
        time.sleep(0.001)
        self.packet_5th_byte.setText(str(rov_UDP.th_horizontal_2))
        time.sleep(0.001)
        self.packet_6th_byte.setText(str(rov_UDP.th_horizontal_3))
        time.sleep(0.001)
        self.labelCalibrating.setText(str(rov_UDP.isCalibrationNeeded))
        time.sleep(0.001)
        self.label_ServoPacket.setText(str(rov_UDP.servoManipulator))


def inputHandling():
    while True:
        state = pad.get_state()
        window.updateUI(state)
        if state:
            rov_UDP.formPacket(state)
            rov_UDP.appendDebugInfo(window)
            rov_UDP.sendPacket()
            window.debug_updatePacketUI()
            rov_UDP.clearPacket()
        elif state is None:
            window.label_padNotDetected.setText("!!! Геймпад не обнаружен !!!")
            while state is None:
                state = pad.get_state()
                # нужно прописать отдельный случай для отправки служебной информации
                rov_UDP.appendDebugInfo(window)
                rov_UDP.sendPacket()
                window.debug_updatePacketUI()
                rov_UDP.clearPacket()


if __name__ == "__main__":
    import sys

    pad = xinput.XInputJoystick(0)
    # прикрутить ввод ip адреса и порта
    rov_UDP = UDP.UDPConnection("192.168.0.177", 8080)
    # rov_UDP = UDP.UDPConnection("127.0.0.1", 127) # for debugging purposes

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    window = ExtendedUI()
    window.setupUi(mainWindow)
    mainWindow.show()

    inputStream = Thread(target=inputHandling, args=(), daemon=True)
    inputStream.start()

    sys.exit(app.exec())
