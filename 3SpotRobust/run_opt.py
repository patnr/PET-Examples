# import ip
import os
import glob
import shutil
import logging
from glob import glob
import numpy as np
import datetime as dt
import csv

from popt.loop.optimize import Optimize
from simulator.opm import flow
from input_output import read_config
from popt.update_schemes.enopt import EnOpt
from popt.cost_functions.npv import npv

from plot_optim import *

np.random.seed(270623)


def main():
    # Check if folder contains any En_ files, and remove them!
    for folder in glob('En_*'):
        try:
            if len(folder.split('_')) == 2:
                int(folder.split('_')[1])
                shutil.rmtree(folder)
        finally:
            pass

    # remove old results
    for f in glob("debug_analysis_step_*.npz"):
        os.remove(f)

    # Set initial state
    init_injbhp = 250.0 * np.ones(120)
    init_prodbhp = 150.0 * np.ones(60)
    np.savez('init_injbhp.npz', init_injbhp)
    np.savez('init_prodbhp.npz', init_prodbhp)

    # Set dates
    report_dates = []
    for index in range(60):
        report_dates.append(dt.datetime(2029, 1, 1) + dt.timedelta(30*(index+1)))
    with open('report_dates.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(list(report_dates))

    ko, kf = read_config.read_txt('init_optim_inj.popt')
    ke = ko

    sim = flow(kf)
    method = EnOpt(ko, ke, sim, npv)

    optimization = Optimize(method)
    optimization.run_loop()

    # Post-processing: enopt_plot
    plot_obj_func()
    plt.show()

    # Display results
    state_initial = np.load('ini_state.npz', allow_pickle=True)
    state_final = np.load('opt_state.npz', allow_pickle=True)
    for f in state_initial.files:
        print('Initial ' + f + ' ' + str(state_initial[f]))
        print('Final ' + f + ' ' + str(state_final[f]))
        print('---------------')


if __name__ == '__main__':
    main()
