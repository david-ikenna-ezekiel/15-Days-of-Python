class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


    def promote(self, new_position):
        self.position = new_position
        return f"{self.name} has been promoted to {self.position}"


employee = Employee("David Ezekiel", "Data Engineer", 100000)
print(employee.promote("Senior Data Engineer"))