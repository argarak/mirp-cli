
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

from os.path import expanduser

# Global variables/classes/functions...
__home__        = expanduser("~")
__debug_level__ = 0

class text_style:
    header  = '\033[95m'
    ok      = '\033[94m'
    success = '\033[92m'
    warn    = '\033[93m'
    fail    = '\033[91m'
    end     = '\033[0m'
    bold    = '\033[1m'
    uline   = '\033[4m'

# Variables for setup.py
__title__    = "mirp-cli"
__version__  = "0.1dev"
__packages__ = ["mirp-cli"]
__author__   = "argarak"
__license__  = "Apache 2.0 License"
__readme__   = "README.md"
