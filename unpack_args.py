def f(*args, **kwargs): 
    print("Named:", kwargs)
    

"""
args are positional argulents (have positions or locationas)
kwargs are named arguments (have keys and values)
"""

f(galleons=100, sickles=50, knuts=25)