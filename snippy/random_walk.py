import numpy as np
import matplotlib.pyplot as plt



def random_walk_2d(num_steps: int) -> float:
    """2-dimensional random walk.
    """
    pos = (0., 0.)
    for _ in range(num_steps):
        phi = np.random.uniform(0., 2. * np.pi)
        pos += (np.cos(phi), np.sin(phi))
    return pos


def random_walk_2d_fast(num_steps: int) -> float:
    """Vectorized 2-dimensional random walk.
    """
    phi = np.random.uniform(0., 2. * np.pi, num_steps)
    return (np.cos(phi).sum(), np.sin(phi).sum())


def plot_random_walk_2d(num_steps: int, step_size: float = 1.) -> float:
    """2-dimensional random walk.
    """
    x = [0.]
    y = [0.]
    for _ in range(num_steps):
        phi = np.random.uniform(0., 2. * np.pi)
        dx = step_size * np.cos(phi)
        dy = step_size * np.sin(phi)
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    plt.figure('Random Walk')
    plt.plot(x, y)
    plt.gca().set_aspect('equal')
    plt.xlabel('x [a.u.]')
    plt.ylabel('x [a.u.]')


def gauss(x, norm, mu, sigma):
    """Gaussian model.
    """
    return norm /  np.sqrt(2 * np.pi) / sigma * np.exp(-(x - mu)**2. / (2. * sigma**2.))


def expo(x, norm, mean):
    """Exponential model.
    """
    return norm / mean * np.exp(-x / mean)


def dmodel(x, norm, loc):
    """
    """
    return 2. * norm / loc * x * np.exp(-x**2. / loc)





if __name__ == '__main__':

    num_realizations = 10000
    num_steps = 100
    x = []
    y = []
    d = []
    d2 = []
    for _ in range(num_realizations):
        _x, _y = random_walk_2d_fast(num_steps)
        x.append(_x)
        y.append(_y)
        d.append(np.sqrt(_x**2 + _y**2))
        d2.append(_x**2 + _y**2)

    binning = np.linspace(-25, 25, 51)
    bin_width = binning[1] - binning[0]
    bin_centers = binning[:-1] + bin_width / 2.
    model = lambda x: gauss(x, num_realizations * bin_width, 0., np.sqrt(num_steps / 2.))

    plt.figure('x histogram')
    obs, _, _ = plt.hist(x, bins=binning)
    exp = model(bin_centers)
    mask = obs > 0
    chisq = ((obs[mask] - exp[mask])**2 / exp[mask]).sum()
    print(f'x distribution, chisquare = {chisq} / {mask.sum()} dof')
    plt.plot(bin_centers, model(bin_centers))

    plt.figure('y histogram')
    obs, _, _ = plt.hist(y, bins=binning)
    exp = model(bin_centers)
    mask = obs > 0
    chisq = ((obs[mask] - exp[mask])**2 / exp[mask]).sum()
    print(f'y distribution, chisquare = {chisq} / {mask.sum()} dof')
    plt.plot(bin_centers, model(bin_centers))

    binning = np.linspace(0, 1000, 101)
    bin_width = binning[1] - binning[0]
    bin_centers = binning[:-1] + bin_width / 2.
    model = lambda x: expo(x, num_realizations * bin_width, num_steps)

    plt.figure('d2 histogram')
    obs, _, _ = plt.hist(d2, bins=binning)
    exp = model(bin_centers)
    mask = obs > 0
    chisq = ((obs[mask] - exp[mask])**2 / exp[mask]).sum()
    print(f'd^2 distribution, chisquare = {chisq} / {mask.sum()} dof')
    plt.plot(bin_centers, model(bin_centers))

    binning = np.linspace(0, 30, 51)
    bin_width = binning[1] - binning[0]
    bin_centers = binning[:-1] + bin_width / 2.
    model = lambda x: dmodel(x, num_realizations * bin_width, num_steps)

    plt.figure('d histogram')
    obs, _, _ = plt.hist(d, bins=binning)
    exp = model(bin_centers)
    mask = obs > 0
    chisq = ((obs[mask] - exp[mask])**2 / exp[mask]).sum()
    print(f'd^2 distribution, chisquare = {chisq} / {mask.sum()} dof')
    plt.plot(bin_centers, model(bin_centers))

    num_realizations = 1000
    N = (10, 25, 50, 100, 250, 500, 1000)
    d = []
    for num_steps in N:
        _d = 0.
        for _ in range(num_realizations):
            _x, _y = random_walk_2d_fast(num_steps)
            _d += np.sqrt(_x**2 + _y**2)
        d.append(_d / num_realizations)
    plt.figure('scaling')
    plt.plot(N, d, 'o')
    grid = np.linspace(0., 1000., 100)
    plt.plot(grid, np.sqrt(np.pi) / 2 * np.sqrt(grid))
    plt.xlabel('$N$')
    plt.ylabel('$<d>$')

    plot_random_walk_2d(1000)

    plt.show()