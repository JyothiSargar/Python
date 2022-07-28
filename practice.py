class Avenger:
    def __init__(self,Name,Age,Gender,Super_Power,Weapon):
        self.Name= Name
        self.Age= Age
        self.Gender = Gender
        self.Super_power= Super_Power
        self.Weapon = Weapon
    def getinfo(self):
            return f"""
            Avenger Profile:

            Name:   {self.Name}
            Age:    {self.Age}
            Gender: {self.Gender}

            Has {self.Weapon} weapon and {self.Super_power} super Power. 
            """



Super_heroes = ['Captain America', 'Iron Man', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
super_powers = ['Super strength', 'Technology', 'superhuman', 'Unlimited Strength', 'super Energy', 'fighting skills']
weapons = ["Shield", "Armor", "Batons", "No Weapon", "Mjölnir", "Bow and Arrows"]
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']

Avengers = []
for Name,Age,Gender,Super_Power,Weapon in zip(Super_heroes ,ages,genders,super_powers,weapons):
    Avengers.append(
        Avenger(Name,Age,Gender,Super_Power,Weapon)
    )

print(Avengers[4].getinfo())
