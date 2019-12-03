import numpy as np

def fn(x):
    p = 3**9 + 3**12 + 3**15 + 3**x
    a = np.cbrt(p)
    return a if a == np.floor(a) else -1

if __name__ == '__main__':
    for i in range(0, 20):
        q = fn(i)
        print('i={}, result={}'.format(i, q))

        if q != -1:
            print('n =', i)
            break
