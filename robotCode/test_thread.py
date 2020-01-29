from threading import Timer, Thread, Event

class perpetualTimer():
    def __init__(self, t, function):
    	self.t=t
    	self.function = function
    	self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
	self.function()
	self.thread = Timer(self.t,self.handle_function)
	self.thread.start()

    def start(self):
	self.thread.start()

    def cancerl(self):
	self.thread.cancel()

def printer():
    print 'ipsem lorem'

t = perpetualTimer(0.1, printer)
t.start()
