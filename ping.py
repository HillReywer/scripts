#!/usr/bin/python

import socket
import time

jenkins = 'localhost'
port = 8080
retry = 5
delay = 10
timeout = 3

def isOpen(jenkins, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((jenkins, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def checkHost(jenkins, port):
        ipup = False
        for i in range(retry):
                if isOpen(jenkins, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if checkHost(jenkins, port):
        print (jenkins + " is UP")