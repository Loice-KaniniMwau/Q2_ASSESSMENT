#  pseudo code 
#  input - define length of story ,moral lessons and its age group
#  process-define a class Ancestral stories which will help describe the story.
#  output-ancestral stories with their description and their storytellers , the translators
class Ancestral_stories:
    def __init__(self,length,morallessons,age,nameofstory ) :
        self.length=length
        self.morallessons=morallessons
        self.age=age
        self.nameofstory=nameofstory
    def describe_story(self):
        return f"`${self.nameofstory} teaches us to be ${self.morallessons} and targets ${self.age}"
class Stories(Ancestral_stories):
    def __init__(self, length, morallessons, age, nameofstory,typeofstory):
        super().__init__(length, morallessons, age, nameofstory)  
        self.typeofstory=typeofstory
    def typeofstory(self):
        return f"${self.nameofstory} which is a ${self.typeofstory}teaches us to be ${self.morallessons} and targets ${self.age}"
story1=Ancestral_stories(10,"live good life",20,"riverandthesoruce")
print(story1.describe_story())

story2=Stories(30,"respect",40,"bronacrime","historical")
print(story2.describe_story)
print(story2.typeofstory)
# question2
# pseudo code 
# input-define the names different african cusines,their unique ingredients, preparation time, cooking method, and nutritional
# information
# process-define class Recipe where the african cusines will inherit from and have their unique methods
# output-well defined african cusines with their descriptions and their preparation process

class Recipe:
    def __init__(self,nameofcuisine,countryoforigin,cookingmethod,nutritionalvalue):
        self.nameofcuisne=nameofcuisine
        self.cookingmethod=cookingmethod
        self.countryoforigin=countryoforigin
        self.ingredients={}
        self.preparationtime=0
        self.nutrionvalue=nutritionalvalue
    def describeCuisine(self):
        return f"${self.nameofcuisne} is originally from ${self.countryoforigin} and helps with ${self.nutrionvalue}"

class MoroccanRecipe(Recipe):
    def __init__(self, nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue):
        super().__init__(nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue) 
    def describeCuisine(self):
        # return super().describeCuisine()
        return f"${self.nameofcuisne} is made in ${self.countryoforigin} and helps with {self.nutrionvalue}"
    def preparation0fcuisine(self,timetaken,ingredient,quantity):
        timetaken=self.preparationtime+timetaken
        self.ingredients[ingredient]=quantity
        return f"{self.nameofcuisne} takes ${timetaken} to be ready and it prepared with ${self.ingredients}"
class NigerianRecipe(Recipe):
    def __init__(self, nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue):
        super().__init__(nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue)
    def describeCuisine(self):
        return super().describeCuisine()
    def preparation(self, timetaken,ingredient,quantity):
          timetaken=self.preparationtime+timetaken
          self.ingredients[ingredient]=quantity
          return f"{self.nameofcuisne} takes ${timetaken} to be ready and it prepared with ${self.ingredients}"

# 
class Wildlife:
    def __init__(self,nameofpark,species,speciestype):
        self.nameofpark=nameofpark
        self.species=species
        self.nameofpark=nameofpark
        self.speciestype=speciestype
    
    def  describeSpecies(self):
        return f"${self.species} is a ${self.speciestype} and is found in ${self.nameofpark}"
    

class Species(Wildlife):
    def __init__(self,nameofpark,species,speciestype,diet,lifespan,migrationpattern):
        super().__init__(nameofpark,species,speciestype)
        self.diet=diet
        self.lifespan=lifespan
        self.migrationpattern=migrationpattern
    
    def dietofspecies(self):
        return f"{self.species} feeds on ${self.diet}"
    
    def migrationPattern(self,riverlevel,currentweather):
        self.riverlevel=riverlevel
        self.currentweather=currentweather
        if(self.riverlevel=="low" and self.currentweather=="dry"):
            return f"{self.species} will move south in search of pasture"
        
        else:
            return f"{self.species} will stay in {self.nameofpark} because there is enough food and water"
        
       
    

class Predator(Species):
    def __init__(self,nameofpark,species,speciestype,diet,lifespan,migrationpattern):
        super().__init__(nameofpark,species,speciestype)
        
# question5
# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculatetotal(self):
        total=self.quantity*self.price
        return total
product1=Product("lotion",400,3)
print(product1.calculatetotal())
product2=Product("cookingoil",200,5)
print(product2.calculatetotal())
# // question6
# // Implement a class called Student with attributes for name, age, and grades (a
# //     list of integers). Include methods to calculate the average grade, display the
# //     student information, and determine if the student has passed (average grade >=
# //     60). Create objects for the Student class and demonstrate the usage of these
# //     methods.
        
class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    
    def calculateAverage(self):
        average=sum(self.grades)/len(self.grades)
        if average >60:
            return f"{self.name} has paased"
        else:
            return f"{self.name} is below average"
student1=Student("loice",20,[50,60,70,60])
print(student1.calculateAverage())
student2=Student("marion",32,[69,60,75,65,90])
print(student2.calculateAverage())


      
        
    

    


     
    


       
        