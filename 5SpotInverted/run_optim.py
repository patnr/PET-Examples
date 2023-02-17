# import ip
import os
import glob
import shutil
import logging
from glob import glob
import numpy as np

from popt.loop.optimize import Optimize
from simulator.opm import flow
from input_output import read_config
from popt.update_schemes.enopt import EnOpt
from popt.cost_functions.npv import npv

from enopt_plot import plot_obj_func, plot_bhp

np.random.seed(101122)


def main():
    # Check if folder contains any En_ files, and remove them!
    for folder in glob('En_*'):
        try:
            if len(folder.split('_')) == 2:
                int(folder.split('_')[1])
                shutil.rmtree(folder)
        finally:
            pass

    ko, kf = read_config.read_txt('init.popt')
    ke = ko

    sim = flow(kf)
    method = EnOpt(ko, ke, sim, npv)

    optimization = Optimize(method)
    optimization.run_loop()

    # Post-processing: enopt_plot
    plot_obj_func()
    plot_bhp()


if __name__ == '__main__':
    main()
