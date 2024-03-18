from db import c, conn


class Employee(object):
    def __init__(self, name, surname, age, id=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def employees_exist(cls):
        return c.execute("SELECT COUNT(*) FROM employee").fetchone()[0]

    @classmethod
    def get(cls, employee_id):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        values = result.fetchone()
        if values is None:
            print("Employee does not exist")
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT DISTINCT * FROM employee WHERE "
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query += " AND ".join(conditions)
        result = c.execute(query, tuple(values))

        employees = []
        for row in result.fetchall():
            employees.append(Employee(row["name"], row["surname"], row["age"]))
        return employees

    def __repr__(self):
        return "Employee: {}".format(self.name)

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))
        conn.commit()

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid
        conn.commit()

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        conn.commit()

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.age < other.age
        return False

    def __le__(self, other):
        if isinstance(other, Employee):
            return self.age <= other.age
        return False

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.age == other.age
        return False

    def __ne__(self, other):
        if isinstance(other, Employee):
            return self.age != other.age
        return False

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.age > other.age
        return False

    def __ge__(self, other):
        if isinstance(other, Employee):
            return self.age >= other.age
        return False
