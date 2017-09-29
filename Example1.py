from java.util import Random, Scanner
from java.lang import System

def example1():
    rand = Random()
    print(rand.nextInt())



def example2():
    scanner = Scanner(System.in)
    id , name , age, wage, active = None , None, None, None , None
    print("insert your id: ")
    id = scanner.nextLong()
    scanner.nextLine()
    print("insert your name: ")
    name = scanner.nextLine()
    print("insert your age: ")
    age = scanner.nextInt()
    scanner.nextLine()
    print("insert your wage: ")
    wage = scanner.nextDouble()
    scanner.nextLine()
    print("insert whether you are active: ")
    active = scanner.nextBoolean()
    scanner.nextLine()
    print("id = ", id)
    print("name = ", name)
    print("age = ", age)
    print("wage = ", wage)
    print("active = ", active)


# example2()


class Foo:
    def bar(self):
        print("hello")

