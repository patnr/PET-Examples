import glob
import shutil
from glob import glob
import numpy as np

from popt.loop.optimize import Optimize
from simulator.simple_models import rosen, noSimulation
from input_output import read_config
from popt.update_schemes.enopt import EnOpt
from Plotting.plot_optim import plot_obj_func

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

    ko, kf = read_config.read_txt('init_optim.popt')
    ke = ko

    if 0:  # use rosen class
        sim = rosen(kf)

        def sign_swap(pred_data, *args):
            values = []
            for v in pred_data[0]['value'][0]:
                values.append(-v)
            return values

        method = EnOpt(ko, ke, sim, sign_swap)
    else:  # use noSimulation class
        sim = noSimulation(kf)

        def rosenbr(state, *args):
            """
            Rosenbrock with negative sign (since we want to find the minimum)
            http://en.wikipedia.org/wiki/Rosenbrock_function
            """
            x = state[0]['vector']
            x0 = x[:-1]
            x1 = x[1:]
            ans = sum((1 - x0) ** 2) + 100 * sum((x1 - x0 ** 2) ** 2)
            return [-i for i in ans]

        method = EnOpt(ko, ke, sim, rosenbr)

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
