from numOfOccurances import NumberOfOccurances
class Person():
    name = None

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


person = Person(name="Thameem")
person.display_name()
NumberOfOccurances.read_input(NumberOfOccurances())
#NumberOfOccurances.print_dup_removed()
