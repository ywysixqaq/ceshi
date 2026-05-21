import time

def time_format(timestamp):
    time_array = time.localtime(timestamp)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return formatted_time

if __name__ == '__main__':
    timestamp = time.time()
    formatted_time = time_format(timestamp)
    print(formatted_time)