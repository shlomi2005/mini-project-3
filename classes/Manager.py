from classes.Employee import Employee


class Manager(Employee):
    def __init__(self, name, monthly, bonus):
        super().__init__(name, monthly)
        self.bonus = bonus

    def title(self):
        return "Meneger"

    def monthly_cost(self):
        return super().monthly_cost() + self.bonus
