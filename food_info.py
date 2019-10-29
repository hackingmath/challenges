"""Nutritional Breakdown Program"""

class Food(object):
    def __init__(self,name,protein,fats,carbs,cholestorol,sodium,sugars,fiber,calories):
        self.name = name
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.cholestorol = cholestorol
        self.sodium = sodium
        self.sugars = sugars
        self.fiber = fiber
        self.calories = calories
        self.facts = [self.protein,
                      self.fats,
                      self.carbs,
                      self.cholestorol,
                      self.sodium,
                      self.sugars,
                      self.fiber,
                      self.calories]

    def __str__(self):
        return self.name

    def __add__(self,other):
        output = []
        for i in range(len(self.facts)):
            output.append(self.facts[i] + other.facts[i])
        return output

    def print_info(self):
        #print(f"{self.name}")
        print(f"Protein: {self.protein}g")
        

foods = []
foods.append(Food("Grilled Chicken",
                       34,4,0,118,58.7,0,0,165))
foods.append(Food("Mashed Sweet Potatoes",
                       5,0.5,59.1,0,2,13.9,4.3,258))

meal = []

print("The menu is:")
print("1) Grilled Chicken")
print("2) Mashed Sweet Potatoes")

while True:
    choice = input("Enter the number of an item or 'd' if you're done. ")
    if choice == 'd': break
    meal.append(foods[int(choice)-1])


print()
print("Your order is:")
for food in meal:
    print(food.name)

a = Food("Grilled Chicken",
                       34,4,0,118,58.7,0,0,165)
b = Food("Mashed Sweet Potatoes",
                       5,0.5,59.1,0,2,13.9,4.3,258)

print(a+b)
