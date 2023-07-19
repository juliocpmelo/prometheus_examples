import random
import time
import math
from prometheus_client import start_http_server, Summary, Gauge, Counter

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
sin_time = Gauge('sin_example', 'Sin of current time')
sin_time_counter = Counter('counter_sin', 'The amount of times the function was called')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def postRand():
    sin_time_counter.inc(1) # increment of a given value
    currentTimeMillis = time.time() * 1000
    sin_time.set(math.sin(currentTimeMillis))   # Set to a given value

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        postRand()