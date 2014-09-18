# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tlBrokerConfig
 
 Configure individual Brokers
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import webbrowser

from ui_tlbrokerconfig import Ui_tlBrokerConfig
from tlbrokers import tlBrokers as Brokers
from lib.tlsettings import tlSettings as Settings, tlConstants
from lib.tllogging import tlLogging as Log
from tlmqttclient import *
from tltopicmanagerfactory import tlTopicManagerFactory as topicManagerFactory
import traceback, sys,os,imp, json


# Todo
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


class tlBrokerConfig(QtGui.QDialog, Ui_tlBrokerConfig):
    
    BrokerConfigTabId   = 0
    TopicManagerTabId   = 1
    
    def __init__(self,creator,broker,create=False):
        super(tlBrokerConfig, self).__init__()
    
        self._creator = creator
        self.plugin_dir = creator.plugin_dir
        self._iface = creator.iface
        self._create = create
        self._broker = broker
        self._topicManager = None
        self._tested = False
  
        self.setupUi()
 
    def setupUi(self):
       super(tlBrokerConfig,self).setupUi(self)

       if self._create == True:
           self._mode = tlConstants.Create
       else:
           self._mode = tlConstants.Update
    
       self.connectHelp.clicked.connect(self._help)
       self.connectTest.clicked.connect(self._test)
       
       self.connectName.setValidator(QRegExpValidator(QRegExp("^[a-zA-Z0-9\s]+"),self))
       self.connectHost.setValidator(QRegExpValidator(QRegExp("^[a-z0-9\.]+"),self))

       self.Tabs.setCurrentIndex(tlBrokerConfig.BrokerConfigTabId); # First index
       #if Modal create mode
       self.setName(self._broker.name())
       self.setHost(self._broker.host())
       self.setPort(str(self._broker.port()))
       self.setPoll(str(self._broker.poll()))
       self.setKeepAlive(str(self._broker.keepAlive()))
       self._topicManager = None
       
       self.connectApply.setEnabled(False)
       self.connectTopicManager.addItem("Please select ...",None)
       for topicManager in topicManagerFactory.getTopicManagers():
            self.connectTopicManager.addItem(topicManager['name'],topicManager['id'])
            
       if self._mode == tlConstants.Create: # Create Layer - so Modal
           self.connectPoll.setCurrentIndex(
           self.connectPoll.findText(Settings.get('mqttPoll',5)))
           self.connectApply.setText(_translate("tlBrokerConfig", "Create", None))
           self.connectApply.clicked.connect(self.accept)
           self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
           self.dockWidget.setWindowTitle(_translate("tlBrokerConfig", "Configure Broker", None))
        #   self.connectFarmSenseServer.setEnabled(False)
       elif self._mode == tlConstants.Update:

           self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
           self.dockWidget.setWindowTitle(_translate("tlBrokerConfig", "Configure Broker ", None) + self.getName())
           self.connectApply.setText(_translate("tlBrokerConfig", "Apply", None))
           if self._broker.topicManager() !=None:
            self.setTopicManager(self._broker.topicManager())
            if self._loadTopicManager(self.getTopicManager()):
                self.connectTopicManager.setEnabled(False)
       

    def _loadTopicManager(self,topicManagerId = 'digisense'):
        try:
            if self._create:
                self._broker.setTopicManager(topicManagerId)
            self._topicManager = topicManagerFactory.getTopicManager(self._broker,self._create)
            QObject.connect(self._topicManager,SIGNAL("topicManagerReady"),self._topicManagerLoaded)
            QObject.connect(self._topicManager,SIGNAL("topicManagerError"),self._topicManagerLoaded)
            self.Tabs.setTabEnabled(tlBrokerConfig.TopicManagerTabId,False)
            widget = self._topicManager.getWidget()
            self.Tabs.addTab(widget,"Topics")
            self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
            return True

        except Exception as e:
            Log.debug(e)
            
        
    def _topicManagerLoaded(self,state,obj):
        if state:
            self.Tabs.setTabEnabled(tlBrokerConfig.TopicManagerTabId,True)
            self.connectApply.setEnabled(True)
        else:
            Log.critical(obj)


    def getTopicManager(self):
        return self.connectTopicManager.itemData( self.connectTopicManager.currentIndex())

    def setTopicManager(self,tmid):
        tmidx = self.connectTopicManager.findData(tmid)
        if tmidx > 0:
            self.connectTopicManager.setCurrentIndex(tmidx)
        else:
            self.connectTopicManager.setCurrentIndex(0)
            

   
    def getTopics(self):
        if self._topicManager == None:
            return []
        return self._topicManager.getTopics()
            
   
    def getBroker(self):
            
        self._broker.setName(self.getName())
        self._broker.setHost(self.getHost())
        self._broker.setPort(self.getPort())
        self._broker.setPoll(self.getPoll())
        self._broker.setKeepAlive(self.getKeepAlive())
        self._broker.setTopics(self.getTopics())
        self._broker.setTopicManager(self.getTopicManager())
        return self._broker

    def getName(self):
        return self.connectName.text()
   
    def setName(self,name):
        self.connectName.setText(name)

    def getHost(self):
        return self.connectHost.text()

    def setHost(self,host):
        self.connectHost.setText(host)

    def getPort(self):
        if len(self.connectPort.text()) > 0:
           return int(self.connectPort.text())
        return None

    def setPort(self,port):
        self.connectPort.setText(str(port))

    def getKeepAlive(self,default = "0"):
        val = self.connectKeepAlive.itemText(self.connectKeepAlive.currentIndex())
        if val == None or not val.isdigit():
            val = default
        return int(val)

    def setKeepAlive(self,keepalive):
        idx = self.connectKeepAlive.findText(str(keepalive))
        if idx == None:
            idx = 0
        self.connectKeepAlive.setCurrentIndex(idx)

    def getPoll(self):
        return int(self.connectPoll.itemText(self.connectPoll.currentIndex())) * 1000

    def setPoll(self,interval):
        _interval = int(float(1.0/1000) * float(interval))
        self.connectPoll.setCurrentIndex(self.connectPoll.findText(str(_interval)))

    def getTested(self):
        return self._tested

    def setTested(self,state = True):
        self._tested = state
        if state and self._topicManager == None:
            if self._loadTopicManager(self.getTopicManager()):
                self.connectTopicManager.setEnabled(False)
        else:
            pass
            #self.Tabs.setTabEnabled(1,False)

            
        
    def validate(self):
        if len(self.getName()) == 0:
            Log.alert("Please supply a name for this broker")
            return False
    
        if self.getTopicManager() == None:
            Log.alert("Please specify a Broker Type (Topic Manager)")
            return False
        
        if not Brokers.instance().uniqName(self._broker.id(),self.getName()):
            Log.alert("A broker named " + self.getName() + " already exists")
            return False

        if len(self.getHost()) == 0:
            Log.alert("Please supply a hostname")
            return False

        if self.getPort() == None:
            Log.alert("Please specify a port")
            return False
        
        return True
        
    
    def _test(self):
        if not self.validate():
            return
        testClient = tlMqttTest(self,self.getHost(),self.getPort())
        self.connectTest.setEnabled(False)

        QObject.connect(testClient, QtCore.SIGNAL("mqttOnConnect"), self._connectSuccess)
        QObject.connect(testClient, QtCore.SIGNAL("mqttConnectionError"), self._connectError)
        QObject.connect(testClient, QtCore.SIGNAL("mqttOnTimeout"), self._connectError)

        Log.progressPush("Testing Connection")
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor));

        testClient.run()

    def _connectError(self,mqtt,msg = ""):
        self.connectTest.setEnabled(True)
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor));
        QObject.disconnect(mqtt, QtCore.SIGNAL("mqttOnConnect"), self._connectSuccess)
        QObject.disconnect(mqtt, QtCore.SIGNAL("mqttConnectionError"), self._connectError)
        Log.progressPop("Testing Connection")
        Log.progress(msg)
        Log.debug(msg)
        mqtt.kill()
        if self.getTested():
            self.setTested(False)

    def _connectSuccess(self,mqtt,obj, rc):
        self.connectTest.setEnabled(True)
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor));
        QObject.disconnect(mqtt, QtCore.SIGNAL("mqttOnConnect"), self._connectSuccess)
        QObject.disconnect(mqtt, QtCore.SIGNAL("mqttConnectionError"), self._connectError)
        Log.progressPop("Testing Connection")
        Log.progress("Connection successful!")
        mqtt.kill()
        self.setTested(True)

    def _help(self):
       webbrowser.open(Settings.getMeta('helpURL'))

    def _showLog(self,state):
        logDock = self._iface.mainWindow().findChild(QtGui.QDockWidget, 'MessageLog')
        if state:
            logDock.show()
        else:
            logDock.hide()


    def accept(self):
        print("accept")
        self.connectHelp.clicked.disconnect(self._help)
        self.connectTest.clicked.disconnect(self._test)
        super(tlBrokerConfig,self).accept()
        

    