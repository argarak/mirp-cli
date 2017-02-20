
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

import sys
from utils import text_style

__debug_level__ = 0

def set_level(level):
    global __debug_level__
    __debug_level__ = level

def dprint(*objects, level=1, eid=-1, sep=' ', end='\n', file=sys.stdout, flush=False):
    def replace_newline(items, style):
        for i in items:
            if type(i).__name__ == "str":
                i.replace("\n", style + "\t")
                print(i.replace("\n", "\n" + style + "\t"), sep=sep, end=end,
                      file=file, flush=flush)

    if eid == 2 or eid == 3:
        level = 0

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
            print(text_style.end)
            return
        print(*objects, sep=sep, end=end, file=file, flush=flush)
        print(text_style.end, end="")
