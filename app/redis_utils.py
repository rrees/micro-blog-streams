import redis

def setup_redis(redis_url):
    if not redis_url:
        return None
    
    return redis.from_url(redis_url, decode_responses=True)
