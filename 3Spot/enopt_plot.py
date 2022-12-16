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

    mm = []
    for iter in range(num_iter):
        info = np.load(str(path_to_files) + '/debug_analysis_step_{}.npz'.format(iter))
        mm.append(info['obj_func_values'])

    f = plt.figure()
    plt.plot(mm,'bs-')
    plt.xticks(range(num_iter))
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.xlabel('Iteration no.', size=20)
    plt.ylabel('NPV', size=20)
    plt.title('Objective function', size=20)
    f.tight_layout(pad=2.0)
    plt.savefig(str(path_to_figures) + '/obj_func')
    plt.show()


if __name__ == "__main__":
    plot_obj_func()
