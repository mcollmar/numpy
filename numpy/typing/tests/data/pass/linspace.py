import numpy as np

class Index:
    def __index__(self) -> int:
        return 0

np.linspace(0, 2)
np.linspace(0.5, [0, 1, 2])
np.linspace([0, 1, 2], 3)
np.linspace(0j, 2)
np.linspace(0, 2, num=10)
np.linspace(0, 2, endpoint=True)
np.linspace(0, 2, retstep=True)
np.linspace(0j, 2j, retstep=True)
np.linspace(0, 2, dtype=bool)
np.linspace([0, 1], [2, 3], axis=Index())

np.logspace(0, 2, base=2)
np.logspace(0, 2, base=2)
np.logspace(0, 2, base=[1j, 2j], num=2)

np.geomspace(1, 2)
