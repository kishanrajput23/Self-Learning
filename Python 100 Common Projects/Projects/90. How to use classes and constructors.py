class company:
    def __init__(self, employee_firstname, employee_surname):
        self.firstname = employee_firstname
        self.surname = employee_surname

    def employee(self):
        return self.firstname + ' ' + self.surname

staff = []
for i in range(3):
    name = input("Insert firstname and surname: ")
    name = name.split()
    staff.append(company(name[0], name[1]))

for i in staff:
    print(i.employee())