class Employee:
    def __init__(self,name,age,salary,education,employee_id,stage):
        self._name = name
        self._age = age
        self.__salary = salary
        self._education = education
        self.__employee_id = employee_id
        self.stage = stage
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get__salary(self):
        return self.__salary
    def get__education(self):
        return self._education
    def get__employee_id(self):
        return self.__employee_id
    def calculate_salary(self):
        return self.__salary
    def up_salary(self):
        return self.__salary * self.stage * 0.05
    def __str__(self):
        return f"ID:{self.__employee_id} имя {self._name} образование {self._education} зарплата {self.calculate_salary()} рублей ."
        
class Manager(Employee):
    def __init__(self, name, age, salary, education, employee_id, stage ,team_size):
        super().__init__(name, age, salary, education, employee_id, stage)
        self._team_size = team_size
        self._bonus_per_person = 5000
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus =  self._team_size * self._bonus_per_person
        return bonus + base_salary 
    def __str__(self): 
        base_info = super().__str__()
        return f"{base_info} размер команды {self._team_size}"

class Developer(Employee):
    def __init__(self, name, age, salary, education, employee_id, stage, quantity):
        super().__init__(name, age, salary, education, employee_id, stage)
        self._quantity = quantity
        self._bonus_per_quantity = 20000
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus =  self._quantity * self._bonus_per_quantity
        return bonus + base_salary
    def __str__(self): 
        base_info = super().__str__()
        return f"{base_info} количество созданных приложений {self._quantity}"

class Department:
    def __init__(self,name):
        self.name = name
        self._employees = []
    def hire_employee(self,employee):
        if  isinstance(employee,Employee):
            self._employees.append(employee)
            print(f"{employee.get_name()} принят в отдел {self.name}")
        else:
            print("Ошибка можно нанимать только сотрудников Employee")
    def delete_employee(self,employee_id):
        for employee in self._employees:
            if employee.get__employee_id() == employee_id:
                self._employees.remove(employee)
                print(f"Сотрудник с ID:{employee_id} уволен")
                return
            else:
                print(f"Сотрудник с данным id не найден")
    def list_employee(self):
        print(f"Сотрудники отдела {self.name}")
        if not self._employees:
            print(f"Сотрудников в отделе {self.name} нету")
        for employee in self._employees:
            print(employee) 
class Company:
    def __init__(self,name):
        self.name = name

    def movement(self,department1,department2,employee):
        # for dep in department1._employees:
        if employee in department1._employees:
            department1._employees.remove(employee)
            department2._employees.append(employee)
            print(f"Сотрудник {employee._name} был переведен из отдела {department1.name} в отдел {department2.name}")
        else:
            print(f"Сотрудника {employee} в отделе {department1} нет")





if __name__ == "__main__":
    my_company = Company("Хрючка вонючка")
    control_department = Department("Контроль качества")
    marketing_department = Department("Маркетинг")
    robert = Developer("Robert",24,50000,"Высшее","IU3420", 3, 2)
    alice = Employee("Alice",20,50000,"Среднее","EM10090", 1)
    bob = Manager("Bob",50,50000,"Высшее","MR007", 14, 6)
    control_department.hire_employee(robert)
    marketing_department.hire_employee(alice)
    marketing_department.hire_employee(bob)
    control_department.list_employee()
    marketing_department.list_employee()
    # marketing_department.delete_employee("EM10090")
    marketing_department.list_employee()
    control_department.list_employee()

    my_company.movement(marketing_department,control_department,bob)
    marketing_department.list_employee()
    control_department.list_employee()


# Реализовать систему повышение зарплаты от стажа работы и инфляции UFLFDFKFQQQ

# Реализовать выручку как всей компании так и отдельно отделов