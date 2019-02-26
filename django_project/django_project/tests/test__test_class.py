
from django_project.models.TestClass import TestClass


def test_1():
    test_cl = TestClass()
    test_cl.print_name()


test_1()
