import socket
from array import *


class UDPConnection:
    def __init__(self, remoteIP, remotePort):
        self.UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddressPort = (remoteIP, remotePort)
        self.UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientAddressPort = ("192.168.1.100", 8888)
        # TODO обработать исключение при отстутствии сети
        self.UDPServerSocket.bind(self.clientAddressPort)
        # TODO НУЖНО ДЛЯ РАБОТЫ НО БЯЛТЬ работает только если есть соединение, нужно обработать ошибку
        self.UDPServerSocket.settimeout(3)
        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, 1, 1])
        '''
        вертикальные 1-2 - [0-1]
        горизонтальные 1-4 - [2-5]
        манипулятор - [6-7]
        '''
        self.rearCoefficient = array('f', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.frontCoefficient = array('f', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.msgFrom = self.toWrite.tobytes()
        self.receivedPacket = array('b', [-1, -1, -1, -1, -1, -1])
        self.isConnectionEstablished = False

    def sendPacket(self):
        self.convertPacket()
        self.UDPClientSocket.sendto(self.msgFrom, self.serverAddressPort)

    def receivePacket(self):
        try:
            data, addr = self.UDPServerSocket.recvfrom(18)
            self.isConnectionEstablished = True
            self.receivedPacket = array('b', data)
            # self.decodePacket(self.receivedPacket)
        except TimeoutError as e:
            print(e)
            self.receivedPacket = array('b', [-1, -1, -1, -1, -1, -1])
            self.isConnectionEstablished = False

    def clearPacket(self):
        self.msgFrom = self.toWrite.tobytes()
        self.toWrite = array('B', [91, 91, 91, 91, 91, 91, self.toWrite[6], self.toWrite[7]])

    def formPacket(self, state):
        if state.Gamepad.wButtons & 0b1000000000000000:  # треугольник\Y - поднять робота вверх (приоритет)
            self.frontCoefficient[3] = 1.0
            self.frontCoefficient[4] = 1.0
        elif state.Gamepad.wButtons & 0b0001000000000000:  # крестик\A - погрузить робота
            self.rearCoefficient[3] = 1.0
            self.rearCoefficient[4] = 1.0
        else:
            self.frontCoefficient[3] = 0.0
            self.rearCoefficient[3] = 0.0
            self.frontCoefficient[4] = 0.0
            self.rearCoefficient[4] = 0.0

        if state.Gamepad.wButtons & 0b0000000100000000:  # L1\LB - поворот вокруг своей оси налево
            self.frontCoefficient[0] = 1.0  # вращение боковых движителей в этом и следующем if
            self.frontCoefficient[1] = 1.0
        else:
            self.frontCoefficient[0] = 0.0
            self.rearCoefficient[0] = 0.0
            self.frontCoefficient[1] = 0.0
            self.rearCoefficient[1] = 0.0

        if state.Gamepad.wButtons & 0b0000001000000000:  # R1\RB - поворот вокруг своей оси направо
            self.frontCoefficient[2] = 1.0
            self.frontCoefficient[5] = 1.0
        else:
            self.frontCoefficient[2] = 0.0
            self.rearCoefficient[2] = 0.0
            self.frontCoefficient[5] = 0.0
            self.rearCoefficient[5] = 0.0

        if state.Gamepad.sThumbLX > 1024:
            self.frontCoefficient[5] = state.Gamepad.sThumbLX / 32768
            self.rearCoefficient[2] = state.Gamepad.sThumbLX / 32768
        elif state.Gamepad.sThumbLX < -1024: # сломано из-за кабеля из колбы
            self.frontCoefficient[0] = abs(state.Gamepad.sThumbLX / 32768)
            self.rearCoefficient[1] = abs(state.Gamepad.sThumbLX / 32768)

        if state.Gamepad.bRightTrigger:
            # нижние
            self.frontCoefficient[1] = (state.Gamepad.bRightTrigger / 255)
            self.frontCoefficient[2] = (state.Gamepad.bRightTrigger / 255)

        if state.Gamepad.bLeftTrigger:
            self.rearCoefficient[0] = (state.Gamepad.bLeftTrigger / 255)
            self.rearCoefficient[5] = (state.Gamepad.bLeftTrigger / 255)

        '''
        if state.Gamepad.bRightTrigger:
            # левый борт
            coefficientForLeftSide = 0.75  # коэф ослабления левого борта
            for i in [0, 5]:
                self.frontCoefficient[i] = ((state.Gamepad.bRightTrigger / 255))
            # правый борт
            for i in [1, 2]:
                self.frontCoefficient[i] = ((state.Gamepad.bRightTrigger / 255) * coefficientForLeftSide)
            # от 2 до 5 включительно
        elif state.Gamepad.bLeftTrigger:
            for i in [0, 1, 2, 5]:
                self.rearCoefficient[i] = (state.Gamepad.bLeftTrigger / 255)
            # от 2 до 5 включительно
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

        if state.Gamepad.wButtons & 16384:  # квадрат и круг - стабилизация тангажа
            self.frontCoefficient[3] = 1.0
            self.rearCoefficient[4] = 1.0
        elif state.Gamepad.wButtons & 8192:
            self.rearCoefficient[3] = 1.0
            self.frontCoefficient[4] = 1.0

    def convertPacket(self):
        for i in range(0, 6):
            self.toWrite[i] = int(self.toWrite[i] + (36 * self.frontCoefficient[i]) - (66 * self.rearCoefficient[i]))
        # print("done converting packet")
