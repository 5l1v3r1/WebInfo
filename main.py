#!/usr/lib/python3.6
# wrote by iwHh <3 iran-cyber.net
# =================================
# Import Modules

import os, time, sys, random
try:
    from colorama import Fore, Style, Back, Cursor
except ImportError:
    print("Installing Modules for you")
    time.sleep(4)
    if os.name == "nt":
        os.system("python -m pip install builtwith")
        print("Run me again")
        sys.exit(0)
    else:
        os.system("sudo pip3 install builtwith")
        print("Run me again")
        sys.exit(0)
try:
    import builtwith
except ImportError:
    print("Installing modules for you")
    time.sleep(4)
    if os.name == "nt":
        os.system("python -m pip install builtwith")
        print("Run me again")
        sys.exit(0)
    else:
        os.system("sudo pip3 install builtwith")
        print("Run me again")
        sys.exit(0)

class Icg(object):
    def __init__(self):
        self.r = Fore.RED
        self.b = Fore.BLUE
        self.g = Fore.GREEN
        self.w = Fore.WHITE
        self.y = Fore.YELLOW
        self.c = Fore.CYAN
        self.reset = Style.RESET_ALL
        self.bgc = Back.CYAN
        self.bgr = Back.RED
        try:
            self.target = sys.argv[1]
        except IndexError:
            self.clear()
            self.print_logo()
            print("{}{}Usage : python {} google.com {}".format(self.bgr, self.w, sys.argv[0],  self.reset))
            sys.exit()
        self.main()

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
            $$\      $$\   ICG     $$\       $$$$$$\            $$$$$$\           
            $$ | $\  $$ |          $$ |      \_$$  _|          $$  __$$\          
            $$ |$$$\ $$ | $$$$$$\  $$$$$$$\    $$ |  $$$$$$$\  $$ /  \__|$$$$$$\  
            $$ $$ $$\$$ |$$  __$$\ $$  __$$\   $$ |  $$  __$$\ $$$$\    $$  __$$\ 
            $$$$  _$$$$ |$$$$$$$$ |$$ |  $$ |  $$ |  $$ |  $$ |$$  _|   $$ /  $$ |
            $$$  / \$$$ |$$   ____|$$ |  $$ |  $$ |  $$ |  $$ |$$ |     $$ |  $$ |
            $$  /   \$$ |\$$$$$$$\ $$$$$$$  |$$$$$$\ $$ |  $$ |$$ |     \$$$$$$  |
            \__/     \__| \_______|\_______/ \______|\__|  \__|\__|      \______/ 
            iran-cyber.NeT                              Web Info v1.0
            Wrote by iwHh
            """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
    def main(self):
        self.clear()
        self.print_logo()
        print(Cursor.FORWARD(60) + Fore.CYAN + "Target -> " + Fore.WHITE + self.target)
        if self.target.startswith("http://"):
            self.target.replace("http://", "")
        elif self.target.startswith("https://"):
            self.target.replace("https://", "")
        self._r = builtwith.parse("http://" + self.target)
        if "web-servers" in self._r:
            print(self.c + "WebServer " + self.b + "~> ")
            for _ in self._r['web-servers']:
                print(self.g + _)
                time.sleep(0.05)
        if "font-scripts" in self._r:
            print(self.c + "Font Scripts " + self.b + "~> ")
            for _ in self._r['font-scripts']:
                print(self.g + _)
                time.sleep(0.05)
        if "tag-managers" in self._r:
            print(self.c + "Tag Managers " + self.b + "~> ")
            for _ in self._r['tag-managers']:
                print(self.g + _)
                time.sleep(0.05)
        if "cms" in self._r:
            print(self.c + "Cms " + self.b + "~> " + self.g + self._r['cms'][0])
            time.sleep(0.05)
        if "blogs" in self._r:
            print(self.c + "Blogs " + self.b + "~> ")
            for _ in self._r['blogs']:
                print(self.g + _)
                time.sleep(0.05)
        if "programming-languages" in self._r:
            print(self.c + "Programming Languages " + self.b + "~> ")
            for _ in self._r['programming-languages']:
                print(self.g + _)
                time.sleep(0.05)
        if "javascript-frameworks" in self._r:
            print(self.c + "JavaScript FrameWorks" + self.b + "~> ")
            for _ in self._r['javascript-frameworks']:
                print(self.g + _)
                time.sleep(0.05)
        if "web-frameworks" in self._r:
            print(self.c + "Web FrameWorks " + self.b + "~> ")
            for _ in self._r['web-frameworks']:
                print(self.g + _)
                time.sleep(0.05)
        if "marketing-automation" in self._r:
            print(self.c + "Marketing AutoMation " + self.b + "~> ")
            for _ in self._r['marketing-automation']:
                print(self.g + _)
        if "video-players" in self._r:
            print(self.c + "Video Players " + self.b + "~> ")
            for _ in self._r['video-players']:
                print(self.g + _)
                time.sleep(0.05)
        if "cdn" in self._r:
            print(self.c + "Cdn " + self.b + "~> " + self.g + self._r['cdn'][0])


if __name__ == "__main__":
    run = Icg()
    
    #ENJOY
