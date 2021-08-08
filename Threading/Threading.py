import threading

def method_1():
    sum = 0
    for i in range(0,10000,2):
        sum += i

    return sum


def method_2():
    sum = 0
    for i in range(1,10000,2):
        sum += i
    sum += 1


thread_1 = threading.Thread(target=method_1)
thread_2 = threading.Thread(target=method_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(thread_1, thread_2)
