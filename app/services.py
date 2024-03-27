from huey import RedisHuey
from redis import Redis

huey = RedisHuey("queue", host="localhost", password="a-very-complex-password-here")
r = Redis(host="localhost", port=6379 , password="a-very-complex-password-here")

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
