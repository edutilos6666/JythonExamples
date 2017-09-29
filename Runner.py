from SimpleMath import SimpleMath
from ComplexNumber import ComplexNumber
from InterfaceExample import CustomFile
from InheritanceExample import Triangle, Rectangle, Circle
from DateTimeExample import DateTimeExample
import DAOExample
from SwingExample import SwingExample

def test_SimpleMath():
    x, y = 10.0, 3.0
    sm = SimpleMath(x, y)
    res_add = sm.add()
    res_sub = sm.sub()
    res_mul = sm.mul()
    res_div = sm.div()
    print("{0} + {1} = {2}".format(x, y, res_add))
    print("{0} - {1} = {2}".format(x, y, res_sub))
    print("{0} * {1} = {2}".format(x, y, res_mul))
    print("{0} / {1} = {2}".format(x, y, res_div))
    print("")


def test_ComplexNumber():
    cn1 , cn2  = ComplexNumber(3, 3), ComplexNumber(2, 2)
    cn_add = cn1 + cn2
    cn_sub = cn1 - cn2
    cn_mul = cn1 * cn2
    cn_div = cn1 / cn2
    print("cn1 = {0}".format(str(cn1)))
    print("cn2 = {0}".format(repr(cn2)))
    print("cn1 + cn2 = {0}".format(repr(cn_add)))
    print("cn1 - cn2 = {0}".format(repr(cn_sub)))
    print("cn1 * cn2 = {0}".format(cn_mul))
    print("cn1 / cn2 = {0}".format(cn_div))


def test_InterfaceExample():
    cn1 , cn2 , cn3 , cn4 = None , None, None, None
    cn1 = CustomFile("foo.read")
    cn2 = CustomFile("foo.write")
    cn3 = CustomFile("foo.exe")
    cn4 = CustomFile("foo.read.write.exe")
    print("<<infos on {0}".format(cn1.filename))
    print("{0} is readable = {1}".format(cn1.filename, cn1.is_readable()))
    print("{0} is writable = {1}".format(cn1.filename, cn1.is_writable()))
    print("{0} is executable = {1}".format(cn1.filename, cn1.is_executable()))
    cn1.read()
    cn1.write()
    cn1.execute()
    print("")

    print("<<infos on {0}".format(cn2.filename))
    print("{0} is readable = {1}".format(cn2.filename, cn2.is_readable()))
    print("{0} is writable = {1}".format(cn2.filename, cn2.is_writable()))
    print("{0} is executable = {1}".format(cn2.filename, cn2.is_executable()))
    cn2.read()
    cn2.write()
    cn2.execute()
    print("")

    print("<<infos on {0}".format(cn3.filename))
    print("{0} is readable = {1}".format(cn3.filename, cn3.is_readable()))
    print("{0} is writable = {1}".format(cn3.filename, cn3.is_writable()))
    print("{0} is executable = {1}".format(cn3.filename, cn3.is_executable()))
    cn3.read()
    cn3.write()
    cn3.execute()
    print("")

    print("<<infos on {0}".format(cn4.filename))
    print("{0} is readable = {1}".format(cn4.filename, cn4.is_readable()))
    print("{0} is writable = {1}".format(cn4.filename, cn4.is_writable()))
    print("{0} is executable = {1}".format(cn4.filename, cn4.is_executable()))
    cn4.read()
    cn4.write()
    cn4.execute()
    print("")




def test_InheritanceExample():
    s1, s2 , s3 = None , None , None
    s1 = Triangle(8, 9, 10)
    s2 = Rectangle(10, 20)
    s3 = Circle(10)
    print("<<infos on {0}".format(s1))
    print("perimeter = {0}".format(s1.perimeter()))
    print("area = {0}".format(s1.area()))
    print("")
    print("<<infos on {0}".format(s2))
    print("perimeter = {0}".format(s2.perimeter()))
    print("area = {0}".format(s2.area()))
    print("")
    print("<<infos on {0}".format(s3))
    print("perimeter = {0}".format(s3.perimeter()))
    print("area = {0}".format(s3.area()))
    print("")


def test_DateTimeExample():
    runner = DateTimeExample()
    runner.test_LocalDate()
    print("")
    runner.test_LocalTime()
    print("")
    runner.test_LocalDateTime()
    print("")
    runner.test_Calendar()


def test_DAOExample():
    runner = DAOExample.DAOExample()
    runner.example1()


def test_SwingExample():
    runner = SwingExample()
    runner.example1()

def main():
    # test_SimpleMath()
    # test_ComplexNumber()
    # test_InterfaceExample()
    # test_InheritanceExample()
    # test_DateTimeExample()
    # test_DAOExample()
    test_SwingExample()

if __name__ == "__main__":
    main()

