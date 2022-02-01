from slovar import *
from colorama import Fore, Back, Style


def sprasevanje(prevod):
    r = 3
    while len(prevod) > 0:
        keys = [k for k, v in prevod.items()]
        for sp in keys:
            if sp == input(str(prevod[sp]) + ": "):
                print(Fore.GREEN + "bravo")
                print(Style.RESET_ALL)
                del prevod[sp]
            else:
                print(sp)
                for i in range(r):
                    input(str(i + 1) + ". "+ str(prevod[sp]) + ": ")
        if 0 < len(prevod):
            print(Fore.RED + "----------\n" + str(r - 2) + ". krog zaključen" + "\n----------")
            print(Style.RESET_ALL)
            r += 1
        else:
            print("ʕ•ᴥ•ʔ")



for se, n in seti.items():
    print(se, "-", n)
exec("sprasevanje(" + input("Set? ") + ")")

