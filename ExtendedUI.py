import time

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from camera import Worker1
from ui import *
import sys


class ExtendedUI(Ui_MainWindow):
    # Класс-наследник окна, создаваемого qt designer.
    # Использовать для любых изменений класса-родителя.

    # вкладки
    def switchTabInput(self):
        self.info_stackedWidget.setCurrentWidget(self.info_Page)

    def switchTabControls(self):
        self.info_stackedWidget.setCurrentWidget(self.PID_Page)

    def submitCoefs(self):
        self.coefsInput.append(int(self.P_coef_field.text()))
        self.coefsInput.append(int(self.I_coef_field.text()))
        self.coefsInput.append(int(self.D_coef_field.text()))
        self.coefsInput.append(int(self.depth_coef_field.text()))
        self.coefsInput.append(int(self.heading_coef_field.text()))

    # функции для работы с камерой
    def ImageUpdateSlot(self, Image):
        self.camera_feed.setPixmap(QPixmap.fromImage(Image).scaled(self.camera_feed.width(), self.camera_feed.height()))

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
        self.coefsInput = bytearray()
        self.btn_restore.hide()
        self.btn_close.clicked.connect(self.exit)
        self.btn_minimize.clicked.connect(lambda: self.minimizeWindow(MainWindow))
        self.btn_maximize.clicked.connect(lambda: self.maximizeWindow(MainWindow))
        self.btn_restore.clicked.connect(lambda: self.restoreWindow(MainWindow))
        self.button_controlsTab.clicked.connect(lambda: self.switchTabInput())
        self.button_tauTab.clicked.connect(lambda: self.switchTabControls())
        self.buttonSubmitCoefs.clicked.connect(lambda: self.submitCoefs())
        # окно без рамки
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    def updateUI(self, rov_UDP, state=None):
        if state:
            if rov_UDP.isConnectionEstablished:
                self.label_connectionNotDetected.setText("")
            else:
                self.label_connectionNotDetected.setText("Нет аппарата")
            self.label_padNotDetected.setText("")
            if state.Gamepad.wButtons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх
                self.buttonA_perc.setText("0%")
                self.buttonY_perc.setText("100%")
            elif state.Gamepad.wButtons & 0b0001000000000000:  # крестик\A - погрузить робота
                self.buttonY_perc.setText("0%")
                self.buttonA_perc.setText("100%")
            else:
                self.buttonY_perc.setText("0%")
                self.buttonA_perc.setText("0%")

            if state.Gamepad.wButtons & 0b100000000000000:  # квадрат\Х - открыть манипулятор
                self.buttonB_perc.setText("0%")
                time.sleep(0.005)
                self.buttonX_perc.setText("100%")
            elif state.Gamepad.wButtons & 0b10000000000000:  # круг\В - закрыть манипулятор
                self.buttonX_perc.setText("0%")
                time.sleep(0.005)
                self.buttonB_perc.setText("100%")
            else:
                self.buttonX_perc.setText("0%")
                self.buttonB_perc.setText("0%")

            if state.Gamepad.wButtons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси по часовой стрелке
                self.buttonRB_perc.setText("100%")
            else:
                self.buttonRB_perc.setText("0%")

            if state.Gamepad.wButtons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси против часовой стрелки
                self.buttonLB_perc.setText("100%")
            else:
                self.buttonLB_perc.setText("0%")

            self.buttonLT_perc.setText(str(int((state.Gamepad.bLeftTrigger / 255) * 100)) + "%")
            self.buttonRT_perc.setText(str(int((state.Gamepad.bRightTrigger / 255) * 100)) + "%")

            time.sleep(0.02)
            self.thrus_vert_0_perc.setText(str(rov_UDP.toWrite[0]))
            self.thrus_vert_1_perc.setText(str(rov_UDP.toWrite[1]))
            time.sleep(0.001)
            self.thrus_horiz_0_perc.setText(str(rov_UDP.toWrite[2]))
            time.sleep(0.001)
            self.thrus_horiz_1_perc.setText(str(rov_UDP.toWrite[3]))
            time.sleep(0.001)
            self.thrus_horiz_2_perc.setText(str(rov_UDP.toWrite[4]))
            time.sleep(0.001)
            self.thrus_horiz_3_perc.setText(str(rov_UDP.toWrite[5]))
            time.sleep(0.001)
            self.manip_rotation_perc.setText(str(rov_UDP.toWrite[6]))
            time.sleep(0.001)
            self.manip_grabber_perc.setText(str(rov_UDP.toWrite[7]))
            time.sleep(0.001)
            # приём
            self.pitch_digit.setText(str(rov_UDP.receivedPacket[0]))
            time.sleep(0.001)
            self.yaw_digit.setText(str(rov_UDP.receivedPacket[1]))
            time.sleep(0.001)
            self.roll_digit.setText(str(rov_UDP.receivedPacket[2]))
            time.sleep(0.001)
            # TODO - добавить еще поля телеметрии
            '''
            self.packet_depth.setText(str(rov_UDP.receivedPacket[3]))
            time.sleep(0.001)
            self.packet_emp1.setText(str(rov_UDP.receivedPacket[4]))
            time.sleep(0.001)
            self.packet_emp2.setText(str(rov_UDP.receivedPacket[5]))
            time.sleep(0.001)
            '''
        else:
            time.sleep(0.02)
            self.thrus_vert_0_perc.setText(str(rov_UDP.toWrite[0]))
            self.thrus_vert_1_perc.setText(str(rov_UDP.toWrite[1]))
            time.sleep(0.001)
            self.thrus_horiz_0_perc.setText(str(rov_UDP.toWrite[2]))
            time.sleep(0.001)
            self.thrus_horiz_1_perc.setText(str(rov_UDP.toWrite[3]))
            time.sleep(0.001)
            self.thrus_horiz_2_perc.setText(str(rov_UDP.toWrite[4]))
            time.sleep(0.001)
            self.thrus_horiz_3_perc.setText(str(rov_UDP.toWrite[5]))
            time.sleep(0.001)
            self.manip_rotation_perc.setText(str(rov_UDP.toWrite[6]))
            time.sleep(0.001)
            self.manip_grabber_perc.setText(str(rov_UDP.toWrite[7]))
            time.sleep(0.001)
            # приём
            self.pitch_digit.setText(str(rov_UDP.receivedPacket[0]))
            time.sleep(0.001)
            self.yaw_digit.setText(str(rov_UDP.receivedPacket[1]))
            time.sleep(0.001)
            self.roll_digit.setText(str(rov_UDP.receivedPacket[2]))
            time.sleep(0.001)
            # TODO - добавить еще поля телеметрии
            '''
            self.packet_depth.setText(str(rov_UDP.receivedPacket[3]))
            time.sleep(0.001)
            self.packet_emp1.setText(str(rov_UDP.receivedPacket[4]))
            time.sleep(0.001)
            self.packet_emp2.setText(str(rov_UDP.receivedPacket[5]))
            time.sleep(0.001)
            '''
