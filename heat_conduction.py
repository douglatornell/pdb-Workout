"""Heat conduction in a rod (i.e. 1-d diffusion over time)

Example code for 10Sep2015 EOAS SWC Workout on Debugging and pdb
"""
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Diffusion coefficient
    kappa = 0.01

    # 1-d spatial grid
    x_max = 100
    x_max_p1 = x_max + 1
    mid = x_max_p1 / 2

    # Time domain
    max_time = 10
    timesteps = 50
    dt = max_time / timesteps

    # Initialize temperature
    temp = np.zeros(x_max_p1)
    dtemp = np.zeros_like(temp)
    temp[mid] = 1.

    for time in np.linspace(0, max_time, timesteps):
        # Boundary conditions
        temp[1] = 0
        temp[x_max_p1] = 0
        for i in range(x_max_p1):
            dtemp[i] = kappa * (temp[i-1] - 2*temp[i] + temp[i+1])/dt ** 2
        temp = temp + dtemp
    plot_temp_distribution(temp, time)


def plot_temp_distribution(temp, time):
    fig, ax = plt.subplots(1, 1, figsize=(16, 2))
    ax.plot(temp)
    ax.set_xlabel('x')
    ax.set_ylabel('temp')
    ax.set_title('temp distribution at time = {}'.format(time))
    return fig


if __name__ == '__main__':
    main()
