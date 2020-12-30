import threading
import time
import random
import multiprocessing
import concurrent.futures

from simple_business_logic import do_something, get_random_seconds

# Generally speaking, the API is pretty much identitical to the threading model

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit( do_something, get_random_seconds() ) for _ in range(10)]

    for f in concurrent.futures.as_completed(futures):
        print(f.result())

with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [get_random_seconds() for n in range(10)]

    results = executor.map( do_something, seconds )

