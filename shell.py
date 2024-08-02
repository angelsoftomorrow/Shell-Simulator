# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:34:03 2023

@author: Angel
"""
import sys
import os
import re

    
def cd_exec(path):
    try:
        os.chdir(path)
    except Exception:
        print("cd: No such file or directory")
 
def execute(cmd):
    fork = os.fork()
    if fork == 0:
        line = cmd.split()
        for dir in re.split(":", os.environ['PATH']):
            command = "%s/%s" % (dir, line[0])
            try:
                os.execve(command, line, os.environ)
            except:
                continue
        os.write(0, ("-shell.py: " + line[0] + ": command not found\n").encode())
        sys.exit(0)
    elif fork > 0:
        os.wait()
    else:
        print("fork failed")

def amp(cmd):
    fork = os.fork()
    if fork == 0:
        execute(cmd)
    elif fork > 0:
        pass
    else:
        print("Task failed")
               
def main():
    while True:
        cmd = input("$ ")
        
        if cmd == "quit":
            sys.exit(0)
        elif cmd.split()[0] == "cd":
            cd_exec(cmd.split()[-1])
        elif cmd[0] == "#":
            continue
        elif cmd[-1] == "&":
            cmd1 = cmd.split()[:-1]
            cmd2 = " ".join(cmd1)
            amp(cmd2)
        else:
            execute(cmd)
        
        
if __name__ == "__main__":
    main()