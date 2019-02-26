
from django_project.models.TestClass import TestClass


class ConcreteTestClass(TestClass):

    def __init__(self, name):
        super(ConcreteTestClass, self).__init__()
        self.name = name
        print("ConcreteTestClass")




con_test = ConcreteTestClass('name1')
print(con_test.__dict__)