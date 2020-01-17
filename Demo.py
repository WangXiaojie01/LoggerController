#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.17
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from LogController import LogController
from Logger import *

if __name__ == "__main__":
    logRoot = os.path.abspath(os.path.join(__file__, "../log")) #指定日志存放的根路径
    logController = LogController(logRoot) #使用根目录初始化日志控制器
    logController.addLogger("socket", LOG_TYPE_DEBUG) #添加一个名为socket的日志控制类，记录DEBUG级别以上的日志
    SocketLogger = logController.getLogger("socket")  #获取socket的日志控制类
    logController.addLogger("monitor", LOG_TYPE_ERROR) #添加一个名为monitor的日志控制类，记录Error级别以上的日志
    MonitorLogger = logController.getLogger("monitor")  #获取monitor的日志控制类
    SocketLogger.logDebug("hello socket %s, %s", "world", "debug man") #SocketLogger输出Debug日志
    SocketLogger.logInfo("hello socket %s, %s", "world", "info man")  #SocketLogger输出info日志
    SocketLogger.logError("hello socket %s, %s", "world", "error man")   #SocketLogger输出error日志
    MonitorLogger.logDebug("hello monitor %s, %s", "world", "debug man") #MonitorLogger输出Debug日志
    MonitorLogger.logInfo("hello monitor %s, %s", "world", "info man")  #MonitorLogger输出info日志
    MonitorLogger.logError("hello monitor %s, %s", "world", "error man")   #MonitorLogger输出error日志
    #可以看到在logRoot下会有两个文件夹，monitor记录了只有Error的日志，Socket记录了Debug、Info、Error的日志

    #此时,Console不会输出任何日志,试着调用
    logController.setPrintToConsole(True)
    SocketLogger.logDebug("hello socket %s, %s", "world", "debug man") #SocketLogger输出Debug日志
    SocketLogger.logInfo("hello socket %s, %s", "world", "info man")  #SocketLogger输出info日志
    SocketLogger.logError("hello socket %s, %s", "world", "error man")   #SocketLogger输出error日志
    MonitorLogger.logDebug("hello monitor %s, %s", "world", "debug man") #MonitorLogger输出Debug日志
    MonitorLogger.logInfo("hello monitor %s, %s", "world", "info man")  #MonitorLogger输出info日志
    MonitorLogger.logError("hello monitor %s, %s", "world", "error man")   #MonitorLogger输出error日志

    #还可以设置某个日志控制类输出到Console，某个不输出到Console
    SocketLogger.setPrintToConsole(False)
    SocketLogger.logDebug("hello socket %s, %s", "world", "debug man") #SocketLogger输出Debug日志
    SocketLogger.logInfo("hello socket %s, %s", "world", "info man")  #SocketLogger输出info日志
    SocketLogger.logError("hello socket %s, %s", "world", "error man")   #SocketLogger输出error日志
    MonitorLogger.logDebug("hello monitor %s, %s", "world", "debug man") #MonitorLogger输出Debug日志
    MonitorLogger.logInfo("hello monitor %s, %s", "world", "info man")  #MonitorLogger输出info日志
    MonitorLogger.logError("hello monitor %s, %s", "world", "error man")   #MonitorLogger输出error日志
    