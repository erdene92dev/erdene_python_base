class Vehicles(): 
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year

    def process_vehicle_results(self):
        vehicle_year = int(self.year)
        
        print('Your vehicle make is:')
        print('Your vehicle model is:')
        print('Your vehicle year is:')
