import threading, time


def hel():
    print("Hello world")
    time.sleep(10)
    print(threading.current_thread().getName())
    print("fgh")


def wel():
    print("HI")
    time.sleep(10)
    print(threading.current_thread().getName())
    print("PRABHU")
    #print(threading.current_thread().getName())


t1 = threading.Thread(target=hel, name='thread1', daemon=True)
print("1***")
t1.start()
print("2***")
t2 = threading.Thread(target=wel, name='thread2')
print("3***")
t2.start()
print("4***")
