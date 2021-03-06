# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Telemetry Layer
                                 A QGIS plugin
 Interface to Telemetry Layer sensor network
                             -------------------
        begin                : 2014-05-30
        copyright            : (C) 2014 by Andrew McClure
        email                : andrew@agsense.co.nz
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

from forms.ui_telemetrylayer import Ui_TelemetryLayer
from tlbrokers import tlBrokers as Brokers, BrokerNotSynced, BrokerNotFound
from tlbrokerconfig import tlBrokerConfig as BrokerConfig
from lib.tlsettings import tlSettings as Settings, tlConstants as Constants
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
    """
    Class to provide the intial settings dialog - interface to broker management etc.
    
    Note - QGIS names all classes as TelemetryLayer.xxx[.xxx] so this becomes: TelemetryLayer.TelemetryLayer
    """

    _this = None
    
    kBrokerSettingsTabId = 0
    kBrokerListTabId = 1

    ## Nathan - Avoid static methods if you can. Just put it outside the class'
    @staticmethod
    def _getQtBoxStateValue(state):
        if eval(str(state)):
            return Qt.Checked
        else:
            return Qt.Unchecked

    def __init__(self, creator):
        super(TelemetryLayer, self).__init__()

        self.iface = creator.iface
        self.plugin_dir = creator.plugin_dir
        self._brokerDlg = None
        # Nathan - Avoid call to instance.  Just make a Brokers instance and keep in
        # self._brokers like a normal variable
        self._brokers = Brokers.instance()
        self._layerManager = creator.layerManager
        self._setup = False
        self.dockWidget = None
        # Nathan - Remove the instance() method you don't need this here.
        TelemetryLayer._this = self

        #Nathan = This can be done like the following:
        #self._brokers.brokersLoaded.connect(self.brokersLoaded)
        self._brokers.brokersLoaded.connect(lambda: self.brokersLoaded())    
        # Nathan - Don't need pass at the end
        pass

    # Nathan - Avoid this pattern. It's not bad but you don't need it and is confusing.
    # Just store a variable on the
    # calling end and reference it like normal
    @staticmethod
    def instance():
        return TelemetryLayer._this

    def show(self, broker=None):
        if not self._setup:
            self.setupUi()
            self._setup = True

        if not self.dockWidget.isVisible():
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.dockWidget.setVisible(True)

        if broker is not None:
            # if self._brokerDlg.dockWidget.isVisible():
            #                self._brokerDlg.dockWidget.setVisible(False)
            # Add check to see if _brokerDlg is currently open and a prompt to change it if dirty!
            self._updateBroker(broker, True)


    def hide(self):
        if self.dockWidget.isVisible():
            self.dockWidget.setVisible(False)

    def brokersLoaded(self):
        if self.dockWidget and self.dockWidget.isVisible():
            self._buildBrokerTable()
            
    def setupUi(self):
        super(TelemetryLayer, self).setupUi(self)
        self.dockWidget.setFixedHeight(self.height())  # paramterise
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.dockWidget.setWindowTitle(_translate("tlBrokerConfig", "Configure Telemetry Layer", None))
        self.ckShowLog.clicked.connect(self._showLog)

        # Nathan - Use setChecked(bool) to make it easier
        self.ckShowLog.setCheckState(self._getQtBoxStateValue(Log.logDockVisible()))

        self.dockWidget.visibilityChanged.connect(self._visibilityChanged)

        self.btnApply.clicked.connect(self._apply)
        self.btnAdd.clicked.connect(self._addBroker)

        logStates = int(Settings.get('logStates', Log.CRITICAL))

        # Nathan - The checked state conversion isn't needed
        # Just call setChecked(bool)
        # Also consider using a QButtonGroup here in order to have only one button pressed at a time.
        self.logCritical.setCheckState(self._getQtBoxStateValue(logStates & Log.CRITICAL))
        self.logInfo.setCheckState(self._getQtBoxStateValue(logStates & Log.INFO))
        self.logWarn.setCheckState(self._getQtBoxStateValue(logStates & Log.WARN))
        self.logDebug.setCheckState(self._getQtBoxStateValue(logStates & Log.DEBUG))
        self.logStatus.setCheckState(self._getQtBoxStateValue(logStates & Log.STATUS))
        self.brokerManagerWidget.setCurrentIndex(self.kBrokerListTabId)
        self._buildBrokerTable()

    def checkBrokerConfig(self):
        # Nathan - Can be done like this:
        # if not self._brokers.list():
        # (if not will check for the empty list)
        if len(self._brokers.list()) == 0:
            raise BrokersNotDefined

        if self.dirty():
            if Log.confirm("You have unsaved changed in your broker configuration. Save now?"):
                self.apply()
            else:
                raise BrokerNotSynced("Unsaved changes")


    def _showLog(self, state):
        logDock = self.iface.mainWindow().findChild(QtGui.QDockWidget, 'MessageLog')
        if state:
            logDock.show()
        else:
            logDock.hide()


    def _apply(self):
        logStates = 0
        if self.logCritical.checkState() == self._getQtBoxStateValue(True):
            logStates |= Log.CRITICAL

        if self.logWarn.checkState() == self._getQtBoxStateValue(True):
            logStates |= Log.WARN

        if self.logInfo.checkState() == self._getQtBoxStateValue(True):
            logStates |= Log.INFO

        if self.logDebug.checkState() == self._getQtBoxStateValue(True):
            logStates |= Log.DEBUG

        if self.logStatus.checkState() == self._getQtBoxStateValue(True):
            logStates |= Log.STATUS

        Log.setLogStates(logStates)

    def _buildBrokerTable(self):
        brokers = self._brokers.list()

        columns = ["Name", "Edit", "Delete"]
        tbl = self.tableBrokerList
        tbl.clear()

        tbl.setStyleSheet("font: 10pt \"System\";")
        tbl.setRowCount(len(brokers))
        tbl.setColumnCount(len(columns))
        tbl.setColumnWidth(30, 30)  # ?
        tbl.setHorizontalHeaderLabels(columns)
        tbl.verticalHeader().setVisible(True)
        tbl.horizontalHeader().setVisible(True)
        tbl.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        tbl.setSelectionMode(QAbstractItemView.NoSelection)

        tbl.setShowGrid(True)

        # Nathan - Remove this
        row = 0
        # Nathan - Use:
        # for row, broker in enumerate(self._brokers.list()):
        for broker in self._brokers.list():
            item = QtGui.QTableWidgetItem(0)
            item.setText(broker.name())
            item.setFlags(Qt.NoItemFlags)
            # item.setData(Qt.UserRole,broker)
            tbl.setItem(row, 0, item)

            button = QtGui.QPushButton('Edit', self)
            button.clicked.connect(self._callback(broker, Constants.Update))
            tbl.setCellWidget(row, 1, button)

            button = QtGui.QPushButton('Delete', self)
            button.clicked.connect(self._callback(broker, Constants.Deleted))
            tbl.setCellWidget(row, 2, button)
            # Nathan - Not needed when using enumerate
            row += 1

    def _callback(self, param, action):
        if action == Constants.Update:
            return lambda: self._updateBroker(param)
        if action == Constants.Deleted:
            return lambda: self._delBroker(param)
        return None

    def _updateBroker(self, broker, groupClicked=False):
        
        if self._brokerDlg is not None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        Log.debug("Update broker")
        self._brokerDlg = BrokerConfig(self, broker, False)
        self._brokerDlg.connectApply.clicked.connect(self._updateBrokerApply)
        self._brokerDlg.connectClose.clicked.connect(self._updateBrokerClose)
        self.dockWidget.setFixedHeight(25)  # paramterise
        # self.dockWidget.setMaximumHeight(25) # paramterise
        if groupClicked:
            self._brokerDlg.Tabs.setCurrentIndex(self._brokerDlg.kBrokerConfigTabId) # was .kFeatureListTabId
        self.dockWidget.repaint()
        self.iface.addDockWidget(Qt.LeftDockWidgetArea, self._brokerDlg.dockWidget)

    def dirty(self):
        return self._brokerDlg is not None and self._brokerDlg.isVisible() and self._brokerDlg.dirty()

    def apply(self):
        self._apply()
        if self._brokerDlg is None:
            return

            if self._brokerDlg.mode() == Constants.Create:
            self._addBrokerApply()
        elif self._brokerDlg.mode() == Constants.Update:
            self._updateBrokerApply()


    def _updateBrokerApply(self):
        if not self._brokerDlg.validate():
            return
        Log.debug("_updateBrokerApply")
        broker = self._brokerDlg.getBroker()
        #for key, val in broker.properties().iteritems():
        #    Log.debug(key + " " + str(val))
        self._brokers.update(broker)
        self._brokers.sync(True)
        broker.setDirty(False)
        self._brokerDlg.connectApply.setEnabled(False)
        Log.progress("Broker updated")
       
        #self._brokerDlg.dockWidget.setVisible(False)
        #self.dockWidget.setFixedHeight(self.height())  # paramterise
        #broker = self._brokerDlg.getBroker()
        #self._brokers.update(broker)
        #self._brokers.sync(True)
        #self._buildBrokerTable()


    def _delBroker(self, broker):
        if self._layerManager.brokerInUse(broker.id()):
            Log.alert("A layer is currently using this broker. Please remove this first!")
            return

        if not Log.confirm("Are you sure you want to delete the broker " + broker.name() + "?"):
            return
        broker.deletingBroker.emit()
        self._brokers.delete(broker)
        self._brokers.sync()
        self._buildBrokerTable()

    def _addBroker(self):
        if self._brokerDlg is not None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        broker = self._brokers.create()
        self._brokerDlg = BrokerConfig(self, broker, True)
        self._brokerDlg.connectApply.clicked.connect(self._addBrokerApply)
        self._brokerDlg.connectClose.clicked.connect(self._updateBrokerClose)
        self.dockWidget.setFixedHeight(25)  # paramterise
        # self.dockWidget.setMaximumHeight(25) # paramterise
        self.dockWidget.repaint()
        self.iface.addDockWidget(Qt.LeftDockWidgetArea, self._brokerDlg.dockWidget)


    def _addBrokerApply(self):
        if not self._brokerDlg.validate():
            self._brokers.load()
            return
        self._brokerDlg.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height())  # paramterise
        broker = self._brokerDlg.getBroker()
        self._brokers.update(broker)
        self._brokers.sync(True)
        self._buildBrokerTable()
        Log.debug("Brokers reloaded")
        self._brokerDlg.connectApply.setEnabled(False)
        self.brokerManagerWidget.setCurrentIndex(self.kBrokerListTabId)
          
        # update Table List

    def _updateBrokerClose(self):
        broker = self._brokerDlg.getBroker()
        if broker.dirty():
            if not Log.confirm("You have unsaved changes. Close anyway?"):
                return
        self._brokerDlg.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height())  # paramterise
        self._brokers.load()
        self.brokerManagerWidget.setCurrentIndex(self.kBrokerListTabId)

    def _visibilityChanged(self, state):
        if not state:
            self.tearDown()

    def tearDown(self):
        if self.dockWidget is None:
            return
        self.dockWidget.setVisible(False)
        self.dockWidget.setFixedHeight(self.height())  # paramterise
        if self._brokerDlg is not None:
            self._brokerDlg.dockWidget.setVisible(False)
            self._brokerDlg = None
        
