class RemoteControl(object):
    def __init__(self):
        self.commandStack = []
        self.undoCommandStack = []

    def setCommand(self, command):
        self.commandStack.append(command)

    def pressButton(self):
        command = self.commandStack.pop()
        command.excute()
        self.undoCommandStack.append(command)

    def undo(self):
        self.undoCommandStack.pop().undo()


class Command(object):
    def excute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def excute(self):
        print("Light is On")

    def undo(self):
        print("Light is Off")


class LightOffCommand(Command):
    def excute(self):
        print("Light is Off")

    def undo(self):
        print("Light is On")


if __name__ == "__main__":
    r = RemoteControl()
    r.setCommand(LightOnCommand())
    r.setCommand(LightOffCommand())
    r.pressButton()
    r.undo()
