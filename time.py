import time
print(time.ctime(time.time()))
to= time.localtime()
print(to)
lt=time.strftime("%B %d %Y %H:%M:%S",to)
print(lt)