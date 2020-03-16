#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.17
author: wangxiaojie
'''

import os
import logging
import datetime

__all__ = [
    "Logger",
    "LOG_TYPE_ERROR",
    "LOG_TYPE_INFO",
    "LOG_TYPE_DEBUG"
    ]
LOG_TYPE_ERROR = logging.ERROR
LOG_TYPE_INFO = logging.INFO
LOG_TYPE_DEBUG = logging.DEBUG

class Logger(object):
    def __init__(self):
        self.logLevel = LOG_TYPE_DEBUG
        self.logName = "default"
        self.logPath = os.path.abspath(os.path.join(__file__, ".."))
        self.logFile = None
        self.logger = None 
        self.logHandler = None 
        self.printToConsole = False
        self.redirectLogFile = False
        self.logFormater = logging.Formatter('%%(asctime)s <%s(%s)> %%(levelname)s: %%(message)s' % (self.logName, os.getpid()))
    
    def flushLog(self):
        if not self.redirectLogFile:
            fileName = datetime.datetime.now().strftime("%Y%m%d.log")
            if self.logFile == fileName:
                return
            else:
                self.logFile = fileName
        self.logger = logging.getLogger(self.logName)
        if self.logHandler:
            self.logger.removeHandler(self.logHandler)
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        self.logHandler = logging.FileHandler(os.path.join(self.logPath, self.logFile), "a")
        #self.logHandler.setFormatter(logging.Formatter('<%s>  %%(levelname)s: %%(message)s' % self.logName))
        self.logHandler.setFormatter(self.logFormater)
        self.logger.addHandler(self.logHandler)
        self.logger.setLevel(self.logLevel)

    def openLog(self, name, level, path, file = None):
        self.logName = name
        self.logLevel = level
        self.logPath = path
        if file:
            self.logFile = file
            self.redirectLogFile = True
        else:
            self.redirectLogFile = False
        
        self.flushLog()

    def logDebug(self, msg, *args):
        if self.logger:
            self.flushLog()
            self.logger.debug(msg, *args)
            if self.printToConsole:
                print(msg % args)

    def logInfo(self, msg, *args):
        if self.logger:
            self.flushLog()
            self.logger.info(msg, *args)
            if self.printToConsole:
                print(msg % args)

    def logError(self, msg, *args):
        if self.logger:
            self.flushLog()
            self.logger.error(msg, *args)
            if self.printToConsole:
                print(msg % args)
    
    def setLogFormat(self, format):
        self.logFormater = logging.Formatter(format)

    def setPrintToConsole(self, isPrint):
        self.printToConsole = isPrint
            
if __name__ == "__main__":
    import time
    logger = Logger()
    logger.openLog("test", LOG_TYPE_DEBUG, ".")
    logger.setPrintToConsole(True)
    for i in range(10):
        logger.logDebug("hello %s, %s", "world", "debug man")
        logger.logInfo("hello %s, %s", "world", "info man")
        logger.logError("hello %s, %s", "world", "error man")
        time.sleep(20)
