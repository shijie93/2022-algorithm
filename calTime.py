import time
def cal_time(func):
    def wrapper(*args, **kw):  
        start = time.perf_counter() 
        ret = func(*args, **kw) 
        print(f'Function [{func.__name__ }] spent {time.perf_counter() - start:0.5f} s')
        return ret
    return wrapper 

def cal_avg_time(times):
    def dector(func):
        def wrapper(*args, **kw):  
            start = time.perf_counter() 
            ret = func(*args, **kw) 
            print(f'Function [{func.__name__ }] avg {times} spent {(time.perf_counter() - start) / times:0.5f} s [{args[0].__name__}] ')
            return ret
        return wrapper 
    return dector