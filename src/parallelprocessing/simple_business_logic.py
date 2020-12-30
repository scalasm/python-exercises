import threading
import time
from random import choice

def do_something(seconds):
    thread_name = threading.current_thread().name
    print(f"Start doing something for {seconds} seconds in thread {thread_name} ...")
    time.sleep( seconds )
    print(f"{thread_name} completed!")

    return f"It took me {seconds} seconds!"

def get_random_seconds():
    return choice( range(5) ) + 1