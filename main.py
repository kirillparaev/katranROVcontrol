import sys

if sys.platform == 'win32':
    import XInput
elif sys.platform == 'linux':
    import gamepad_linux
import UDP
from ui import *
from threading import Thread
import ExtendedUI
import resources_rc


def linux_inputHandling():
    rov_UDP.sendPacket()
    pad = gamepad_linux.Gamepad_linux()
    pad.startBackgroundUpdates()
    while True:
        if gamepad_linux.available():
            state = pad.convertState()
            window.updateUI(rov_UDP, state)
            if state:
                rov_UDP.formPacket(state)
                rov_UDP.receivePacket()
                rov_UDP.sendPacket()
                window.updateUI(rov_UDP, state)
                rov_UDP.clearPacket()
        else:
            window.label_padNotDetected.setText("Нет геймпада")
            is_connected = gamepad_linux.available()
            while is_connected is False:
                is_connected = gamepad_linux.available()
                rov_UDP.receivePacket()
                rov_UDP.sendPacket()
                window.updateUI(rov_UDP)
                rov_UDP.clearPacket()


def inputHandling():
    # введенные данные на регуляторы брать из ui и передавать в udp объект
    rov_UDP.sendPacket()
    while True:
        if XInput.get_connected()[0]:
            state = XInput.get_state(0)
            window.updateUI(rov_UDP, state)
            if state:
                rov_UDP.formPacket(state)
                rov_UDP.receivePacket()
                rov_UDP.sendPacket()
                window.updateUI(rov_UDP, state)
                rov_UDP.clearPacket()
        else:
            window.label_padNotDetected.setText("Нет геймпада")
            is_connected = XInput.get_connected()[0]
            while is_connected is False:
                is_connected = XInput.get_connected()[0]
                rov_UDP.receivePacket()
                rov_UDP.sendPacket()
                window.updateUI(rov_UDP)
                rov_UDP.clearPacket()


if __name__ == "__main__":
    # прикрутить ввод ip адреса и порта
    rov_UDP = UDP.UDPConnection("192.168.1.177", 8080)
    # rov_UDP = UDP.UDPConnection("127.0.0.1", 8080) # local debug
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    window = ExtendedUI.ExtendedUI()
    window.setupUi(mainWindow)
    mainWindow.show()
    if sys.platform == 'win32':
        inputStream = Thread(target=inputHandling, args=(), daemon=True)
        inputStream.start()
    elif sys.platform == 'linux':
        inputStream = Thread(target=linux_inputHandling, args=(), daemon=True)
        inputStream.start()
    sys.exit(app.exec())
