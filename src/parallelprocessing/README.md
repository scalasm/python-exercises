# FAQ

## Multi-processing vs Multi-threading in Python

You want to use multithreading when dealing with IO-bound tasks (e.g., HTTP calls or Disk read/write); use multiprocessing when you have computation-intensive tasks, like image processing, and you are running on a multi-core machine.

It's a trade-off depending on your use-case, see [this article](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/) for more information.
