import sys
from threading import Thread

class mythread(Thread):
    def __init__(self, objet):
	Thread.__init__(self)
	self.objet = objet

    def run(self):
	i = 0
	while i < 20:
    	    print "Valure send", self.objet
	    i += 1

thread1 = mythread("1")
thread2 = mythread("2")

thread1.start()
thread2.start()
