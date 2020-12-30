import threading
import time
import random

from simple_business_logic import do_something, get_random_seconds


start = time.perf_counter()

# Option 1 - This is the old way

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[2])
#     t.start()
#     threads.append(t)

# # Ensure they both finish before bailing out with results!
# for t in threads:
#     t.join()

# Option 2 - From Python 3.2 onwards use this one

import concurrent.futures


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = [executor.submit( do_something, get_random_seconds() ) for _ in range(10)]

#     for f in concurrent.futures.as_completed(futures):
#         print(f.result())

# Option 3 - You can use map() to obtain a similar result

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [get_random_seconds() for n in range(10)]

    # Using map produces results in the exact order of the submitted tasks!
    results = executor.map( do_something, seconds )

# You can have them complete before shutting down the executor
#executor.shutdown(wait=True)

finish = time.perf_counter()

print( f"Finished in {round(finish-start,2)} second(s)" )
