import platform
a = platform.machine()
b = platform.version()
c = platform.platform()
d = platform.uname()
f = platform.system()
g = platform.processor()
#Mohammad Hosseinzadeh
input_choise = input("please choise information!!::::::\nia= info Architecture/iv= info version/io= info os/ic= info core/ai= all info ")
if input_choise == "ia":
    def inf_arch(one):
        print("This system has Architecture:" + one)
    inf_arch(a)
elif input_choise == "iv":
    def inf_ver(two):
        print("This system has version:" + two)
    inf_ver(b)
elif input_choise == "io":
    def inf_os(Third):
        print("This system has Os:" + Third)
    inf_os(c)
elif input_choise == "ic":
    def inf_ic(Fourth):
        print("This system has Core:" + Fourth)
    inf_ic(g)
elif input_choise == "ai":
    def inf_ai(Fifth):
        print("This system has all information:" + str(Fifth))
    inf_ai(d)






