
# -*- coding: utf-8 -*-

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

import glob
import click

from utils.debug import dprint

def scan_devices():
    device_list = glob.glob("/dev/tty{ACM,USB}*")
    if not device_list:
        dprint(("No devices found. Add -d [PATH] " 
                "to manually include the port "
                "path e.g. /dev/ttyACM0"), eid=2)
        exit()
        
    # Select first device found
    return device_list[0]

@click.command("monitor", help="""
Allows communication with devices connected via serial.
""")
@click.option("-d", "--device", default="auto", 
              help="Manually set device port if not automatically detected")
def monitor(device):
    if device == "auto":
        # Detect device
        device = scan_devices()
    dprint("Selected device under " + device + ".", level=1, eid=-1)