###############################################################################
# Class implementation - single thread

class Singleton:
    _instance = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

###############################################################################
# Decorator implementation - single thread

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Initializing Database")


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1 is obj2)

    db1 = Database()
    db2 = Database()
    print(db1 is db2)

###############################################################################
# Decorator implementation - multithread

import threading

def singleton(cls):
    instances = {}
    lock = threading.Lock()
    
    def get_instance(*args, **kwargs):
        nonlocal instances
        if cls not in instances:
            with lock:
                if cls not in instances:  # Double-checked locking
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class SingletonClass:
    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value

def singleton_test():
    instance = SingletonClass()
    print(f"Instance ID: {id(instance)}, Value: {instance.get_value()}")

threads = []
for i in range(10):
    t = threading.Thread(target=singleton_test)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
###############################################################################
# Class implementation - multiprocessing

from multiprocessing import Manager, Process, Lock

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    manager = Manager()
                    cls._instances[cls] = manager.SingletonClass()
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value

def singleton_test():
    instance = SingletonClass()
    print(f"Instance ID: {id(instance)}, Value: {instance.get_value()}")

if __name__ == "__main__":
    processes = []
    for i in range(10):
        p = Process(target=singleton_test)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
