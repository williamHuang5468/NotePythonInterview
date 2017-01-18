

class Subject(object):
    def regist(self, observer):
        pass

    def unregist(self, observer):
        pass

    def notify(self):
        pass


class Observer(object):
    def update(self):
        pass


class MoniterObserver(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, data):
        print("{} get data {}".format(self.name, data))


class CommandObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print("{} get data {}".format(self.name, data))


class SubjectA(Subject):
    def __init__(self):
        self.observers = []
        self.data = 5

    def changeData(self, data):
        self.data = data

    def regist(self, observer):
        self.observers.append(observer)

    def unregist(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.data)


if __name__ == "__main__":
    s = SubjectA()
    m = MoniterObserver("moniter")
    c = CommandObserver("command")
    s.regist(m)
    s.regist(c)
    s.notify()

    s.changeData(10)
    s.notify()
