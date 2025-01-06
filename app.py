import os
import time
import redis
from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Get Redis connection details from environment variables with defaults
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
cache = redis.Redis(host=redis_host, port=redis_port)


def get_hit_count():
    retries = 5
    while retries > 0:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            app.logger.warning(f"Redis connection failed. Retrying... ({5 - retries}/5)")
            retries -= 1
            time.sleep(0.5)
    app.logger.error("Max retries exceeded. Could not connect to Redis.")
    raise redis.exceptions.ConnectionError("Failed to connect to Redis after 5 retries")


@app.route("/")
def hello():
    try:
        count = get_hit_count()
        return f"Hello, World! This page has been visited {count} times.\n"
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return "An error occurred while fetching the hit count. Please try again later.\n", 500


if __name__ == "__main__":
    # Run Flask application
    app.run(host="0.0.0.0", port=5000)
