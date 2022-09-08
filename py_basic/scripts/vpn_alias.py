#!/usr/bin/env python3

import sys
import os

print("""Poland VPN\n
-start\n
-stop\n""")

argall = []

while True:
    try:
        for arg in sys.argv:
            argall.append(arg)

        if argall[1] == "-start":
                os.system("sudo wg-quick up wg0")
                print("VPN Poland", argall[1], "NOW IP: **.**.199.24")
                break
        elif argall[1] == "-stop":
                os.system("sudo wg-quick down wg0")
                print("VPN Poland", argall[1])
                break
        else:
            print("Command does not exist")
            break
    except IndexError:
        print("You didn't enter anything")
