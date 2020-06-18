import sys
from tracer import Tracer
from example import main


tracer = Tracer()
sys.settrace(tracer)
creds = main(1993, 71, 1.79)
print(creds)
