class Employee:
    def __init__(self, name, monthly):
        self.name = name
        self.monthly = monthly

    def title(self):
        return "Employee"

    def monthly_cost(self):
        return self.monthly

    def describe(self):
        return f"{self.name} {self.title()}: {self.monthly}"
