# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Telemetry Layer
                                 A QGIS plugin
 Interface to Telemetry Layer sensor network
                             -------------------
        begin                : 2014-05-30
        copyright            : (C) 2014 by Andrew McClure
        email                : andrew@southweb.co.nz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from ui_telemetrylayer import Ui_TelemetryLayer
from tlbrokers import tlBrokers as Brokers
from tlbrokerconfig import tlBrokerConfig as BrokerConfig
from lib.tlsettings import tlSettings as Settings
from lib.tllogging import tlLogging as Log

# Add Help Button


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class TelemetryLayer(QtGui.QDialog, Ui_TelemetryLayer):
 
    UPDATE = 1
    DELETE = 2 

    _this = None

    @staticmethod   
    def _getQtBoxStateValue(state):
        if eval(str(state)):
            return Qt.Checked
        else:
            return Qt.Unchecked
    
    def __init__(self,creator):
       super(TelemetryLayer, self).__init__()

       self.iface = creator.iface
       self.plugin_dir = creator.plugin_dir
       self._brokerDlg = None
       self._brokers = Brokers.instance()
       self._setup = False
       self.dockWidget = None
       TelemetryLayer._this = self

       pass
    
    @staticmethod
    def instance():
        return TelemetryLayer._this

    def show(self,broker = None):
        if not self._setup:
            self.setupUi()
            self._setup = True

        if not self.dockWidget.isVisible():
            self.iface.addDockWidget( Qt.LeftDockWidgetArea,   self.dockWidget )
        self.dockWidget.setVisible(True)
        
        if broker !=None:
#            if self._brokerDlg.dockWidget.isVisible():
#                self._brokerDlg.dockWidget.setVisible(False)
            # Add check to see if _brokerDlg is currently open and a prompt to change it if dirty!
            self._updateBroker(broker)
        

    def hide(self):
        if self.dockWidget.isVisible():
            self.dockWidget.setVisible(False)
        

    def setupUi(self):
       super(TelemetryLayer,self).setupUi(self)
       self.dockWidget.setFixedHeight(self.height()) # paramterise
       self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
       self.dockWidget.setWindowTitle(_translate("tlBrokerConfig", "Configure Telemetry Layer", None))
       self.ckShowLog.clicked.connect(self._showLog)
       self.ckShowLog.setCheckState(self._getQtBoxStateValue(Log.logDockVisible()))
      
       self.dockWidget.visibilityChanged.connect(self._visibilityChanged)
       
       self.btnApply.clicked.connect(self._apply)
       self.btnAdd.clicked.connect(self._addBroker)

       logStates = int(Settings.get('logStates',Log.CRITICAL))
       
       self.logCritical.setCheckState(self._getQtBoxStateValue(logStates & Log.CRITICAL))
       self.logInfo.setCheckState(self._getQtBoxStateValue(logStates & Log.INFO))
       self.logWarn.setCheckState(self._getQtBoxStateValue(logStates & Log.WARN)) 
       self.logDebug.setCheckState(self._getQtBoxStateValue(logStates & Log.DEBUG)) 
 
