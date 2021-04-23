class Student():
    def __init__(self, name, age, group_num):
        self.name = name
        self.age = age
        self.group_num = group_num

    def get_group_number(self):
        print("Номер группы ", self.group_num)

    def set_name_age(self):
        self.name = input("Введите новое имя ученика")
        print("Имя ученика изменилась на ", self.name)
        self.age = int(input("Введите новый возраст ученика"))
        print("Возраст ученика изменился на ", self.age)

    def set_num_group(self):
        self.group_num = int(input("Введите новый номер группы"))
        print("Номер группы изменён на ", self.group_num)

stud1 = Student("Ivan", 18, "10A")
stud2 = Student("Alan", 16, "9Б")
stud3 = Student("Gosha", 15, "8Б")
stud4 = Student("Maxim", 16, "9Б")
stud5 = Student("Igor", 17, "11А")

stud2.get_group_number()