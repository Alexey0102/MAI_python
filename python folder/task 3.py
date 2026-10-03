import time
def i_time(fun):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = fun(*args,**kwargs)
        print(f'Time:{time.time()-start}')
        return result
    return wrapper
@i_time
def func():
    sum(range(10_000_000))
func()