#       self.logCritical.setCheckState(self._getQtBoxStateValue(Settings.get('logCritical',True)))
#       self.logWarn.setCheckState(self._getQtBoxStateValue(Settings.get('logWarn',False)))
#       self.logDebug.setCheckState(self._getQtBoxStateValue(Settings.get('logDebug',False)))
#       self.logInfo.setCheckState(self._getQtBoxStateValue(Settings.get('logInfo',False)))
       
       self._buildBrokerTable()

    def _showLog(self,state):
        logDock = self.iface.mainWindow().findChild(QtGui.QDockWidget, 'MessageLog')
        if state:
            logDock.show()
        else:
            logDock.hide()
    

    def _apply(self):
        logStates = 0
        if self.logCritical.checkState() ==  self._getQtBoxStateValue(True):
            logStates |= Log.CRITICAL

        if self.logWarn.checkState() ==  self._getQtBoxStateValue(True):
            logStates |= Log.WARN

        if self.logInfo.checkState() ==  self._getQtBoxStateValue(True):
            logStates |= Log.INFO

        if self.logDebug.checkState() ==  self._getQtBoxStateValue(True):
            logStates |= Log.DEBUG
            
        Log.setLogStates(logStates)


    def _buildBrokerTable(self):
        brokers = self._brokers.list()
        
        columns = ["Name","Edit","Delete"]
        tbl = self.tableBrokerList
        tbl.clear()

        tbl.setStyleSheet("font: 10pt \"System\";") 
        tbl.setRowCount(len(brokers))
        tbl.setColumnCount(len(columns))
        tbl.setColumnWidth(30,30) #?
        tbl.setHorizontalHeaderLabels(columns)
        tbl.verticalHeader().setVisible(True)
        tbl.horizontalHeader().setVisible(True)
        tbl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        tbl.setSelectionMode(QAbstractItemView.NoSelection)

        tbl.setShowGrid(True)

        row=0
        for broker in self._brokers.list():
            item = QtGui.QTableWidgetItem(0)
            item.setText(broker.name())
            item.setFlags(Qt.NoItemFlags)
           # item.setData(Qt.UserRole,broker)
            tbl.setItem(row,0,item)

            button = QtGui.QPushButton('Edit', self)
            button.clicked.connect(self._callback(broker,TelemetryLayer.UPDATE))
            tbl.setCellWidget(row,1,button)

            button = QtGui.QPushButton('Delete', self)
            button.clicked.connect(self._callback(broker,TelemetryLayer.DELETE))
            tbl.setCellWidget(row,2,button)
            row=row+1
    
    def _callback(self,param,action):
        if action == TelemetryLayer.UPDATE:
            return lambda: self._updateBroker(param)
        if action == TelemetryLayer.DELETE:
            return lambda: self._delBroker(param)
        return None

    def _updateBroker(self,broker):
        if self._brokerDlg != None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        self._brokerDlg = BrokerConfig(self,broker,False)
        self._brokerDlg.connectApply.clicked.connect(self._updateBrokerApply)
        self._brokerDlg.connectCancel.clicked.connect(self._addBrokerCancel)
        self.dockWidget.setFixedHeight(25) # paramterise
        #self.dockWidget.setMaximumHeight(25) # paramterise
        self.dockWidget.repaint()
        self.iface.addDockWidget( Qt.LeftDockWidgetArea, self._brokerDlg.dockWidget )

    def _updateBrokerApply(self):
        if not self._brokerDlg.validate():
            return
        self._brokerDlg.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height()) # paramterise
        broker = self._brokerDlg.getBroker()
        self._brokers.update(broker)
        self._brokers.sync(True)
        self._buildBrokerTable()
            

    def _delBroker(self,broker):
        self._brokers.delete(broker)
        self._brokers.sync()
        self._buildBrokerTable()

    def _addBroker(self):
        if self._brokerDlg != None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        broker = self._brokers.create()
        self._brokerDlg = BrokerConfig(self,broker,True)
        self._brokerDlg.connectApply.clicked.connect(self._addBrokerApply)
        self._brokerDlg.connectCancel.clicked.connect(self._addBrokerCancel)
        self.dockWidget.setFixedHeight(25) # paramterise
        #self.dockWidget.setMaximumHeight(25) # paramterise
        self.dockWidget.repaint()
        self.iface.addDockWidget( Qt.LeftDockWidgetArea, self._brokerDlg.dockWidget )
        
#        result = broker.exec_()
#        if result != 0:
#            Log.debug("Yay")
    
    def _addBrokerApply(self):
        if not self._brokerDlg.validate():
            self._brokers.load()
            return
        self._brokerDlg.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height()) # paramterise
        broker = self._brokerDlg.getBroker()
        self._brokers.update(broker)
        self._brokers.sync(True)
        self._buildBrokerTable()
        # update Table List

    def _addBrokerCancel(self):
        self._brokerDlg.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height()) # paramterise
        self._brokers.load()

    def _visibilityChanged(self,state):
        if not state:
            self.tearDown()

    def tearDown(self):
        if self.dockWidget ==None:
            return
        self.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height()) # paramterise
        if self._brokerDlg !=None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        