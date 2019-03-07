import operator

def percent(arg1, arg2):
    step1 = operator.mul(arg1, arg2)
    return operator.truediv(step1, 100)
