import os
import sys
import subprocess

mysymbols = {0: "", 1: "[*]", 2: "[-]", 3: "[+]"}


def myprint(title, level=0):
    print("{} {}".format(mysymbols.get(level), title))


def myrun(cmd):
    completed_process = subprocess.run(cmd, shell=True)
    # myprint("completed_process:", completed_process)


def compile_2_run():
    myprint("Remove", 2)
    cmd = " ".join(["rm", TARGET])
    myrun(cmd)

    myprint("Compile", 2)
    cmd = " ".join([CC, "-o", TARGET, SOURCE, "$(python3-config --libs)"])
    myprint("cmd:" + cmd)
    myrun(cmd)

    myprint("Run", 2)
    myrun(TARGET)


if __name__ == '__main__':
    myprint("main", 1)
    compiles = {"c": "gcc", "cpp": "g++"}

    SOURCE = sys.argv[1]
    TARGET = "./xy"
    CC = compiles.get(SOURCE.split('.')[1])

    compile_2_run()

# python3 compile-and-run-c-or-cpp.py c/unsafe-type.c
# python3 compile-and-run-c-or-cpp.py cpp/unsafe-type.cpp

# cmd: gcc -o xy c/unsafe-type.c
# black -l 80 -S compile-and-run-c-or-cpp.py
