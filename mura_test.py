import numpy as np
import matplotlib.pyplot as plt

def is_quadratic_residue(n, p):
    for i in range(p):
        if (i * i) % p == n:
            return True
    return False

# generate a MURA
# p must be prime (and possibly other constraints?)
def A(p: int) -> np.ndarray:
    a = np.ndarray((p,p))
    quadratic_residues = [is_quadratic_residue(n,p) for n in range(p)]
    for r in range(p):
        for c in range(p):
            if r == 0:
                a[r][c] = 0
            elif c == 0:
                a[r][c] = 1
            elif quadratic_residues[r] ^ quadratic_residues[c]:
                a[r][c] = 0
            else:
                a[r][c] = 1
    # The .T[...] is what's needed to make the pattern match our physical masks
    # There's probably a simpler transform to get there
    return a.T[:,::-1]


def plot_binary_image(image, cmap='gray'):
    image_array = np.asarray(image)
    plt.imshow(image_array, cmap=cmap, interpolation='nearest')
    plt.axis('off')
    plt.show()


plot_binary_image(A(11))