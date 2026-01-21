import matplotlib.pyplot as plt
import numpy as np
from random import uniform


def gen_points(m, b, noise, n = 100):
    xs = []
    ys = []
    for i in range(n):
        xs.append(i)
        ys.append(m * i + b + uniform(-noise, noise))
    return xs, ys

def show_loss_map(loss_func, xs, ys, res=100, m_min=0, m_max=10, b_min=-10, b_max=10):
    loss_map = np.zeros((res, res))
    ms = np.linspace(m_min, m_max, res)
    bs = np.linspace(b_min, b_max, res)

    for j in range(len(ms)):
        for i in range(len(bs)):
            loss_map[j,i] = loss_func(xs, ys, ms[j], bs[i])
    
    x = np.linspace(m_min, m_max, res)
    y = np.linspace(b_min, b_max, res)
    X, Y = np.meshgrid(x, y)
    
    plt.imshow(loss_map, cmap="viridis", extent=[m_min, m_max, b_min, b_max], origin="lower", aspect="auto")
    plt.xlabel("m")
    plt.ylabel("b")
    plt.colorbar()
    plt.contour(X, Y, loss_map, levels=25, colors="white", linewidth=0.25)
    plt.show()
    

def ls_loss(xs, ys, m, b):
    loss = 0
    for x, y in zip(xs, ys):
        loss += (m * x + b - y) ** 2
    return loss

def abs_loss(xs, ys, m, b):
    loss = 0
    for x, y in zip(xs, ys):
        loss += abs(m * x + b - y)
    return loss

def abs_cubic_loss(xs, ys, m, b):
    loss = 0
    for x, y in zip(xs, ys):
        loss += abs((m * x + b -y) ** 3)
    return loss

xs, ys = gen_points(1, 0, 0)

show_loss_map(abs_loss, xs, ys, m_min=-1, m_max=2, b_min=-50, b_max=50)
