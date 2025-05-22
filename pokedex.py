class Pokemon:
    def __init__(self, dex_no, name, type, id_no, nature, level, caught_location, item):
        self.dex_no = dex_no
        self.name = name
        self.type = type
        self.id_no = id_no
        self.nature = nature
        self.level = level
        self.caught_location = caught_location
        self.item = item

    def speak(self):
        print(self.name.upper(), self.name.upper())

    def display_data(self):
        print(f"Dex No.: {self.dex_no}")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Type: {self.type}")
        print(f"ID No.: {self.id_no}")
        print(f"Nature: {self.nature}")
        print(f"Caught Location: {self.caught_location}")
        print(f"Item: {self.item}")


shelly = Pokemon("007","Oshawott","Water", 47475, "Quirky",38,"Nuvema Town","Shell Bell")

zebstrika = Pokemon("029", "Zebstrika", "Electric", 47475, "Rash", 38, "Route 3" , "Magnet")

# shelly.display_data()
zebstrika.display_data()
