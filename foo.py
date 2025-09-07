def add_int(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x + y 
    else:
        raise ValueError("{} or {} is not Integer.".format(x,y))