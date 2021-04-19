class Employee():
    def __init__(self, surname, first_name, position):
        self.surname = surname
        self.first_name = first_name
        self.position = position
    def prin(self):
        print("Привет, я ", self.first_name, ", работаю на должности", self.position)

Nikita = Employee(surname="Полежака", first_name="Никита", position="ученик")
Bogdan = Employee(surname="!?!", first_name="Богдан", position="тим лид")
Artyom = Employee(surname="?!?", first_name="Артём", position="ученик")

print(Nikita.prin())