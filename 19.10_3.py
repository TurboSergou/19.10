import time

class CurrentTime:
    def curtime(func):
        def wrapper(self):
            print("********************")
            func(self)
            print("********************")

        return wrapper
    @curtime
    def mytime(self):
        dt = time.gmtime()
        print(dt.tm_hour +3,':',dt.tm_min)

dt = CurrentTime()
dt.mytime()