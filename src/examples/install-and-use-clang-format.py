import os
import subprocess

if __name__ == '__main__':
    print("[Install Clang-format]")

    cmd = "sudo apt install -y clang-format"
    completed_process = subprocess.run(
        cmd, stderr=subprocess.STDOUT, shell=True
    )
    print("--> completed_process:", completed_process)

# python3 install-and-use-clang-format.py

# clang-format -style=llvm -dump-config > .clang-format
# clang-format -i c/unsafe-type.c

# black -l 80 -S install-and-use-clang-format.py
