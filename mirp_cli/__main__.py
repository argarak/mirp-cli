
# Copyright 2017 Jakub Kukiełka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
import os
import sys
import json
import errno

from __init__ import (
    __debug_level__, __home__, text_style
)

#from commands import *

def dprint(*objects, level=1, eid=-1, sep=' ', end='\n', file=sys.stdout, flush=False):
    def replace_newline(items, style):
        for i in items:
            if type(i).__name__ == "str":
                i.replace("\n", style + "\t")
                print(i.replace("\n", "\n" + style + "\t"), sep=sep, end=end,
                      file=file, flush=flush)

    if __debug_level__ >= level:
        if eid == -1:
            print(text_style.normal, end="\t")
        elif eid == 0:
            print(text_style.success, end="\t")
        elif eid == 1:
            print(text_style.warn, end="\t")
        elif eid == 2:
            print(text_style.fail, end="\t")
        elif eid == 3:
            print("\n" + text_style.info, end="\t")
            replace_newline(objects, text_style.info)
            print("")
            return
        print(*objects, sep=sep, end=end, file=file, flush=flush)
        print(text_style.end, end="")

def test_styles():
    dprint("normal")
    dprint("success", eid=0)
    dprint("warning", eid=1)
    dprint("failure", eid=2)
    dprint("additional information\nthis can span many\nlines...", eid=3)

def create_config():
    dprint("Trying to create directory...")
    try:
        os.makedirs(__home__ + "/.mirp")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return False
    dprint("Success!")

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-v', '--verbose', count=True)
def cli(ctx, verbose):
    global __debug_level__
    __debug_level__ = verbose

    if create_config() == False:
        dprint("Config exists!")
    test_styles()

if __name__ == "__main__":
    cli()
