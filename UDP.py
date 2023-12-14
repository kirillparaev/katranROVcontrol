import socket
from array import *


class UDPConnection:
    def __init__(self, remoteIP, remotePort):
        self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddressPort = (remoteIP, remotePort)
        self.bufferSize = 1024
        self.hasSentFirstPacket = False
        self.isInDebugMode = False
        self.leftStickX_prev = 0
        self.leftStickY_prev = 0
        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, 1, 1])
        '''
        вертикальные 1-2 - [0-1]
        горизонтальные 1-4 - [2-5]
        манипулятор - [6-7]
        '''
        self.msgFrom = self.toWrite.tobytes()
        self.prevPacket = self.msgFrom
        self.receivedPacket = None  # добавляем новую переменную
        self.toRead = array('B', [0, 0, 0, 0, 0, 0])

    def sendPacket(self):
        if not self.hasSentFirstPacket:
            for i in range(5):
                self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
            self.hasSentFirstPacket = True
        elif self.msgFrom == self.prevPacket:
            return
        else:
            self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)
        self.prevPacket = self.msgFrom

    def receivePacket(self):
        data, addr = self.UDPClientSocket.recvfrom(6)
        receivedPacket = array('B', data)
        if receivedPacket is None:
            receivedPacket = array('B', [-1, -1, -1, -1, -1, -1])
        return receivedPacket

    def clearPacket(self):
        self.msgFrom = self.toWrite.tobytes()
        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, self.toWrite[6], self.toWrite[7]])
        self.toRead = array('B', [0, 0, 0, 0, 0, 0])

    def formPacket(self, state):
        if state.Gamepad.wButtons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх (приоритет)
            self.toWrite[0] = 127
            self.toWrite[1] = 127
        elif state.Gamepad.wButtons & 0b0001000000000000:  # крестик\A - погрузить робота
            self.toWrite[0] = 25
            self.toWrite[1] = 25
        else:
            self.toWrite[0] = 91
            self.toWrite[1] = 91

        if state.Gamepad.wButtons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси направо
            self.toWrite[2] = 127  # вращение боковых движителей в этом и следующем if
            self.toWrite[3] = 127
        else:
            self.toWrite[2] = 91
            self.toWrite[3] = 91

        if state.Gamepad.wButtons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси налево
            self.toWrite[4] = 127
            self.toWrite[5] = 127
        else:
            self.toWrite[4] = 91
            self.toWrite[5] = 91

        if state.Gamepad.bRightTrigger:
            right_trigger = int((state.Gamepad.bRightTrigger / 255) * 36)
            for i in range(2, 6):
                self.toWrite[i] = self.toWrite[i] + right_trigger
            '''
            self.toWrite[2] = (91 + right_trigger)
            self.toWrite[3] = (91 + right_trigger)
            self.toWrite[4] = (91 + right_trigger)
            self.toWrite[5] = (91 + right_trigger)
            '''

        if state.Gamepad.bLeftTrigger:
            left_trigger = int((state.Gamepad.bLeftTrigger / 255) * 66)
            for i in range(2, 6):
                self.toWrite[i] = self.toWrite[i] - left_trigger
            '''
            self.toWrite[2] = (91 - left_trigger)
            self.toWrite[3] = (91 - left_trigger)
            self.toWrite[4] = (91 - left_trigger)
            self.toWrite[5] = (91 - left_trigger)
            '''

        if state.Gamepad.wButtons & 2:
            # вниз - закрыть манипулятор
            self.toWrite[6] = 2
        elif state.Gamepad.wButtons & 1:
            # вверх - открыть манипулятор
            self.toWrite[6] = 0
        else:
            self.toWrite[6] = 1

        if state.Gamepad.wButtons & 4:
            # влево - вращать манипулятор влево
            self.toWrite[7] = 2
        elif state.Gamepad.wButtons & 8:
            # вправо - вращать манипулятор вправо
            self.toWrite[7] = 0
        else:
            self.toWrite[7] = 1

        if state.Gamepad.wButtons & 16384: # квадрат и круг - стабилизация тангажа
            self.toWrite[0] = 127
            self.toWrite[1] = 25
        elif state.Gamepad.wButtons & 8192:
            self.toWrite[0] = 25
            self.toWrite[1] = 127

        if state.Gamepad.sThumbLX:
            if state.Gamepad.sThumbLX > 10000:
                if self.toWrite[4] > 91 and self.toWrite[5] > 91 and not state.Gamepad.wButtons & 0b0000001000000000:
                    self.toWrite[4] = self.toWrite[4] - abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                    self.toWrite[5] = self.toWrite[5] - abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                elif state.Gamepad.bLeftTrigger:
                    self.toWrite[2] = self.toWrite[2] + abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                    self.toWrite[3] = self.toWrite[3] + abs(int(state.Gamepad.sThumbLX / 32768 * 32))
            elif state.Gamepad.sThumbLX < -10000:
                if self.toWrite[2] > 91 and self.toWrite[3] > 91 and not state.Gamepad.wButtons & 0b0000000100000000:
                    self.toWrite[2] = self.toWrite[2] - abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                    self.toWrite[3] = self.toWrite[3] - abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                elif state.Gamepad.bLeftTrigger:
                    self.toWrite[4] = self.toWrite[4] + abs(int(state.Gamepad.sThumbLX / 32768 * 32))
                    self.toWrite[5] = self.toWrite[5] + abs(int(state.Gamepad.sThumbLX / 32768 * 32))
