import socket


class UDPConnection:
    def __init__(self, remoteIP, remotePort):
        self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddressPort = (remoteIP, remotePort)
        self.bufferSize = 1024
        self.hasSentFirstPacket = False
        self.isInDebugMode = False

        self.th_vertical_0 = 0x5B  # 1st byte
        self.th_vertical_1 = 0x5B  # 2nd byte
        self.th_horizontal_0 = 0x5B  # 3
        self.th_horizontal_1 = 0x5B  # 4
        self.th_horizontal_2 = 0x5B  # 5
        self.th_horizontal_3 = 0x5B  # 6
        self.isCalibrationNeeded = 0x00  # 7
        self.servoManipulator_0 = 127  # 8
        self.servoManipulator_1 = 127  # 9

        self.msgFrom = bytearray()
        self.prevPacket = self.msgFrom

    def sendPacket(self):
        self.msgFrom.append(self.th_vertical_0)
        self.msgFrom.append(self.th_vertical_1)
        self.msgFrom.append(self.th_horizontal_0)
        self.msgFrom.append(self.th_horizontal_1)
        self.msgFrom.append(self.th_horizontal_2)
        self.msgFrom.append(self.th_horizontal_3)
        self.msgFrom.append(self.servoManipulator_0)
        self.msgFrom.append(self.servoManipulator_1)

        self.msgFrom.append(self.isCalibrationNeeded)
        if not self.hasSentFirstPacket:
            self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
            self.hasSentFirstPacket = True
        elif self.msgFrom == self.prevPacket:
            return
        else:
            for i in range(1):  # прикрутить настройку потока посылаемых пакетов
                self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
        self.prevPacket = self.msgFrom

    def clearPacket(self):
        self.msgFrom = bytearray()
        self.th_vertical_0 = 0x5B
        self.th_vertical_1 = 0x5B
        self.th_horizontal_0 = 0x5B
        self.th_horizontal_1 = 0x5B
        self.th_horizontal_2 = 0x5B
        self.th_horizontal_3 = 0x5B
        self.isCalibrationNeeded = 0x00

    def formPacket(self, state):
        if state.gamepad.buttons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх (приоритет)
            self.th_vertical_0 = 0x7F
            self.th_vertical_1 = 0x7F
        elif state.gamepad.buttons & 0b0001000000000000:  # крестик\A - погрузить робота
            self.th_vertical_0 = 0x19
            self.th_vertical_1 = 0x19
        else:
            self.th_vertical_0 = 0x5B
            self.th_vertical_1 = 0x5B

        if state.gamepad.buttons & 0b100000000000000:  # квадрат\Х - открыть манипулятор
            if self.servoManipulator_0 != 255 and self.servoManipulator_1 != 255:
                if self.servoManipulator_0 + 1 > 255 and self.servoManipulator_1 + 1 > 255:
                    self.servoManipulator_0 = 255
                    self.servoManipulator_1 = 255
                else:
                    self.servoManipulator_0 = self.servoManipulator_0 + 1
                    self.servoManipulator_1 = self.servoManipulator_1 + 1
        elif state.gamepad.buttons & 0b10000000000000:  # круг\В - закрыть манипулятор
            if self.servoManipulator_0 != 0 and self.servoManipulator_1 != 0:
                if self.servoManipulator_0 - 1 < 0 and self.servoManipulator_1 - 1 < 0:
                    self.servoManipulator_0 = 0
                    self.servoManipulator_1 = 0
                else:
                    self.servoManipulator_0 = self.servoManipulator_0 - 1
                    self.servoManipulator_1 = self.servoManipulator_1 - 1
        else:
            self.servoManipulator_0 = self.servoManipulator_0
            self.servoManipulator_1 = self.servoManipulator_1
        '''
        if state.gamepad.buttons & 0b100000000000000:  # квадрат\Х - открыть манипулятор
            if (self.servoManipulator_0 + 5) > 255:
                self.servoManipulator_0 = 255
            else:
                self.servoManipulator_0 = self.servoManipulator_0 + 5
        elif state.gamepad.buttons & 0b10000000000000:  # круг\В - закрыть манипулятор
            if (self.servoManipulator_0 - 5) < 0:
                self.servoManipulator_0 = 0
            else:
                self.servoManipulator_0 = self.servoManipulator_0 - 5
        else:
            self.servoManipulator_0 = self.servoManipulator_0
        '''

        if state.gamepad.buttons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси направо
            self.th_horizontal_0 = 0x7F  # вращение боковых движителей в этом и следующем if
            self.th_horizontal_1 = 0x7F
        else:
            self.th_horizontal_0 = 0x5B
            self.th_horizontal_1 = 0x5B

        if state.gamepad.buttons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси налево
            self.th_horizontal_2 = 0x7F
            self.th_horizontal_3 = 0x7F
        else:
            self.th_horizontal_2 = 0x5B
            self.th_horizontal_3 = 0x5B

        # курки не будут работать вместе с плечиками
        if state.gamepad.right_trigger and (state.gamepad.buttons & 0b0000000100000000 == 0) and (
                state.gamepad.buttons & 0b0000001000000000 == 0):
            right_trigger = int((state.gamepad.right_trigger / 255) * 24) # default - 50; for 1 eng = 25
            self.th_horizontal_0 = (self.th_horizontal_0 + right_trigger)
            self.th_horizontal_1 = (self.th_horizontal_1 + right_trigger)
            self.th_horizontal_2 = (self.th_horizontal_2 + right_trigger)
            self.th_horizontal_3 = (self.th_horizontal_3 + right_trigger)

        if state.gamepad.left_trigger and (state.gamepad.buttons & 0b0000000100000000 == 0) and (
                state.gamepad.buttons & 0b0000001000000000 == 0):
            left_trigger = int((state.gamepad.left_trigger / 255) * 24)
            self.th_horizontal_0 = (self.th_horizontal_0 - left_trigger)
            self.th_horizontal_1 = (self.th_horizontal_1 - left_trigger)
            self.th_horizontal_2 = (self.th_horizontal_2 - left_trigger)
            self.th_horizontal_3 = (self.th_horizontal_3 - left_trigger)

    def appendDebugInfo(self, UI):
        # gyro calibration
        if UI.checkBoxCalibrationMode.isChecked():
            self.isCalibrationNeeded = 0xFF
