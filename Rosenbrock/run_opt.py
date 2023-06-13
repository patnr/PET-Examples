import glob
import shutil
from glob import glob
import numpy as np
import os

from popt.loop.optimize import Optimize
from simulator.simple_models import noSimulation
from input_output import read_config
from popt.update_schemes.enopt import EnOpt
from Plotting.plot_optim import plot_obj_func
from popt.cost_functions.rosenbrock import rosenbrock

np.random.seed(101122)


def main():
    # remove old results
    for f in glob("debug_analysis_step_*.npz"):
        os.remove(f)

    dimension = 100  # dimension of Rosenbrock function

    # select starting point
    startmean = np.array([-2]*dimension)
    np.savez('init_mean.npz', startmean)

    # read init file
    ko, kf = read_config.read_txt('init_optim.popt')

    ke = ko
    sim = noSimulation(kf)
    method = EnOpt(ko, ke, sim, rosenbrock)

    optimization = Optimize(method)
    optimization.run_loop()

    # Post-processing: enopt_plot
    plot_obj_func()

    # Display results
    state_initial = np.load('ini_state.npz', allow_pickle=True)
    state_final = np.load('opt_state.npz', allow_pickle=True)
    for f in state_initial.files:
        print('Initial ' + f + ' ' + str(state_initial[f]))
        print('Final ' + f + ' ' + str(state_final[f]))
        print('---------------')
    print('---------------')


if __name__ == '__main__':
    main()
