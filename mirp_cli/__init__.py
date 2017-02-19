from os.path import expanduser

# Global variables
__home__        = expanduser("~")
__debug_level__ = 1

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
