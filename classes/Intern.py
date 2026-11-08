from classes.Employee import Employee


class Intern(Employee):
    def __init__(self, name, monthly, month):
        super().__init__(name, monthly)
        self.month = month

    def validation(self, month):
        if month <= 0 or month > 12:
            raise ValueError("months must be 1-12")

    def title(self):
        return "Intern"
