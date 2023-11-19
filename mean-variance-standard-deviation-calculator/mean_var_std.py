import numpy as np 
def calculate(lst):
    if len(lst)!=9:
        raise ValueError( "List must contain nine numbers.")
    a=np.array(lst)
    b=a.reshape(3,3)
    calculations={**fmean(b),**fvar(b),**fstd(b),**fmax(b),**fmin(b),**fsum(b)}
    return(calculations)
def fmean(x):
    y=[(x.mean(axis=0)).tolist(),(x.mean(axis=1)).tolist(),x.mean()]
    return {'mean':y}
def fvar(x):
    y=[(x.var(axis=0)).tolist(),(x.var(axis=1)).tolist(),x.var()]
    return {"variance":y}
def fmax(x):
    y=[(x.max(axis=0)).tolist(),(x.max(axis=1)).tolist(),x.max()]
    return {"max":y}
def fmin(x):
    y=[(x.min(axis=0)).tolist(),(x.min(axis=1)).tolist(),x.min()]
    return{'min':y}
def fsum(x):
    y=[(x.sum(axis=0)).tolist(),(x.sum(axis=1)).tolist(),x.sum()]
    return{'sum':y}
def fstd(x):
    y=[(x.std(axis=0)).tolist(),(x.std(axis=1)).tolist(),x.std()]
    return{'standard deviation':y}