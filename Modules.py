import os
import sys

print( "Current user is {0}".format( os.environ["USER"] ) )
print( "Running {0}, version {1}".format( sys.platform, sys.version ) )