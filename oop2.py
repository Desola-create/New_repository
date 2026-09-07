class Edible:
    def __init__(self, edible_name, edible_type):
        self.edible_name = edible_name
        self.edible_type = edible_type


    def display_edible(self):
        print ("edible Name:", self.edible_name)
        print ("edible Type:", self.edible_type)

rice = Edible("Rice", "carbohydrate")
rice.display_edible()