from time import sleep, localtime, strftime
from secrets import token_hex


hash = token_hex(nbytes=16)

if __name__ == "__main__":
    while True:
        t = localtime()
        current_time = strftime("%H:%M:%S", t)
        print(f'{current_time}: {hash}', flush=True)

        sleep(5)