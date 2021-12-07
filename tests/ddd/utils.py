import time
from uuid import uuid4


def current_timestamp():
    return int(time.time() * 1000)


def uuid_gen():
    return uuid4().hex
