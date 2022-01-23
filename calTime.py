import time
def cal_time(func):
    def wrapper(*args, **kw):  
        start = time.perf_counter() 
        func(*args, **kw) 
        print(f'Function [{func.__name__ }] spent {time.perf_counter() - start:0.5f} s')
    return wrapper 
