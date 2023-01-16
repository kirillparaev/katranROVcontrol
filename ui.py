from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 568)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(600, 32))
        self.label_title.setMaximumSize(QtCore.QSize(9999999, 9999999))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 144, 227);")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.frameAppTabs = QtWidgets.QFrame(self.frame_title)
        self.frameAppTabs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frameAppTabs.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameAppTabs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameAppTabs.setObjectName("frameAppTabs")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameAppTabs)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnCameraTab = QtWidgets.QPushButton(self.frameAppTabs)
        self.btnCameraTab.setMinimumSize(QtCore.QSize(56, 20))
        self.btnCameraTab.setStyleSheet("border: 3px solid rgb(43, 43, 43);\n"
"border-radius: 5px;\n"
"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btnCameraTab.setObjectName("btnCameraTab")
        self.horizontalLayout_4.addWidget(self.btnCameraTab)
        self.btnDebugTab = QtWidgets.QPushButton(self.frameAppTabs)
        self.btnDebugTab.setMinimumSize(QtCore.QSize(56, 20))
        self.btnDebugTab.setStyleSheet("border: 3px solid rgb(43, 43, 43);\n"
"border-radius: 5px;\n"
"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btnDebugTab.setObjectName("btnDebugTab")
        self.btnCameraTab.clicked.connect(self.SwitchTabCamera)
        self.btnDebugTab.clicked.connect(self.SwitchTabDebug)
        self.horizontalLayout_4.addWidget(self.btnDebugTab)
        self.horizontalLayout_2.addWidget(self.frameAppTabs)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-image: url(:/icons/icons/icon_minimize.png);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(43, 43, 43);\n"
"}\n"
"QPushButton:hover {    \n"
"    \n"
"    background-color: rgb(91, 91, 91);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        self.btn_maximize.setFont(font)
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-image: url(:/icons/icons/icon_maximize.png);\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(43, 43, 43);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(91, 91, 91);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(221, 114, 21);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-image: url(:/icons/icons/icon_close.png);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgb(159, 80, 15);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar_and_styleSheet = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar_and_styleSheet.setStyleSheet("/*  ///////////////////////////////////////////////////// Check Box */\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(221, 114, 21);\n"
"    border: 3px solid rgb(159, 80, 15);    \n"
"    background-image: url(:/icons/icons/cil-check-alt.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QCheckBox {\n"
"    background-color: none;\n"
"    color: rgb(222, 225, 229);\n"
"}\n"
"\n"
"/* ///////////////////////////////////// Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(221, 114, 21);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(159, 80, 15);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(144, 72, 14);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(221, 114, 21);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(159, 80, 15);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(144, 72, 14);\n"
"}\n"
"QSlider {\n"
"    background-color: none;\n"
"}\n"
"\n"
"/* Frame */\n"
"QFrame{\n"
"    background-color:none;\n"
"}\n"
"\n"
"/*  Label */\n"
"QLabel {\n"
"    color: rgb(222, 225, 229);\n"
"}\n"
"\n"
"/* The content_bar itself */\n"
"background-color: none;")
        self.content_bar_and_styleSheet.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content_bar_and_styleSheet.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bar_and_styleSheet.setObjectName("content_bar_and_styleSheet")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_bar_and_styleSheet)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dashboard = QtWidgets.QStackedWidget(self.content_bar_and_styleSheet)
        self.dashboard.setObjectName("dashboard")
        self.page_Camera = QtWidgets.QWidget()
        self.page_Camera.setObjectName("page_Camera")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.page_Camera)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.page_Camera)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.FeedLabel = QtWidgets.QLabel(self.frame_10)
        self.FeedLabel.setText("")
        self.FeedLabel.setObjectName("FeedLabel")
        self.verticalLayout_9.addWidget(self.FeedLabel)
        self.horizontalLayout_12.addWidget(self.frame_10)
        self.dashboard.addWidget(self.page_Camera)
        self.page_Debug = QtWidgets.QWidget()
        self.page_Debug.setObjectName("page_Debug")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_Debug)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.page_Debug)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.labelButtonsPressed = QtWidgets.QLabel(self.frame_4)
        self.labelButtonsPressed.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        self.labelButtonsPressed.setFont(font)
        self.labelButtonsPressed.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelButtonsPressed.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelButtonsPressed.setScaledContents(False)
        self.labelButtonsPressed.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelButtonsPressed.setWordWrap(True)
        self.labelButtonsPressed.setObjectName("labelButtonsPressed")
        self.horizontalLayout_8.addWidget(self.labelButtonsPressed)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.checkBox_Y_btn = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_Y_btn.setEnabled(False)
        self.checkBox_Y_btn.setStyleSheet("border-radius: 10px;")
        self.checkBox_Y_btn.setObjectName("checkBox_Y_btn")
        self.horizontalLayout_6.addWidget(self.checkBox_Y_btn)
        self.checkBox_A_btn = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_A_btn.setEnabled(False)
        self.checkBox_A_btn.setObjectName("checkBox_A_btn")
        self.horizontalLayout_6.addWidget(self.checkBox_A_btn)
        self.checkBox_LB_btn = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_LB_btn.setEnabled(False)
        self.checkBox_LB_btn.setObjectName("checkBox_LB_btn")
        self.horizontalLayout_6.addWidget(self.checkBox_LB_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_LT_L2 = QtWidgets.QLabel(self.frame_7)
        self.label_LT_L2.setObjectName("label_LT_L2")
        self.horizontalLayout_6.addWidget(self.label_LT_L2)
        self.horizontalSlider_LT = QtWidgets.QSlider(self.frame_7)
        self.horizontalSlider_LT.setEnabled(False)
        self.horizontalSlider_LT.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_LT.setObjectName("horizontalSlider_LT")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_LT)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.checkBox_X_btn = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_X_btn.setEnabled(False)
        self.checkBox_X_btn.setObjectName("checkBox_X_btn")
        self.horizontalLayout_7.addWidget(self.checkBox_X_btn)
        self.checkBox_B_btn = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_B_btn.setEnabled(False)
        self.checkBox_B_btn.setObjectName("checkBox_B_btn")
        self.horizontalLayout_7.addWidget(self.checkBox_B_btn)
        self.checkBox_RB_btn = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_RB_btn.setEnabled(False)
        self.checkBox_RB_btn.setObjectName("checkBox_RB_btn")
        self.horizontalLayout_7.addWidget(self.checkBox_RB_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label_RT_R2 = QtWidgets.QLabel(self.frame_8)
        self.label_RT_R2.setObjectName("label_RT_R2")
        self.horizontalLayout_7.addWidget(self.label_RT_R2)
        self.horizontalSlider_RT = QtWidgets.QSlider(self.frame_8)
        self.horizontalSlider_RT.setEnabled(False)
        self.horizontalSlider_RT.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_RT.setObjectName("horizontalSlider_RT")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_RT)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.page_Debug)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.labelSendingPacket = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.labelSendingPacket.setFont(font)
        self.labelSendingPacket.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSendingPacket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelSendingPacket.setObjectName("labelSendingPacket")
        self.horizontalLayout_10.addWidget(self.labelSendingPacket)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.packet_1st_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_1st_byte.setObjectName("packet_1st_byte")
        self.horizontalLayout_11.addWidget(self.packet_1st_byte)
        self.packet_2nd_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_2nd_byte.setObjectName("packet_2nd_byte")
        self.horizontalLayout_11.addWidget(self.packet_2nd_byte)
        self.packet_3rd_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_3rd_byte.setObjectName("packet_3rd_byte")
        self.horizontalLayout_11.addWidget(self.packet_3rd_byte)
        self.packet_4th_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_4th_byte.setObjectName("packet_4th_byte")
        self.horizontalLayout_11.addWidget(self.packet_4th_byte)
        self.packet_5th_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_5th_byte.setObjectName("packet_5th_byte")
        self.horizontalLayout_11.addWidget(self.packet_5th_byte)
        self.packet_6th_byte = QtWidgets.QLabel(self.frame_12)
        self.packet_6th_byte.setObjectName("packet_6th_byte")
        self.horizontalLayout_11.addWidget(self.packet_6th_byte)
        self.labelCalibrating = QtWidgets.QLabel(self.frame_12)
        self.labelCalibrating.setObjectName("labelCalibrating")
        self.horizontalLayout_11.addWidget(self.labelCalibrating)
        self.label_ServoPacket = QtWidgets.QLabel(self.frame_12)
        self.label_ServoPacket.setObjectName("label_ServoPacket")
        self.horizontalLayout_11.addWidget(self.label_ServoPacket)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.page_Debug)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_padNotDetected = QtWidgets.QLabel(self.frame_11)
        self.label_padNotDetected.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.label_padNotDetected.setFont(font)
        self.label_padNotDetected.setObjectName("label_padNotDetected")
        self.horizontalLayout_9.addWidget(self.label_padNotDetected)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.checkBoxCalibrationMode = QtWidgets.QCheckBox(self.frame_11)
        self.checkBoxCalibrationMode.setObjectName("checkBoxCalibrationMode")
        self.horizontalLayout_9.addWidget(self.checkBoxCalibrationMode)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.dashboard.addWidget(self.page_Debug)
        self.verticalLayout_2.addWidget(self.dashboard)
        self.verticalLayout.addWidget(self.content_bar_and_styleSheet)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dashboard.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "katranROVcontrols"))
        self.btnCameraTab.setText(_translate("MainWindow", "Camera"))
        self.btnDebugTab.setText(_translate("MainWindow", "Debug"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.labelButtonsPressed.setText(_translate("MainWindow", "Нажатые кнопки: "))
        self.checkBox_Y_btn.setText(_translate("MainWindow", "Y / Triangle"))
        self.checkBox_A_btn.setText(_translate("MainWindow", "A / Cross"))
        self.checkBox_LB_btn.setText(_translate("MainWindow", "LB / L1"))
        self.label_LT_L2.setText(_translate("MainWindow", "LT / L2:"))
        self.checkBox_X_btn.setText(_translate("MainWindow", "X / Square"))
        self.checkBox_B_btn.setText(_translate("MainWindow", "B / Circle"))
        self.checkBox_RB_btn.setText(_translate("MainWindow", "RB / R1"))
        self.label_RT_R2.setText(_translate("MainWindow", "RT / R2"))
        self.labelSendingPacket.setText(_translate("MainWindow", "Отправляемый пакет: "))
        self.packet_1st_byte.setText(_translate("MainWindow", "5A"))
        self.packet_2nd_byte.setText(_translate("MainWindow", "5A"))
        self.packet_3rd_byte.setText(_translate("MainWindow", "5A"))
        self.packet_4th_byte.setText(_translate("MainWindow", "5A"))
        self.packet_5th_byte.setText(_translate("MainWindow", "5A"))
        self.packet_6th_byte.setText(_translate("MainWindow", "5A"))
        self.labelCalibrating.setText(_translate("MainWindow", "00"))
        self.label_ServoPacket.setText(_translate("MainWindow", "00"))
        self.label_padNotDetected.setText(_translate("MainWindow", "!!! Геймпад не обнаружен !!!"))
        self.checkBoxCalibrationMode.setText(_translate("MainWindow", "Калибровка гироскопа"))

    def SwitchTabCamera(self):
        self.dashboard.setCurrentIndex(0)

    def SwitchTabDebug(self):
        self.dashboard.setCurrentIndex(1)