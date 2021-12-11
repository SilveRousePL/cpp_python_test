# test.py 
import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes 

_doublepp = ndpointer(dtype=np.uintp, ndim=1, flags='C') 

_dll = ctypes.CDLL('./lib.so') 

_foobar = _dll.foobar 
_foobar.argtypes = [ctypes.c_int, ctypes.c_int, _doublepp, _doublepp] 
_foobar.restype = None 

def foobar(x): 
    y = np.zeros_like(x) 
    xpp = (x.__array_interface__['data'][0] 
      + np.arange(x.shape[0])*x.strides[0]).astype(np.uintp) 
    ypp = (y.__array_interface__['data'][0] 
      + np.arange(y.shape[0])*y.strides[0]).astype(np.uintp) 
    m = ctypes.c_int(x.shape[0]) 
    n = ctypes.c_int(x.shape[1]) 
    _foobar(m, n, xpp, ypp) 
    return y 

if __name__ == '__main__': 
    x = np.arange(9.).reshape((3, 3))
    y = foobar(x)

    print(x)
    print(y)