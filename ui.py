import time
from PyQt6 import QtCore, QtWidgets, QtGui
import xinput
import UDP
from threading import Thread


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 465)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelButtonsPressed = QtWidgets.QLabel(self.centralwidget)
        self.labelButtonsPressed.setGeometry(QtCore.QRect(30, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.labelButtonsPressed.setFont(font)
        self.labelButtonsPressed.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelButtonsPressed.setScaledContents(False)
        self.labelButtonsPressed.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelButtonsPressed.setWordWrap(True)
        self.labelButtonsPressed.setObjectName("labelButtonsPressed")
        self.labelSendingPacket = QtWidgets.QLabel(self.centralwidget)
        self.labelSendingPacket.setGeometry(QtCore.QRect(20, 170, 581, 101))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.labelSendingPacket.setFont(font)
        self.labelSendingPacket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelSendingPacket.setObjectName("labelSendingPacket")
        self.checkBox_Y_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Y_btn.setEnabled(False)
        self.checkBox_Y_btn.setGeometry(QtCore.QRect(270, 40, 81, 20))
        self.checkBox_Y_btn.setObjectName("checkBox_Y_btn")
        self.checkBox_A_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_A_btn.setEnabled(False)
        self.checkBox_A_btn.setGeometry(QtCore.QRect(370, 40, 75, 20))
        self.checkBox_A_btn.setObjectName("checkBox_A_btn")
        self.checkBox_LB_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_LB_btn.setEnabled(False)
        self.checkBox_LB_btn.setGeometry(QtCore.QRect(460, 40, 75, 20))
        self.checkBox_LB_btn.setObjectName("checkBox_LB_btn")
        self.checkBox_RB_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_RB_btn.setEnabled(False)
        self.checkBox_RB_btn.setGeometry(QtCore.QRect(560, 40, 75, 20))
        self.checkBox_RB_btn.setObjectName("checkBox_RB_btn")
        self.packet_1st_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_1st_byte.setGeometry(QtCore.QRect(310, 180, 21, 16))
        self.packet_1st_byte.setObjectName("packet_1st_byte")
        self.packet_2nd_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_2nd_byte.setGeometry(QtCore.QRect(330, 180, 21, 16))
        self.packet_2nd_byte.setObjectName("packet_2nd_byte")
        self.packet_3rd_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_3rd_byte.setGeometry(QtCore.QRect(350, 180, 21, 16))
        self.packet_3rd_byte.setObjectName("packet_3rd_byte")
        self.packet_4th_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_4th_byte.setGeometry(QtCore.QRect(370, 180, 21, 16))
        self.packet_4th_byte.setObjectName("packet_4th_byte")
        self.packet_5th_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_5th_byte.setGeometry(QtCore.QRect(390, 180, 21, 16))
        self.packet_5th_byte.setObjectName("packet_5th_byte")
        self.packet_6th_byte = QtWidgets.QLabel(self.centralwidget)
        self.packet_6th_byte.setGeometry(QtCore.QRect(410, 180, 21, 16))
        self.packet_6th_byte.setObjectName("packet_6th_byte")
        self.verticalSlider_LT = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_LT.setEnabled(False)
        self.verticalSlider_LT.setGeometry(QtCore.QRect(500, 100, 18, 160))
        self.verticalSlider_LT.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_LT.setObjectName("verticalSlider_LT")
        self.verticalSlider_RT = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_RT.setEnabled(False)
        self.verticalSlider_RT.setGeometry(QtCore.QRect(620, 100, 18, 160))
        self.verticalSlider_RT.setMaximum(255)
        self.verticalSlider_RT.setProperty("value", 0)
        self.verticalSlider_RT.setSliderPosition(0)
        self.verticalSlider_RT.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_RT.setObjectName("verticalSlider_RT")
        self.label_LT_L2 = QtWidgets.QLabel(self.centralwidget)
        self.label_LT_L2.setGeometry(QtCore.QRect(490, 280, 49, 16))
        self.label_LT_L2.setObjectName("label_LT_L2")
        self.label_RT_R2 = QtWidgets.QLabel(self.centralwidget)
        self.label_RT_R2.setGeometry(QtCore.QRect(610, 280, 49, 16))
        self.label_RT_R2.setObjectName("label_RT_R2")
        self.label_padNotDetected = QtWidgets.QLabel(self.centralwidget)
        self.label_padNotDetected.setEnabled(True)
        self.label_padNotDetected.setGeometry(QtCore.QRect(10, 380, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.label_padNotDetected.setFont(font)
        self.label_padNotDetected.setObjectName("label_padNotDetected")
        self.labelCalibrating = QtWidgets.QLabel(self.centralwidget)
        self.labelCalibrating.setGeometry(QtCore.QRect(430, 180, 49, 16))
        self.labelCalibrating.setObjectName("labelCalibrating")
        self.checkBoxCalibrationMode = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxCalibrationMode.setGeometry(QtCore.QRect(560, 390, 161, 20))
        self.checkBoxCalibrationMode.setObjectName("checkBoxCalibrationMode")
        self.checkBox_X_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_X_btn.setEnabled(False)
        self.checkBox_X_btn.setGeometry(QtCore.QRect(270, 80, 75, 20))
        self.checkBox_X_btn.setObjectName("checkBox_X_btn")
        self.checkBox_B_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_B_btn.setEnabled(False)
        self.checkBox_B_btn.setGeometry(QtCore.QRect(370, 80, 75, 20))
        self.checkBox_B_btn.setObjectName("checkBox_B_btn")
        self.label_ServoPacket = QtWidgets.QLabel(self.centralwidget)
        self.label_ServoPacket.setGeometry(QtCore.QRect(450, 180, 21, 16))
        self.label_ServoPacket.setObjectName("label_ServoPacket")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KATRAN ROV Demo"))
        self.labelButtonsPressed.setText(_translate("MainWindow", "Нажатые кнопки: "))
        self.labelSendingPacket.setText(_translate("MainWindow", "Отправляемый пакет: "))
        self.checkBox_Y_btn.setText(_translate("MainWindow", "Y / Triangle"))
        self.checkBox_A_btn.setText(_translate("MainWindow", "A / Cross"))
        self.checkBox_LB_btn.setText(_translate("MainWindow", "LB / L1"))
        self.checkBox_RB_btn.setText(_translate("MainWindow", "RB / R1"))
        self.packet_1st_byte.setText(_translate("MainWindow", "5A"))
        self.packet_2nd_byte.setText(_translate("MainWindow", "5A"))
        self.packet_3rd_byte.setText(_translate("MainWindow", "5A"))
        self.packet_4th_byte.setText(_translate("MainWindow", "5A"))
        self.packet_5th_byte.setText(_translate("MainWindow", "5A"))
        self.packet_6th_byte.setText(_translate("MainWindow", "5A"))
        self.label_LT_L2.setText(_translate("MainWindow", "LT / L2"))
        self.label_RT_R2.setText(_translate("MainWindow", "RT / R2"))
        self.label_padNotDetected.setText(_translate("MainWindow", "!!! Геймпад не обнаружен !!!"))
        self.labelCalibrating.setText(_translate("MainWindow", "00"))
        self.checkBoxCalibrationMode.setText(_translate("MainWindow", "Калибровка гироскопа"))
        self.checkBox_X_btn.setText(_translate("MainWindow", "X / Square"))
        self.checkBox_B_btn.setText(_translate("MainWindow", "B / Circle"))
        self.label_ServoPacket.setText(_translate("MainWindow", "00"))

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

            self.verticalSlider_RT.setSliderPosition(state.gamepad.right_trigger)
            self.verticalSlider_LT.setSliderPosition(state.gamepad.left_trigger)

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
        ui.updateUI(state)
        if state:
            rov_UDP.formPacket(state)
            rov_UDP.appendDebugInfo(ui)
            rov_UDP.sendPacket()
            ui.debug_updatePacketUI()
            rov_UDP.clearPacket()
        elif state is None:
            ui.label_padNotDetected.setText("!!! Геймпад не обнаружен !!!")
            while state is None:
                state = pad.get_state()
                # нужно прописать отдельный случай для отправки служебной информации
                rov_UDP.appendDebugInfo(ui)
                rov_UDP.sendPacket()
                ui.debug_updatePacketUI()
                rov_UDP.clearPacket()


if __name__ == "__main__":
    import sys

    pad = xinput.XInputJoystick(0)
    # прикрутить ввод ip адреса и порта
    rov_UDP = UDP.UDPConnection("192.168.0.177", 8080)
    # rov_UDP = UDP.UDPConnection("127.0.0.1", 127) # for debugging purposes

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    inputStream = Thread(target=inputHandling, args=(), daemon=True)
    inputStream.start()

    sys.exit(app.exec())
