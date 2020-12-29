import os
import sys

#print( "my_module.py loading ..." )

def print_platform_info():
    """Will print the OS version on screen.
    """
    print( "Current user is {0}".format( os.environ["USER"] ) )
    print( "Running {0}, version {1}".format( sys.platform, sys.version ) )

def print_python_path():
    """Will print the list of directories that Python will look into for valid Python modules
    """
    print( sys.path )