# -*- coding: utf-8 -*-
"""
 tlSettings
"""

from PyQt4.QtCore import QSettings, QObject
import os.path
from ConfigParser import ConfigParser

# set and get settings

# check Loglevel settings and restrict accordingly

class tlConstants:
    Create =0
    Update =1
    Deleted =2

class tlSettings(QObject):
    settings    = None
    metadata = ConfigParser()
    iface = None
    
    def __init__(self,creator):
        super(tlSettings,self).__init__()
        tlSettings.metadata.read(os.path.join( creator.plugin_dir,'metadata.txt'))
        tlSettings.set('plugin_dir',creator.plugin_dir)
        tlSettings._iface = creator.iface
        
    @staticmethod
    def getMeta(key,realm = 'general',default = ''):
        try:
            return tlSettings.metadata.get(realm,key)
        except:
            return None

    @staticmethod
    def get(key,default =''):
        if tlSettings.settings == None:
            tlSettings.settings =  QSettings(QSettings.NativeFormat, QSettings.UserScope, 'QuantumGIS', 'TelemetryLayer')
        result = tlSettings.settings.value(key)
        if result == None:
            return str(default)
        else:
            return str(result);

    @staticmethod
    def set(key,val):
        if tlSettings.settings == None:
            tlSettings.settings =  QSettings(QSettings.NativeFormat, QSettings.UserScope, 'QuantumGIS', 'TelemetryLayer')
        tlSettings.settings.setValue(key,str(val));


    @staticmethod
    def getIface():
        return tlSettings.iface