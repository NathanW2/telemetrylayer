# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tlbrokerconfig.ui'
#
# Created: Wed Sep 10 08:16:18 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tlBrokerConfig(object):
    def setupUi(self, tlBrokerConfig):
        tlBrokerConfig.setObjectName(_fromUtf8("tlBrokerConfig"))
        tlBrokerConfig.resize(300, 376)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tlBrokerConfig.sizePolicy().hasHeightForWidth())
        tlBrokerConfig.setSizePolicy(sizePolicy)
        tlBrokerConfig.setMaximumSize(QtCore.QSize(300, 16777215))
        tlBrokerConfig.setProperty("currentTabName", _fromUtf8("Fubar"))
        self.dockWidget = QtGui.QDockWidget(tlBrokerConfig)
        self.dockWidget.setGeometry(QtCore.QRect(0, 0, 305, 411))
        self.dockWidget.setMinimumSize(QtCore.QSize(305, 401))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(305, 375))
        self.dockWidgetContents.setBaseSize(QtCore.QSize(0, 375))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.Tabs = QtGui.QTabWidget(self.dockWidgetContents)
        self.Tabs.setGeometry(QtCore.QRect(10, 10, 281, 331))
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.tabConnect = QtGui.QWidget()
        self.tabConnect.setEnabled(True)
        self.tabConnect.setObjectName(_fromUtf8("tabConnect"))
        self.connectPoll = QtGui.QComboBox(self.tabConnect)
        self.connectPoll.setGeometry(QtCore.QRect(130, 194, 51, 26))
        self.connectPoll.setObjectName(_fromUtf8("connectPoll"))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectPoll.addItem(_fromUtf8(""))
        self.connectUsername = QtGui.QLineEdit(self.tabConnect)
        self.connectUsername.setGeometry(QtCore.QRect(30, 160, 91, 22))
        self.connectUsername.setMaxLength(8)
        self.connectUsername.setObjectName(_fromUtf8("connectUsername"))
        self.connectTest = QtGui.QPushButton(self.tabConnect)
        self.connectTest.setGeometry(QtCore.QRect(141, 267, 61, 32))
        self.connectTest.setObjectName(_fromUtf8("connectTest"))
        self.connectPollLabel2 = QtGui.QLabel(self.tabConnect)
        self.connectPollLabel2.setGeometry(QtCore.QRect(190, 204, 71, 16))
        self.connectPollLabel2.setObjectName(_fromUtf8("connectPollLabel2"))
        self.connectPort = QtGui.QLineEdit(self.tabConnect)
        self.connectPort.setGeometry(QtCore.QRect(170, 83, 51, 22))
        self.connectPort.setMaxLength(4)
        self.connectPort.setObjectName(_fromUtf8("connectPort"))
        self.connectApply = QtGui.QPushButton(self.tabConnect)
        self.connectApply.setGeometry(QtCore.QRect(201, 268, 61, 31))
        self.connectApply.setObjectName(_fromUtf8("connectApply"))
        self.connectName = QtGui.QLineEdit(self.tabConnect)
        self.connectName.setGeometry(QtCore.QRect(80, 7, 141, 22))
        self.connectName.setMaxLength(12)
        self.connectName.setObjectName(_fromUtf8("connectName"))
        self.connectNameLabel = QtGui.QLabel(self.tabConnect)
        self.connectNameLabel.setGeometry(QtCore.QRect(30, 11, 41, 16))
        self.connectNameLabel.setObjectName(_fromUtf8("connectNameLabel"))
        self.connectPasswordLabel = QtGui.QLabel(self.tabConnect)
        self.connectPasswordLabel.setGeometry(QtCore.QRect(132, 143, 61, 16))
        self.connectPasswordLabel.setObjectName(_fromUtf8("connectPasswordLabel"))
        self.connectPortLabel = QtGui.QLabel(self.tabConnect)
        self.connectPortLabel.setGeometry(QtCore.QRect(170, 67, 31, 16))
        self.connectPortLabel.setObjectName(_fromUtf8("connectPortLabel"))
        self.connectUsernameLabel = QtGui.QLabel(self.tabConnect)
        self.connectUsernameLabel.setGeometry(QtCore.QRect(30, 143, 71, 16))
        self.connectUsernameLabel.setObjectName(_fromUtf8("connectUsernameLabel"))
        self.connectCancel = QtGui.QPushButton(self.tabConnect)
        self.connectCancel.setGeometry(QtCore.QRect(71, 267, 71, 32))
        self.connectCancel.setObjectName(_fromUtf8("connectCancel"))
        self.connectPollLabel = QtGui.QLabel(self.tabConnect)
        self.connectPollLabel.setGeometry(QtCore.QRect(30, 204, 101, 16))
        self.connectPollLabel.setObjectName(_fromUtf8("connectPollLabel"))
        self.connectHelp = QtGui.QPushButton(self.tabConnect)
        self.connectHelp.setGeometry(QtCore.QRect(12, 268, 61, 32))
        self.connectHelp.setObjectName(_fromUtf8("connectHelp"))
        self.connectPassword = QtGui.QLineEdit(self.tabConnect)
        self.connectPassword.setGeometry(QtCore.QRect(132, 160, 91, 22))
        self.connectPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.connectPassword.setInputMask(_fromUtf8(""))
        self.connectPassword.setText(_fromUtf8(""))
        self.connectPassword.setMaxLength(24)
        self.connectPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.connectPassword.setObjectName(_fromUtf8("connectPassword"))
        self.connectHostLabel = QtGui.QLabel(self.tabConnect)
        self.connectHostLabel.setGeometry(QtCore.QRect(30, 67, 121, 16))
        self.connectHostLabel.setObjectName(_fromUtf8("connectHostLabel"))
        self.connectHost = QtGui.QLineEdit(self.tabConnect)
        self.connectHost.setGeometry(QtCore.QRect(30, 83, 131, 21))
        self.connectHost.setAccessibleDescription(_fromUtf8(""))
        self.connectHost.setMaxLength(64)
        self.connectHost.setObjectName(_fromUtf8("connectHost"))
        self.connectTopicManagerLabel = QtGui.QLabel(self.tabConnect)
        self.connectTopicManagerLabel.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.connectTopicManagerLabel.setObjectName(_fromUtf8("connectTopicManagerLabel"))
        self.connectTopicManager = QtGui.QComboBox(self.tabConnect)
        self.connectTopicManager.setGeometry(QtCore.QRect(79, 33, 141, 26))
        self.connectTopicManager.setObjectName(_fromUtf8("connectTopicManager"))
        self.connectKeepAliveLabel = QtGui.QLabel(self.tabConnect)
        self.connectKeepAliveLabel.setGeometry(QtCore.QRect(30, 231, 101, 16))
        self.connectKeepAliveLabel.setObjectName(_fromUtf8("connectKeepAliveLabel"))
        self.connectKeepAlive = QtGui.QComboBox(self.tabConnect)
        self.connectKeepAlive.setGeometry(QtCore.QRect(130, 221, 51, 26))
        self.connectKeepAlive.setObjectName(_fromUtf8("connectKeepAlive"))
        self.connectKeepAlive.addItem(_fromUtf8(""))
        self.connectKeepAlive.addItem(_fromUtf8(""))
        self.connectKeepAlive.addItem(_fromUtf8(""))
        self.connectKeepAlive.addItem(_fromUtf8(""))
        self.connectHostAlt = QtGui.QLineEdit(self.tabConnect)
        self.connectHostAlt.setGeometry(QtCore.QRect(30, 110, 131, 21))
        self.connectHostAlt.setAccessibleDescription(_fromUtf8(""))
        self.connectHostAlt.setMaxLength(64)
        self.connectHostAlt.setObjectName(_fromUtf8("connectHostAlt"))
        self.connectPortAlt = QtGui.QLineEdit(self.tabConnect)
        self.connectPortAlt.setGeometry(QtCore.QRect(170, 110, 51, 22))
        self.connectPortAlt.setMaxLength(4)
        self.connectPortAlt.setObjectName(_fromUtf8("connectPortAlt"))
        self.connectAltLabel = QtGui.QLabel(self.tabConnect)
        self.connectAltLabel.setGeometry(QtCore.QRect(228, 114, 31, 16))
        self.connectAltLabel.setObjectName(_fromUtf8("connectAltLabel"))
        self.Tabs.addTab(self.tabConnect, _fromUtf8(""))
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(tlBrokerConfig)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tlBrokerConfig)
        tlBrokerConfig.setTabOrder(self.connectName, self.connectHost)
        tlBrokerConfig.setTabOrder(self.connectHost, self.connectPort)
        tlBrokerConfig.setTabOrder(self.connectPort, self.connectUsername)
        tlBrokerConfig.setTabOrder(self.connectUsername, self.connectPassword)
        tlBrokerConfig.setTabOrder(self.connectPassword, self.connectPoll)
        tlBrokerConfig.setTabOrder(self.connectPoll, self.connectTest)
        tlBrokerConfig.setTabOrder(self.connectTest, self.connectApply)
        tlBrokerConfig.setTabOrder(self.connectApply, self.Tabs)
        tlBrokerConfig.setTabOrder(self.Tabs, self.connectCancel)
        tlBrokerConfig.setTabOrder(self.connectCancel, self.connectHelp)

    def retranslateUi(self, tlBrokerConfig):
        tlBrokerConfig.setWindowTitle(_translate("tlBrokerConfig", "Broker Configuration", None))
        self.dockWidget.setWindowTitle(_translate("tlBrokerConfig", "Broker Configuration", None))
        self.connectPoll.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Keep Alive values for MQTT Connection settings - default 60 seconds</p></body></html>", None))
        self.connectPoll.setItemText(0, _translate("tlBrokerConfig", "0", None))
        self.connectPoll.setItemText(1, _translate("tlBrokerConfig", "5", None))
        self.connectPoll.setItemText(2, _translate("tlBrokerConfig", "10", None))
        self.connectPoll.setItemText(3, _translate("tlBrokerConfig", "30", None))
        self.connectPoll.setItemText(4, _translate("tlBrokerConfig", "60", None))
        self.connectPoll.setItemText(5, _translate("tlBrokerConfig", "305", None))
        self.connectUsername.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>MQTT Broker Username</p></body></html>", None))
        self.connectTest.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Test and save the connection settings</p></body></html>", None))
        self.connectTest.setText(_translate("tlBrokerConfig", "Test", None))
        self.connectPollLabel2.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p><br/></p></body></html>", None))
        self.connectPollLabel2.setText(_translate("tlBrokerConfig", "Seconds", None))
        self.connectPort.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Port of MQTT Broker</p></body></html>", None))
        self.connectPort.setText(_translate("tlBrokerConfig", "1883", None))
        self.connectApply.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Test and save the connection settings</p></body></html>", None))
        self.connectApply.setText(_translate("tlBrokerConfig", "Apply", None))
        self.connectName.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>MQTT Broker Username</p></body></html>", None))
        self.connectName.setText(_translate("tlBrokerConfig", "Broker1", None))
        self.connectNameLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p><br/></p></body></html>", None))
        self.connectNameLabel.setText(_translate("tlBrokerConfig", "Name", None))
        self.connectPasswordLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>8 Digit Network ID</p></body></html>", None))
        self.connectPasswordLabel.setText(_translate("tlBrokerConfig", "Password", None))
        self.connectPortLabel.setText(_translate("tlBrokerConfig", "Port", None))
        self.connectUsernameLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p><br/></p></body></html>", None))
        self.connectUsernameLabel.setText(_translate("tlBrokerConfig", "Username", None))
        self.connectCancel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Test and save the connection settings</p></body></html>", None))
        self.connectCancel.setText(_translate("tlBrokerConfig", "Cancel", None))
        self.connectPollLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Reconnect after how many seconds<br/></p></body></html>", None))
        self.connectPollLabel.setText(_translate("tlBrokerConfig", "Polling", None))
        self.connectHelp.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Test and save the connection settings</p></body></html>", None))
        self.connectHelp.setText(_translate("tlBrokerConfig", "Help", None))
        self.connectPassword.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>MQTT Broker Password</p></body></html>", None))
        self.connectHostLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Internet Host name or IP address of Farmsense Controller</p></body></html>", None))
        self.connectHostLabel.setText(_translate("tlBrokerConfig", "Hostname", None))
        self.connectHost.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Hostname of MQTT Broker</p></body></html>", None))
        self.connectHost.setText(_translate("tlBrokerConfig", "localhost", None))
        self.connectTopicManagerLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Set the Topic Manager. This is the module that manages available topics.</p></body></html>", None))
        self.connectTopicManagerLabel.setText(_translate("tlBrokerConfig", "Type", None))
        self.connectTopicManager.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Set the Topic Manager. This is the module that manages available topics.</p></body></html>", None))
        self.connectKeepAliveLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Reconnect after how many seconds<br/></p></body></html>", None))
        self.connectKeepAliveLabel.setText(_translate("tlBrokerConfig", "Keep Alive", None))
        self.connectKeepAlive.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>Keep Alive values for MQTT Connection settings - default 60 seconds</p></body></html>", None))
        self.connectKeepAlive.setItemText(0, _translate("tlBrokerConfig", "0", None))
        self.connectKeepAlive.setItemText(1, _translate("tlBrokerConfig", "10", None))
        self.connectKeepAlive.setItemText(2, _translate("tlBrokerConfig", "30", None))
        self.connectKeepAlive.setItemText(3, _translate("tlBrokerConfig", "60", None))
        self.connectHostAlt.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>If you have an alternative host you wish to use with this broker, enter it here.</p></body></html>", None))
        self.connectHostAlt.setText(_translate("tlBrokerConfig", "localhost", None))
        self.connectPortAlt.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>If you have an alternative port you wish to use with this broker, enter it here.</p></body></html>", None))
        self.connectPortAlt.setText(_translate("tlBrokerConfig", "1883", None))
        self.connectAltLabel.setToolTip(_translate("tlBrokerConfig", "<html><head/><body><p>If you have an alternative host/port you wish to use with this broker, enter it here.<br/></p></body></html>", None))
        self.connectAltLabel.setText(_translate("tlBrokerConfig", "Alt.", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tabConnect), _translate("tlBrokerConfig", "Broker", None))
