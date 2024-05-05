import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.model} {self.color}'


if __name__ == "__main__":
    prototype = Prototype()
    car = Car('Tesla Model S', 'red')

    prototype.register_object('Tesla', car)

    car1 = prototype.clone('Tesla')
    car2 = prototype.clone('Tesla', color='blue')

    print(car1)
    print(car2)
