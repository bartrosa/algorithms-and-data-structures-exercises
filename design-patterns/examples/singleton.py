# Class method implementation - single thread

class Singleton:
    _instance = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


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
