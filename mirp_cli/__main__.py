
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

from pprint import pprint

from __init__ import (
    __debug_level__, __home__, __default_dir__
)

from utils.debug import dprint, set_level

#from command_firmware import firmware
#from command_init import init
#from command_update import update
#from command_monitor import monitor
#from commands.command_list import clist
#from command_import import cimport

def test_styles():
    dprint("normal")
    dprint("success", eid=0)
    dprint("warning", eid=1)
    dprint("failure", eid=2)
    dprint("additional information\nthis can span many\nlines...", eid=3)

@click.command("config", help="""
Configuration-related utilities. Run `create` to make the configuration directory.
""")
@click.argument("action", type=click.Choice(["create"]))
def config(action):
    if action == "create":
        if check_config() == False:
            if create_config() == False:
                dprint("Error creating configuration directory!", eid=2)
            else:
                dprint("Successfully created configuration directory.", eid=0, level=0)

def create_config(nodes={}, config={}):
    dprint("Running create_config()")
    try:
        os.makedirs(__home__ + __default_dir__)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return False

    dprint("Checking whether nodes.json exists...")
    if not os.path.isfile(__home__ + __default_dir__ + "/nodes.json"):
        with open(__home__ + __default_dir__ + "/nodes.json", "w") as f:
            json.dump(nodes, f)
            dprint("nodes.json created!", eid=0)

    dprint("Checking whether config.json exists...")
    if not os.path.isfile(__home__ + __default_dir__ + "/config.json"):
        with open(__home__ + __default_dir__ + "/config.json", "w") as f:
            json.dump(config, f)
            dprint("config.json created!", eid=0)

    return True

def check_config():
    if not os.path.isdir(__home__ + __default_dir__):
        return False
    if not os.path.isfile(__home__ + __default_dir__ + "/nodes.json"):
        return False
    if not os.path.isfile(__home__ + __default_dir__ + "/config.json"):
        return False
    return True

@click.group(invoke_without_command=True)
@click.pass_context
@click.option("-v", "--verbose", help="Sets the debug level for the program.", count=True)
def cli(ctx, verbose):
    global __debug_level__
    __debug_level__ = verbose

    set_level(__debug_level__)

    if ctx.invoked_subcommand != "config":
        if check_config() == False:
            dprint("Configuration not found! Run `mirp_cli config create` to generate.", eid=2)

    if ctx.invoked_subcommand == None:
        dprint("No commands specified! Run with --help to list all the commands avaliable.",
               eid=1, level=0)

cli.add_command(config)

if __name__ == "__main__":
    cli()
