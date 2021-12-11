import ctypes
lib = ctypes.cdll.LoadLibrary('./lib.so')

prototype = ctypes.CFUNCTYPE(    
    ctypes.c_int,                
    ctypes.c_int,                
    ctypes.c_int,
    ctypes.c_int    
)
distance = prototype(('distance', lib))

res = distance(ctypes.c_int(2), ctypes.c_int(2), ctypes.c_int(2),ctypes.c_int(2) )
print(res)
