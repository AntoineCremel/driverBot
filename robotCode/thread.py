from threading import Timer,Thread, Event

class Periodic_Thread():
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

    def cancel(self):
        self.thread.cancel()

