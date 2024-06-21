class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
