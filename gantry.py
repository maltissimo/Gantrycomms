#!/bin/zsh

def auto_imports():
    exec(open("global_imports.py").read())
    return()

test = auto_imports()

test.exec()
