import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time1():
    print "Time 1: ", time.time()
    time.sleep(1)

def print_time2():
    print "Time 2: ", time.time()
    time.sleep(1)

s.enterabs(1,1, print_time2, ())

while True:
    s.run()
