import socket


class UDPConnection:
    def __init__(self, remoteIP, remotePort):
        self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddressPort = (remoteIP, remotePort)
        self.bufferSize = 1024
        self.th_vertical_0 = 0x5A  # 90
        self.th_vertical_1 = 0x5A
        self.th_horizontal_0 = 0x5A
        self.th_horizontal_1 = 0x5A
        self.th_horizontal_2 = 0x5A
        self.th_horizontal_3 = 0x5A
        self.isCalibrationNeeded = 0x00
        self.msgFrom = bytearray()
        self.hasSentFirstPacket = False
        self.prevPacket = self.msgFrom

    def sendPacket(self):
        self.msgFrom.append(self.th_vertical_0)
        self.msgFrom.append(self.th_vertical_1)
        self.msgFrom.append(self.th_horizontal_0)
        self.msgFrom.append(self.th_horizontal_1)
        self.msgFrom.append(self.th_horizontal_2)
        self.msgFrom.append(self.th_horizontal_3)
        self.msgFrom.append(self.isCalibrationNeeded)
        if not self.hasSentFirstPacket:
            self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
            self.hasSentFirstPacket = True
        if self.msgFrom == self.prevPacket:
            return
        else:
            for i in range(5):
                self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
        self.prevPacket = self.msgFrom

    def clearPacket(self):
        self.msgFrom = bytearray()
        self.th_vertical_0 = 0x5A
        self.th_vertical_1 = 0x5A
        self.th_horizontal_0 = 0x5A
        self.th_horizontal_1 = 0x5A
        self.th_horizontal_2 = 0x5A
        self.th_horizontal_3 = 0x5A
        self.isCalibrationNeeded = 0x00

    def formPacket(self, state):
        if state.gamepad.buttons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх (приоритет)
            self.th_vertical_0 = 0xB4
            self.th_vertical_1 = 0xB4
        elif state.gamepad.buttons & 0b0001000000000000:  # крестик\A - погрузить робота
            self.th_vertical_0 = 0
            self.th_vertical_1 = 0
        else:
            self.th_vertical_0 = 0x5A
            self.th_vertical_1 = 0x5A

        if state.gamepad.buttons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси направо
            self.th_horizontal_0 = 0xB4  # вращение боковых движителей в этом и следующем if
            self.th_horizontal_1 = 0xB4
        else:
            self.th_horizontal_0 = 0x5A
            self.th_horizontal_1 = 0x5A

        if state.gamepad.buttons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси налево
            self.th_horizontal_2 = 0xB4
            self.th_horizontal_3 = 0xB4
        else:
            self.th_horizontal_2 = 0x5A
            self.th_horizontal_3 = 0x5A

        # курки не будут работать вместе с плечиками
        if state.gamepad.right_trigger and (state.gamepad.buttons & 0b0000000100000000 == 0) and (
                state.gamepad.buttons & 0b0000001000000000 == 0):
            right_trigger = int((state.gamepad.right_trigger / 255) * 90)
            self.th_horizontal_0 = (0x5A + right_trigger)
            self.th_horizontal_1 = (0x5A + right_trigger)
            self.th_horizontal_2 = (0x5A + right_trigger)
            self.th_horizontal_3 = (0x5A + right_trigger)

        if state.gamepad.left_trigger and (state.gamepad.buttons & 0b0000000100000000 == 0) and (
                state.gamepad.buttons & 0b0000001000000000 == 0):
            left_trigger = int((state.gamepad.left_trigger / 255) * 90)
            self.th_horizontal_0 = (0x5A - left_trigger)
            self.th_horizontal_1 = (0x5A - left_trigger)
            self.th_horizontal_2 = (0x5A - left_trigger)
            self.th_horizontal_3 = (0x5A - left_trigger)

        # выполняем отправку по мере нажатия кнопок
        # pad.on_state_changed(state)

    def appendDebugInfo(self, UI):
        # gyro calibration
        if UI.checkBoxCalibrationMode.isChecked():
            self.isCalibrationNeeded = 0xFF
