import numpy as np
import pandas as pd

pi = np.pi

scales = (512, 256, 128, 64)
thetas = (0, pi/6, pi/4, pi/6, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi)
sigmas = (4, 16, 32, 64)
lambdas = ((1, 2), (2, 4), (4, 8), (16, 32))

params = {
    'Scale': np.merge(np.repeat(512, 4), np.repeat(256, 3)),
    'Sigma': [4, 16, 32, 64, 4, 16, 32]
}

print(params)
df = pd.DataFrame(params)

print(df)