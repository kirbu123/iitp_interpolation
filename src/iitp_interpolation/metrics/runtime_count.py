import logging
import time
from functools import wraps

# Create a logger for your module
logging.basicConfig(
    level=logging.INFO,  # Set minimum log level
    format='%(levelname)s - %(message)s'  # Simple format
)
logger = logging.getLogger(__name__)


def runtime_count(func):
    """Decorator that measures and logs the execution time of a function."""
    @wraps(func)
    def wrapper(image, scale_factor: float):
        start_time = time.perf_counter()  # More precise than time.time()
        result = func(image, scale_factor)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        
        logger.info(
            f"Function {func.__name__} executed in {runtime:.6f} seconds | "
        )
        return result  # Return both result and runtime
    
    return wrapper
