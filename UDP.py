import socket
from array import *


class UDPConnection:
    def __init__(self, remoteIP, remotePort):
        self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddressPort = (remoteIP, remotePort)
        self.bufferSize = 1024
        self.hasSentFirstPacket = False
        self.isInDebugMode = False

        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, 1, 1])
        '''
        вертикальные 1-2 - [0-1]
        горизонтальные 1-4 - [2-5]
        манипулятор - [6-7]
        '''
        self.msgFrom = self.toWrite.tobytes()
        self.prevPacket = self.msgFrom

    def sendPacket(self):
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
        self.msgFrom = self.toWrite.tobytes()
        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, self.toWrite[6], self.toWrite[7]])

    def formPacket(self, state):
        if state.Gamepad.wButtons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх (приоритет)
            self.toWrite[0] = 115
            self.toWrite[1] = 115
        elif state.Gamepad.wButtons & 0b0001000000000000:  # крестик\A - погрузить робота
            self.toWrite[0] = 67
            self.toWrite[1] = 67
        else:
            self.toWrite[0] = 91
            self.toWrite[1] = 91

        if state.Gamepad.wButtons & 2:  # влево - вращать манипулятор влево
            self.toWrite[6] = 2
        elif state.Gamepad.wButtons & 1:  # вправо - вращать манипулятор вправо
            self.toWrite[6] = 0
        else:
            self.toWrite[6] = 1

        if state.Gamepad.wButtons & 4:  # вверх - открыть манипулятор
            self.toWrite[7] = 2
        elif state.Gamepad.wButtons & 8:  # вниз - закрыть манипулятор
            self.toWrite[7] = 0
        else:
            self.toWrite[7] = 1

        # левый стик
        if state.Gamepad.sThumbLX and state.Gamepad.sThumbLY:  # init: 67 - 91 - 115
            leftStickX = int(state.Gamepad.sThumbLX / 32768 * 24)  # -32768 - 0 - 32768      вперед назад
            leftStickY = int(state.Gamepad.sThumbLY / 32768 * 24)  # влево вправо
            # пусть у нас движки 0,1 находятся на левом борту, а 2,3 - на правом.
            # тогда, чтобы повернуть на нужно подавать большую скорость на движки стороны,
            # протвивополжной направлению поворота.
            # Например, хотим повернуть налево, двигаем правую сторону аппарата.
            if abs(state.Gamepad.sThumbLY) > 10000:  # 10000 - мертвая зона
                for i in range(2, 6):
                    self.toWrite[i] = (self.toWrite[i] + leftStickY)

            if abs(state.Gamepad.sThumbLX) > 10000 and leftStickX < 0:
                self.toWrite[4] = (self.toWrite[4] + leftStickX)
                self.toWrite[5] = (self.toWrite[5] + leftStickX)
            elif abs(state.Gamepad.sThumbLX) > 10000 and leftStickX > 0:
                self.toWrite[2] = (self.toWrite[2] + leftStickX)
                self.toWrite[3] = (self.toWrite[3] + leftStickX)
