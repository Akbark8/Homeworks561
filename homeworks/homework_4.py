from datetime import datetime as dt

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        result = func(*args, **kwargs)
        print(f"Функция была вызвана в {time_now.hour:02}:{time_now.minute:02}:{time_now.second:02} "
              f"{time_now.day:02}/{time_now.month:02}/{time_now.year}")
        print(func.__name__)
        return result
    return wrapper

@checktime
def hello_world():
    print("hello world")

hello_world()
