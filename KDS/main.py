#!/usr/bin/env python

import subprocess

def is_installed():
    # TODO: add checker code
    return True

def install():
    # TODO: add install code

def update():
    # TODO: add update code

def run():
    # TODO: add run code

if is_installed():
    update()
    run()
else:
    install()


# subprocess.call(["wget/bin/wget", "--no-check-certificate" "ScriptFile"])