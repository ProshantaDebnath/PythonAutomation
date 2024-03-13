from PythonAutomationPractice.OOPSDemo import Calculator


class ChildMethod(Calculator):

    def __init__(self):
        Calculator.__init__(self, self.a, self.b)

    obj = Calculator(4,5)
    obj.add()

