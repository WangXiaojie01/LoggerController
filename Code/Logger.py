#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
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
PRINT_CONSOLE=True

class Logger(object):
    def __init__(self):
        self.logLevel = LOG_TYPE_DEBUG
        self.logName = ""
        self.logPath = ""
        self.logFile = ""
        self.logger = None 
        self.logHandler = None 
        self.printToConsole = False

    def setPrintToConsole(self, isPrint):
        self.printToConsole = isPrint
    
    def flushLog(self):
        fileName = datetime.datetime.now().strftime("%Y%m%d.log")
        if self.logFile == fileName:
            return
        self.logFile = fileName
        self.logger = logging.getLogger(self.logName)
        if self.logHandler:
            self.logger.removeHandler(self.logHandler)
        self.logHandler = logging.FileHandler(os.path.join(self.logPath, self.logFile), "a")
        self.logHandler.setFormatter(logging.Formatter('%%(asctime)s <%s(%s)> %%(levelname)s: %%(message)s' % (self.logName, os.getpid())))
        self.logger.addHandler(self.logHandler)
        self.logger.setLevel(self.logLevel)

    def openLog(self, name, level, path):
        self.logName = name
        self.logLevel = level
        self.logPath = path
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

    def debug(self, scriptName, className, funcName, msg, *args):
        self.logDebug("Script-[%s], Class-[%s], Func-[%s], Debug: " + msg, scriptName, className, funcName, *args)

    def info(self, scriptName, className, funcName, msg, *args):
        self.logInfo("Script-[%s], Class-[%s], Func-[%s], Info: " + msg, scriptName, className, funcName, *args)
 
    def error(self, scriptName, className, funcName, msg, *args):
        self.logError("Script-[%s], Class-[%s], Func-[%s], Error: " + msg, scriptName, className, funcName, *args)

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
