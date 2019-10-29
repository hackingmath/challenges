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
foods.append(Food("Grilled Top Sirloin",
                      30,20,10,78,83.8,0,0,295))

class Meal(object):
    def __init__(self):
        self.food_list = []
        self.protein = 0
        self.fats = 0
        self.carbs = 0
        self.cholestorol = 0
        self.sodium = 0
        self.sugars = 0
        self.fiber = 0
        self.calories = 0
        self.facts = [self.protein,
                      self.fats,
                      self.carbs,
                      self.cholestorol,
                      self.sodium,
                      self.sugars,
                      self.fiber,
                      self.calories]
        self.units = ['g','g','g','mg','mg','g','g','calories']

    def take_order(self):
        global foods
        #self.foods = []

        print("The menu is:")
        print("1) Grilled Chicken")
        print("2) Mashed Sweet Potatoes")
        print("3) Grilled Top Sirloin")

        while True:
            choice = input("Enter the number of an item or 'd' if you're done. ")
            if choice == 'd': break
            self.food_list.append(foods[int(choice)-1])


        print()
        print("Your order is:")
        for food in self.food_list:
            print(food.name)

    def update(self):
        for food in self.food_list:
            for i,f in enumerate(self.facts):
                m.facts[i] += food.facts[i]
        print("Here are the totals for your meal:")
        for i,f in enumerate(self.facts):
            print(f,self.units[i])


#meal 
m = Meal()
m.take_order()
m.update()
