import gc, time, threading, multiprocessing

#lib = '123456789'
#lib = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`,./;'[]~!@#$%^&*()_+{}|:<>?"
global lib2
lib = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`,./;'[]~!@#$%^&*()_+{}|:<>? "


# global libc
# libc = "


def L3_gc():
    time1 = time.time()
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
                    gc.collect()
    time2 = time.time()
    time3 = time2 - time1
    print(time3)

def L3_gc_loop():
    print("L3_gc_Data\n")
    for i in range(10):
        L3_gc()

def L3_clean():
    time1 = time.time()
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
    time2 = time.time()
    time3 = time2 - time1
    print(time3)

def L3_clean_loop():
    print("L3_clean_Data\n")
    for i in range(10):
        L3_gc()

def L3_thread():
    time1 = time.time()
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
    time2 = time.time()
    time3 = time2 - time1
    print(time3)

def L3_thread_loop():
    print("L3_thread_data\n")
    for i in range(10):
        T1 = threading.Thread(target=L3_thread)
        T1.start()
        T1.join()

def L3_proc(lib):
    time1 = time.time()
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
    time2 = time.time()
    time3 = time2 - time1
    print(time3)

def mp_handler():
    p = multiprocessing.Pool(2)
    p.starmap(L3_proc(), lib)

def L3_proc_loop2():
    print("L3_proc_data_2\n")
    for i in range(10):
        if __name__ == '__main__':
            mp_handler()

def mp_handler2():
    p = multiprocessing.Pool(4)
    p.starmap(L3_proc(), lib)

def L3_proc_loop4():
    print("L3_proc_data_4\n")
    for i in range(10):
        if __name__ == '__main__':
            mp_handler2()

from numba import jit
@jit(nopython=False, parallel=True)
def L3_jit():
    time1 = time.time()
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
    time2 = time.time()
    time3 = time2 - time1
    print(time3)

def L3_jit_loop():
    print("L3_jit_data")
    for i in range(10):
        L3_jit()

#L3_gc_loop()
#L3_clean_loop()
#L3_thread_loop()
#L3_proc_loop2()
#L3_proc_loop4()
#L3_jit_loop()

T1 = threading.Thread(target=L3_thread)
T1.start()
T1.join()
