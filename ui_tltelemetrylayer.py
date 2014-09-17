# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tltelemetrylayer.ui'
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

class Ui_tlTelemetryLayer(object):
    def setupUi(self, tlTelemetryLayer):
        tlTelemetryLayer.setObjectName(_fromUtf8("tlTelemetryLayer"))
        tlTelemetryLayer.resize(300, 328)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tlTelemetryLayer.sizePolicy().hasHeightForWidth())
        tlTelemetryLayer.setSizePolicy(sizePolicy)
        tlTelemetryLayer.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dockWidget = QtGui.QDockWidget(tlTelemetryLayer)
        self.dockWidget.setGeometry(QtCore.QRect(0, 0, 301, 321))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.brokerManagerWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.brokerManagerWidget.setGeometry(QtCore.QRect(10, 22, 281, 241))
        self.brokerManagerWidget.setObjectName(_fromUtf8("brokerManagerWidget"))
        self.globalSettings = QtGui.QWidget()
        self.globalSettings.setObjectName(_fromUtf8("globalSettings"))
        self.groupBox = QtGui.QGroupBox(self.globalSettings)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 171, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.logInfo = QtGui.QCheckBox(self.groupBox)
        self.logInfo.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.logInfo.setObjectName(_fromUtf8("logInfo"))
        self.logWarn = QtGui.QCheckBox(self.groupBox)
        self.logWarn.setGeometry(QtCore.QRect(10, 50, 85, 18))
        self.logWarn.setObjectName(_fromUtf8("logWarn"))
        self.logDebug = QtGui.QCheckBox(self.groupBox)
        self.logDebug.setGeometry(QtCore.QRect(10, 70, 85, 18))
        self.logDebug.setObjectName(_fromUtf8("logDebug"))
        self.logCritical = QtGui.QCheckBox(self.groupBox)
        self.logCritical.setGeometry(QtCore.QRect(10, 90, 85, 18))
        self.logCritical.setObjectName(_fromUtf8("logCritical"))
        self.ckShowLog = QtGui.QCheckBox(self.groupBox)
        self.ckShowLog.setGeometry(QtCore.QRect(7, 110, 91, 32))
        self.ckShowLog.setObjectName(_fromUtf8("ckShowLog"))
        self.btnApply = QtGui.QPushButton(self.globalSettings)
        self.btnApply.setGeometry(QtCore.QRect(195, 180, 81, 32))
        self.btnApply.setObjectName(_fromUtf8("btnApply"))
        self.brokerManagerWidget.addTab(self.globalSettings, _fromUtf8(""))
        self.brokerList = QtGui.QWidget()
        self.brokerList.setObjectName(_fromUtf8("brokerList"))
        self.tableBrokerList = QtGui.QTableWidget(self.brokerList)
        self.tableBrokerList.setGeometry(QtCore.QRect(4, 30, 256, 161))
        self.tableBrokerList.setObjectName(_fromUtf8("tableBrokerList"))
        self.tableBrokerList.setColumnCount(0)
        self.tableBrokerList.setRowCount(0)
        self.btnAdd = QtGui.QPushButton(self.brokerList)
        self.btnAdd.setGeometry(QtCore.QRect(0, 0, 71, 32))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.label = QtGui.QLabel(self.brokerList)
        self.label.setGeometry(QtCore.QRect(80, 10, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.brokerManagerWidget.addTab(self.brokerList, _fromUtf8(""))
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(tlTelemetryLayer)
        self.brokerManagerWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(tlTelemetryLayer)

    def retranslateUi(self, tlTelemetryLayer):
        tlTelemetryLayer.setWindowTitle(_translate("tlTelemetryLayer", "Edit Feature", None))
        tlTelemetryLayer.setToolTip(_translate("tlTelemetryLayer", "<html><head/><body><p>Add Feature</p><p><br/></p></body></html>", None))
        tlTelemetryLayer.setProperty("text", _translate("tlTelemetryLayer", "Edit Feature", None))
        self.groupBox.setTitle(_translate("tlTelemetryLayer", "Loggers", None))
        self.logInfo.setText(_translate("tlTelemetryLayer", "Info", None))
        self.logWarn.setText(_translate("tlTelemetryLayer", "Warn", None))
        self.logDebug.setText(_translate("tlTelemetryLayer", "Debug", None))
        self.logCritical.setText(_translate("tlTelemetryLayer", "Critical", None))
        self.ckShowLog.setText(_translate("tlTelemetryLayer", "Show Log", None))
        self.btnApply.setText(_translate("tlTelemetryLayer", "Apply", None))
        self.brokerManagerWidget.setTabText(self.brokerManagerWidget.indexOf(self.globalSettings), _translate("tlTelemetryLayer", "Settings", None))
        self.btnAdd.setToolTip(_translate("tlTelemetryLayer", "<html><head/><body><p>Add a new broker</p></body></html>", None))
        self.btnAdd.setText(_translate("tlTelemetryLayer", "Add", None))
        self.label.setText(_translate("tlTelemetryLayer", "Manage MQTT Broker List", None))
        self.brokerManagerWidget.setTabText(self.brokerManagerWidget.indexOf(self.brokerList), _translate("tlTelemetryLayer", "Message Brokers", None))

