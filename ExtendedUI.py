import time
from PyQt6.QtGui import QPixmap
from PySide6.QtCore import Qt

from camera import Worker1
from ui import *
import sys


class ExtendedUI(Ui_MainWindow):
    # Класс-наследник окна, создаваемого qt designer.
    # Использовать для любых изменений класса-родителя.

    # переключалки вкладок
    def SwitchTabCamera(self):
        self.dashboard.setCurrentIndex(0)

    def SwitchTabDebug(self):
        self.dashboard.setCurrentIndex(1)

    # функции для работы с камерой
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

    def exit(self):
        sys.exit(0)

    def minimizeWindow(self, MainWindow):
        MainWindow.showMinimized()

    def maximizeWindow(self, MainWindow):
        MainWindow.showMaximized()
        self.btn_maximize.hide()
        self.btn_restore.show()

    def restoreWindow(self, MainWindow):
        MainWindow.showNormal()
        self.btn_restore.hide()
        self.btn_maximize.show()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btn_restore.hide()
        self.btnCameraTab.clicked.connect(self.SwitchTabCamera)
        self.btnDebugTab.clicked.connect(self.SwitchTabDebug)
        self.btn_close.clicked.connect(self.exit)
        self.btn_minimize.clicked.connect(lambda: self.minimizeWindow(MainWindow))
        self.btn_maximize.clicked.connect(lambda: self.maximizeWindow(MainWindow))
        self.btn_restore.clicked.connect(lambda: self.restoreWindow(MainWindow))
        # окно без рамки
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    def updateUI(self, state):
        if state:
            self.label_padNotDetected.setText("")

            if state.Gamepad.wButtons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            elif state.Gamepad.wButtons & 0b0001000000000000:  # крестик\A - погрузить робота
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_Y_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_A_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.Gamepad.wButtons & 0b100000000000000:  # квадрат\Х - открыть манипулятор
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                time.sleep(0.005)
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            elif state.Gamepad.wButtons & 0b10000000000000:  # круг\В - закрыть манипулятор
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                time.sleep(0.005)
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_X_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)
                self.checkBox_B_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.Gamepad.wButtons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси по часовой стрелке
                self.checkBox_RB_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_RB_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            if state.Gamepad.wButtons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси против часовой стрелки
                self.checkBox_LB_btn.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                self.checkBox_LB_btn.setCheckState(QtCore.Qt.CheckState.Unchecked)

            self.horizontalSlider_RT.setSliderPosition(state.Gamepad.bRightTrigger)
            self.horizontalSlider_LT.setSliderPosition(state.Gamepad.bLeftTrigger)

    def debug_updatePacketUI(self, rov_UDP):
        if rov_UDP.isConnectionEstablished:
            self.label_connectionNotDetected.setText("")
        else:
            self.label_connectionNotDetected.setText("Нет соединения с аппаратом")
        time.sleep(0.02)  # задержка 20 мс
        self.packet_1st_byte.setText(str(rov_UDP.toWrite[0]))
        self.packet_2nd_byte.setText(str(rov_UDP.toWrite[1]))
        time.sleep(0.001)
        self.packet_3rd_byte.setText(str(rov_UDP.toWrite[2]))
        time.sleep(0.001)
        self.packet_4th_byte.setText(str(rov_UDP.toWrite[3]))
        time.sleep(0.001)
        self.packet_5th_byte.setText(str(rov_UDP.toWrite[4]))
        time.sleep(0.001)
        self.packet_6th_byte.setText(str(rov_UDP.toWrite[5]))
        time.sleep(0.001)
        self.label_Servo1Packet.setText(str(rov_UDP.toWrite[6]))
        time.sleep(0.001)
        self.label_Servo2Packet.setText(str(rov_UDP.toWrite[7]))
        time.sleep(0.001)
        # приём
        self.packet_x.setText(str(rov_UDP.receivedPacket[0]))
        time.sleep(0.001)
        self.packet_y.setText(str(rov_UDP.receivedPacket[1]))
        time.sleep(0.001)
        self.packet_z.setText(str(rov_UDP.receivedPacket[2]))
        time.sleep(0.001)
        self.packet_depth.setText(str(rov_UDP.receivedPacket[3]))
        time.sleep(0.001)
        self.packet_emp1.setText(str(rov_UDP.receivedPacket[4]))
        time.sleep(0.001)
        self.packet_emp2.setText(str(rov_UDP.receivedPacket[5]))
        time.sleep(0.001)


