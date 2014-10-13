# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tLayerConfig

 New Layer Dialog

 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from ui_tlayerconfig import Ui_tLayerConfig
from tlbrokers import tlBrokers as Brokers
from lib.tlsettings import tlSettings as Settings
from lib.tllogging import tlLogging as Log



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


class tLayerConfig(QtGui.QDialog, Ui_tLayerConfig):
    
    def __init__(self,creator):
        super(tLayerConfig, self).__init__()
    
        self._iface = creator._iface
        self._brokers = Brokers.instance().list()
        self.setupUi()
        self.selectBroker.currentIndexChanged.connect(self._brokerChanged)
        self.selectTopicType.currentIndexChanged.connect(self._topicTypeChanged)

 
    def setupUi(self):
        super(tLayerConfig,self).setupUi(self)

        self.selectBroker.addItem("Select Broker ...",None)
            
        for broker in self._brokers:
            self.selectBroker.addItem(broker.name(),broker)
        self._brokerChanged(0)    
        self.buttonCreate.clicked.connect(self.accept)    
        self.buttonCancel.clicked.connect(self.reject)    
       
        #Note: tLayerConfig - add code to get currently selected broker")
        return
              
    def _brokerChanged(self,idx):
        self.selectTopicType.clear()
        broker = self.selectBroker.itemData(idx)
        if broker == None:
            self.selectTopicType.setEnabled(False)
            return
        for ttype in broker.uniqTopicTypes():
            self.selectTopicType.addItem(ttype)
        self.selectTopicType.setEnabled(True)
            
    def _topicTypeChanged(self,idx):
        self.buttonCreate.setEnabled(idx >=0)
        
    def getBroker(self):
        return self.selectBroker.itemData(self.selectBroker.currentIndex())

    def getTopicType(self):
        return self.selectTopicType.itemText(self.selectTopicType.currentIndex())


    def accept(self):
        super(tLayerConfig,self).accept()
        

    
