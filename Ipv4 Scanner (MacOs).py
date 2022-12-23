from threading import Thread
from termcolor import cprint
import pythonping, sys, os
print("ipv4 scanner by Andrew moran\n\nPlease enter the base ip\n(The first 3 sets of pairs)")
baseip = input()

Ping = pythonping.ping

os.system('color')

def ping(a):
    if "Reply from" in str(Ping(str(a),verbose=True,size=1,count=1,timeout=0.1)):
        os.system('clear')
        return(0)
    else:
        os.system('clear')
        return(1)

if baseip[-1] != ".":
    baseip = baseip+"."

class thread1(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(0, 17+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        a18 = ax[17]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(18,34+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread3(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(35,51+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread4(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(52,68+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread5(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(69,85+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread6(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(86,102+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread7(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(103,119+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread8(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(120,136+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread9(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(137,153+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread10(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(154,170+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread11(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(171,187+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread12(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(188,204+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread13(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(205,221+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread14(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(222,238+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

class thread15(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        ax = []
        for x in range(239,255+1):
            if ping(baseip+str(x)) == 0:
               a = baseip+str(x)+": Online", "green"
            else:
                a = baseip+str(x)+": Offline", "red"
            ax.append(a)
        a1 = ax[0]
        a2 = ax[1]
        a3 = ax[2]
        a4 = ax[3]
        a5 = ax[4]
        a6 = ax[5]
        a7 = ax[6]
        a8 = ax[7]
        a9 = ax[8]
        a10 = ax[9]
        a11 = ax[10]
        a12 = ax[11]
        a13 = ax[12]
        a14 = ax[13]
        a15 = ax[14]
        a16 = ax[15]
        a17 = ax[16]
        self.value = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17

Thread1 = thread1()
Thread2 = thread2()
Thread3 = thread3()
Thread4 = thread4()
Thread5 = thread5()
Thread6 = thread6()
Thread7 = thread7()
Thread8 = thread8()
Thread9 = thread9()
Thread10 = thread10()
Thread11 = thread11()
Thread12 = thread12()
Thread13 = thread13()
Thread14 = thread14()
Thread15 = thread15()

Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()
Thread5.start()
Thread6.start()
Thread7.start()
Thread8.start()
Thread9.start()
Thread10.start()
Thread11.start()
Thread12.start()
Thread13.start()
Thread14.start()
Thread15.start()

Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()
Thread5.join()
Thread6.join()
Thread7.join()
Thread8.join()
Thread9.join()
Thread10.join()
Thread11.join()
Thread12.join()
Thread13.join()
Thread14.join()
Thread15.join()

os.system('clear')
for x in range(0,16):
    a = Thread1.value[x]
    cprint(str(str(a).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(a).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    b = Thread2.value[x]
    cprint(str(str(b).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(b).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    c = Thread3.value[x]
    cprint(str(str(c).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(c).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    d = Thread4.value[x]
    cprint(str(str(d).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(d).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    e = Thread5.value[x]
    cprint(str(str(e).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(e).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    f = Thread6.value[x]
    cprint(str(str(f).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(f).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    g = Thread7.value[x]
    cprint(str(str(g).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(g).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    h = Thread8.value[x]
    cprint(str(str(h).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(h).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    i = Thread9.value[x]
    cprint(str(str(i).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(i).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    j = Thread10.value[x]
    cprint(str(str(j).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(j).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    k = Thread11.value[x]
    cprint(str(str(k).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(k).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    l = Thread12.value[x]
    cprint(str(str(l).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(l).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    m = Thread13.value[x]
    cprint(str(str(m).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(m).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    n = Thread14.value[x]
    cprint(str(str(n).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(n).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
for x in range(0,16):
    o = Thread15.value[x]
    cprint(str(str(o).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(o).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))

o = Thread15.value[16]
cprint(str(str(o).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[0]), str(str(o).replace("(",'').replace(")",'').replace("'",'').replace(' ','').replace(':', ': ').split(',')[1]))
    
