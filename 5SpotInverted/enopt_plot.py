# External imports
import matplotlib.pyplot as plt  # Plot functions
import numpy as np  # Numerical toolbox
import os


def plot_obj_func():
    """
    Plot the objective function vs. iterations.
    """

    # Collect all results
    path_to_files = './'
    path_to_figures = './Figures'  # Save here
    if not os.path.exists(path_to_figures):
        os.mkdir(path_to_figures)
    files = os.listdir(path_to_files)
    results = [name for name in files if "debug_analysis_step" in name]
    num_iter = len(results)

    obj = []
    for it in range(num_iter):
        info = np.load(str(path_to_files) + '/debug_analysis_step_{}.npz'.format(it), allow_pickle=True)
        obj.append(info['obj_func_values'])
    obj = np.array(obj)

    f, ax = plt.subplots(1, 1, figsize=(10, 10))
    if obj.ndim > 1:  # multiple models
        if np.min(obj.shape) == 1:
            ax.plot(obj, '.b')
        else:
            ax.plot(obj, 'b:')
        obj = np.mean(obj, axis=1)
    ax.plot(obj, 'rs-', linewidth=4, markersize=10)
    ax.set_xticks(range(num_iter))
    ax.tick_params(labelsize=16)
    ax.set_xlabel('Iteration no.', size=20)
    ax.set_ylabel('NPV', size=20)
    ax.set_title('Objective function', size=20)

    f.savefig(str(path_to_figures) + '/obj')
    f.show()


def plot_bhp():
    """
    Plot the final bottom hole pressures.
    """

    # Collect all results
    path_to_figures = './Figures'  # Save here
    if not os.path.exists(path_to_figures):
        os.mkdir(path_to_figures)

    injbhp = np.load('opt_state.npz', allow_pickle=True)['arr_0'][()]['injbhp']

    f, ax = plt.subplots(2, 2, figsize=(20, 10))
    ax = ax.flatten()
    for w in np.arange(4):
        bhp = injbhp[np.arange(w, len(injbhp), 4)]
        ax[w].step(bhp, '-')
        ax[w].tick_params(labelsize=16)
        ax[w].set_xlabel('Month', size=18)
        ax[w].set_ylabel('State', size=18)
        ax[w].set_title('BHP for injector ' + str(int(w+1)), size=18)

    f.tight_layout()
    f.savefig(str(path_to_figures) + '/bhp')
    f.show()

