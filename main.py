import XInput
import UDP
from ui import *
from threading import Thread
import ExtendedUI
import resources_rc


def inputHandling():
    rov_UDP.sendPacket()
    while True:
        if XInput.get_connected()[0]:
            state = XInput.get_state(0)
            window.updateUI(state)
            if state:
                rov_UDP.formPacket(state)
                rov_UDP.sendPacket()
                rov_UDP.receivePacket()
                window.debug_updatePacketUI(rov_UDP)
                rov_UDP.clearPacket()
        else:
            window.label_padNotDetected.setText("!!! Геймпад не обнаружен !!!")
            is_connected = XInput.get_connected()[0]
            while is_connected is False:
                is_connected = XInput.get_connected()[0]
                rov_UDP.sendPacket()
                rov_UDP.receivePacket()
                window.debug_updatePacketUI(rov_UDP)
                rov_UDP.clearPacket()


if __name__ == "__main__":
    import sys

    if XInput.get_connected()[0]:
        pad = XInput.get_state(0)
    # прикрутить ввод ip адреса и порта
    rov_UDP = UDP.UDPConnection("192.168.0.177", 8080)

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    window = ExtendedUI.ExtendedUI()
    window.setupUi(mainWindow)
    mainWindow.show()
    inputStream = Thread(target=inputHandling, args=(), daemon=True)
    inputStream.start()

    sys.exit(app.exec())
