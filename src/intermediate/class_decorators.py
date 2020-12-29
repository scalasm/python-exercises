import logging
import time
from typing import Any

logging.basicConfig(level=logging.DEBUG)

class Logger(object):
    def __init__(self, original_function) -> None:
        super().__init__()
        self.original_function = original_function
    
    def __call__(self, *args: Any, **kargs: Any) -> Any:
        logging.debug( "Entering {}{}".format(self.original_function.__name__,args) )
        result = self.original_function(*args, **kargs)
        logging.debug( "Exiting {} = {}".format(self.original_function.__name__,result) )
        return result

class Timer(object):
    def __init__(self, original_function) -> None:
        super().__init__()
        self.original_function = original_function

    def __call__(self, *args: Any, **kargs: Any) -> Any:
        time_start = time.time()
        result = self.original_function(*args, **kargs)
        time_elapsed = (time.time() - time_start) / 1000

#        logging.info( "Execution time {}{} is {} seconds".format(self.original_function.__name__,args,time_elapsed) )
        logging.info( "Execution time is {} ms".format(time_elapsed) )
        return result

@Timer
@Logger
def add(a,b):
    return a+b

@Timer
@Logger
def sub(a,b):
    return a-b

add(3,5)
sub(4,3)
