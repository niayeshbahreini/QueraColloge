class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name 
        self.amount = amount
        self.price = price
        


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = list()
        self.employees = list()
   

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)
        

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append({
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })
        
        
         
    def total_value(self):
        total = int
        for drug in self.drugs:
            total += drug.amount * drug.price
        return total
    def employees_summary(self):
        x = "Employees:\n"
        for i, emp in enumerate(self.employees):
            x += f"The employee number {i+1} is {emp['first_name']} {emp['last_name']} who is {emp['age']} years old.\n"
   
        return x
    
        
        