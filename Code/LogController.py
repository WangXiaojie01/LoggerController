#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
'''

import os
from Logger import *

__all__ = [
    "LogController"
    ]

class LogController(object):
    def __init__(self, logRoot):
        self.loggers = {}
        self.logRoot = logRoot
        self.isPrintToConsole = False
    
    def addLogger(self, name, level):
        if not name in self.loggers:
            path = os.path.abspath(os.path.join(self.logRoot, name))
            if not os.path.exists(path):
                os.makedirs(path)
            tempLogger = Logger()
            tempLogger.openLog(name, level, path)
            self.loggers[name] = tempLogger

    def getLogger(self, name):
        if name in self.loggers:
            return self.loggers[name]
        else:
            return None
    
    def setPrintToConsole(self, isPrint):
        self.isPrintToConsole = isPrint
        for logName in self.loggers:
            self.loggers[logName].setPrintToConsole(isPrint)

if __name__ == "__main__":
    import time

    LogRoot = os.path.abspath(os.path.join(__file__, "../log"))
    logController = LogController(LogRoot)
    logController.addLogger("socket", LOG_TYPE_DEBUG)
    logController.setPrintToConsole(True)
    SocketLogger = logController.getLogger("socket")
    for i in range(10):
        SocketLogger.logDebug("hello %s, %s", "world", "debug man")
        SocketLogger.logInfo("hello %s, %s", "world", "info man")
        SocketLogger.logError("hello %s, %s", "world", "error man")
        time.sleep(20)
