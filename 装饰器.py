import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return res

    return wrapper


@timer  # index=timer(index)
def index():
    time.sleep(3)
    print('Welcome to the index page')
    return 200


@timer  # home=timer(home)
def home(name):
    time.sleep(5)
    print('Welcome to the home page', name)


index()
home(123)
