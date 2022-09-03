from threading import Thread, Event
import random
from time import sleep
# StoppableThread is from user Dolphin, from http://stackoverflow.com/questions/5849484/how-to-exit-a-multithreaded-program
class StoppableThread(Thread):  

    def __init__(self):
        Thread.__init__(self)
        self.stop_event = Event()        

    def stop(self):
        # set event to signal thread to terminate
        self.stop_event.set()
        # block calling thread until thread really has terminated
        self.join()

class IntervalTimer(StoppableThread):

    def __init__(self, interval, worker_func):
        super().__init__()
        self._interval = interval
        self._worker_func = worker_func

    def run(self):
        while not self.stop_event.is_set():
            self._worker_func()
            sleep(self._interval)

def keepAlive():
    print("KeepAlive: ", random.random())

keepAliveInterval = IntervalTimer(10,keepAlive)
keepAliveInterval.start()
os.system("python build.py")
keepAliveInterval.stop()
