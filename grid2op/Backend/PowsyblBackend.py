
import os  # load the python os default module
import sys  # laod the python sys default module
import copy
import warnings

import numpy as np
import pandas as pd

import pypowsybl as pp
import scipy

from grid2op.dtypes import dt_int, dt_float, dt_bool
from grid2op.Backend.Backend import Backend
from grid2op.Action import BaseAction
from grid2op.Exceptions import *

try:
    import numba

    numba_ = True
except (ImportError, ModuleNotFoundError):
    numba_ = False
    warnings.warn(
        "Numba cannot be loaded. You will gain possibly massive speed if installing it by "
        "\n\t{} -m pip install numba\n".format(sys.executable)
    )


class PowsyblBackend(Backend):

    def __init__(
            self,
            detailed_infos_for_cascading_failures=False,
            can_be_copied=True
    ):
        Backend.__init__(
            self,
            detailed_infos_for_cascading_failures=detailed_infos_for_cascading_failures,
            can_be_copied=can_be_copied
        ):


    def load_grid(self, path, filename=None):
        pass

    def apply_action(self, action):
        pass

    def runpf(self, is_dc=False):
        pass

    def get_topo_vect(self):
        pass

    def generators_info(self):
        pass

    def loads_info(self):
        pass

    def lines_or_info(self):
        pass

    def lines_ex_info(self):
        pass

    def get_theta(self):
        pass



