
class TestClass(object):

    def __init__(self):
        print('This is: ' + TestClass.__name__)

    def print_name(self):
        print(TestClass.__name__)

    @staticmethod
    def print2(self):
        print(2)

    def __private1(self):
        print("it's a private method")
