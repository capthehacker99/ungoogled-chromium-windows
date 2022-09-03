import random
from threading import Thread
import time

def keepAliveFunction():
    while True:
        time.sleep(10)
        print("KeepAlive: ", random.random())

keepAliveThread = Thread(target = keepAliveFunction)
keepAliveThread.daemon = True
keepAliveThread.start()
exec(open("build.py").read())
