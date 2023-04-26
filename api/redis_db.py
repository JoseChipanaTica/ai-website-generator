import os
import redis


class RedisDB:
    _instance = None
    redis_db = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def start_db(self):
        self.redis_db = redis.Redis(host=os.getenv('REDIS_HOST'),
                                    port=int(os.getenv('REDIS_PORT')),
                                    password=os.getenv('REDIS_PASS'),
                                    username=os.getenv('REDIS_USER'),
                                    decode_responses=True)
