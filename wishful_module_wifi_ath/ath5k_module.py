import logging
import random
import wishful_upis as upis
import wishful_agent as wishful_module
import wishful_module_wifi
import pickle
import os
from wishful_framework.classes import exceptions
import inspect
import subprocess
import zmq
import time
import platform
import numpy as np
import wishful_framework.upi_arg_classes.edca as edca #<----!!!!! Important to include it here; otherwise cannot be pickled!!!!
from atk_module import AthModule

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz, zubow}@tkn.tu-berlin.de"


@wishful_module.build_module
class Ath5kModule(AthModule):
    def __init__(self):
        super(Ath5kModule, self).__init__()
        self.log = logging.getLogger('Ath5kModule')