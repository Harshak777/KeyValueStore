from huey import RedisHuey
from redis import Redis
import os

QUEUE_NAME = os.getenv("QUEUE_NAME", "queue")
HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 6379)


huey = RedisHuey(QUEUE_NAME, host=HOST, port=PORT)
r = Redis(host=HOST, port=PORT)

class Services:
    def __init__(self, host="localhost"):
        self.huey_client = RedisHuey(host)

    @huey.task()
    def set_value(key, value):
        print(key, value)
        response = r.set(key, value)
        return response

    @huey.task()
    def get_value(key):
        if r.exists(key):
            response = r.get(key)
            print(response)
            return response
        else:
            return "Key not found"


    @huey.task()
    def delete_key(key):
        response = r.delete(key)
        print(response)
        return "Key deleted"
