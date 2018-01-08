#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:wzz

'''功能自动化测试-Selenium'''
from time import sleep
from selenium import webdriver


firefox = webdriver.Firefox()
firefoxget('https://login.anjuke.com/login/form?history=aHR0cHM6Ly9iZWlqaW5nLmFuanVrZS5jb20vP3BpPVBaLWJhaWR1LXBjLWFsbC1iaWFvdGk=')