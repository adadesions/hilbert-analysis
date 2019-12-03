import numpy as np
import pandas as pd

pi = np.pi

scales = (512, 256, 128, 64)
thetas = [0, pi/6, pi/4, pi/6, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi]
sigmas = (4, 16, 32, 64)
lambdas = ((1, 2), (2, 4), (4, 8), (16, 32))

lenSigma, lenTheta, lenLambda = len(sigmas), len(thetas), 2
maxLen = lenSigma*lenTheta*lenLambda


params = {
    'Scale': np.concatenate((
        np.repeat(512, 4*2*lenTheta), # lenSigma x lenLambda x lenTheta
        np.repeat(256, 4*2*lenTheta),
    )),
    'Sigma': np.concatenate((
        np.repeat([4, 16, 32, 64], 2*lenTheta, axis=0).flatten(),
        np.repeat([4, 16, 32, 64], 2*lenTheta, axis=0).flatten(),
    )),
    'Lambda': np.concatenate((
        np.repeat([[1, 2]], 4*lenTheta, axis=0).flatten(), # lenSigma x lenTheta
        np.repeat([[2, 4]], 4*lenTheta, axis=0).flatten(),
    )),
    'Theta': np.repeat([thetas], 4*2*2, axis=0).flatten(), # lenSigma x lenLambda 
}

gaborParams = pd.DataFrame(params).sort_values(['Scale', 'Lambda', 'Sigma', 'Theta'])

print(gaborParams)

with open('gaborParams.csv', 'w') as file:
    file.write(gaborParams.to_csv(index=False))