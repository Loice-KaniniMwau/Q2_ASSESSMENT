// pseudo code 
// input - define length of story ,moral lessons and its age group
// process-define a class Ancestral stories which will help describe the story.
// output-ancestral stories with their description and their storytellers , the translators

//define length,moral lessons and the age group for the stories..create a class 
class Ancestral_Stories{
constructor(length,morallessons,age,nameofstory){
    this.length=length
    this.morallessons=morallessons
    this.age=age
    this.nameofstory=nameofstory
}
define_story(){
    console.log(`${this.nameofstory} teaches us to be ${this.morallessons} and targets ${this.age}`);
}

}
class Story extends Ancestral_Stories{
    constructor(length,morallessons,age,nameofstory,typeofstory){
        super(length,morallessons,age,nameofstory)
        this.typeofstory=typeofstory
    }
    define_story(){
        console.log(`${this.nameofstory} which is a ${this.typeofstory}teaches us to be ${this.morallessons} and targets ${this.age}`);
    }

}
class StoryTeller extends Ancestral_Stories{

}

// question2
// # pseudo code 
// # input-define the names different african cusines,their unique ingredients, preparation time, cooking method, and nutritional
// # information
// # process-define class Recipe where the african cusines will inherit from and have their unique methods
// # output-well defined african cusines with their descriptions and their preparation process
class Recipe{
constructor(nameofcuisine,countryoforigin,cookingmethod,nutritionalvalue,ingredients){
    self.nameofcuisne=nameofcuisine
    self.cookingmethod=cookingmethod
    self.countryoforigin=countryoforigin
    self.ingredients=ingredients
    self.preparationtime=0
    self.nutrionvalue=nutritionalvalue
}
describeCuisine(){
 return `${this.nameofcuisne} is originally from ${this.countryoforigin} and helps with ${this.nutrionvalue}`
}
}
class Morocanrecipe extends Recipe{
    constructor(nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue){
       super(nameofcuisine, countryoforigin, cookingmethod, nutritionalvalue)
    }
    describeCuisine(){
       return super().describeCuisine
    }
    preparationtime(timetaken,ingredient,quantity){
        timetaken=this.preparationtime+=timetaken
        this.ingredient=ingredient
        this.quantity=quantity
        return `${this.nameofcuisine} takes ${timetaken} to be prepared and is prepared with ${this.ingredient}`
    }

}

// question3
// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.
class Wildlife{
    constructor(nameofpark,species,speciestype){
        this.nameofpark=nameofpark
        this.species=species
        this.nameofpark=nameofpark
        this.speciestype=speciestype
    }
    describeSpecies(){
        return `${this.species} is a ${this.speciestype} and is found in ${this.nameofpark}`
    }
}
class Species extends Wildlife{
    constructor(nameofpark,species,speciestype,diet,lifespan,migrationpattern){
        super(nameofpark,species,speciestype)
        this.diet=diet
        this.lifespan=lifespan
        this.migrationpattern=migrationpattern
    }
    dietofspecies(){
        return `${this.species} feeds on ${this.diet}`
    }
    migrationPattern(riverlevel,currentweather){
        this.riverlevel=riverlevel
        this.currentweather=currentweather
        if(this.riverlevel=="low" && this.currentweather=="dry"){
            return `${this.species} will move south in search of pasture  `
        }
        else {
            return `${this.species} will stay in ${this.nameofpark} because there is enough food and water`
        }
       
    }
}
class Predator extends Species{
    constructor(nameofpark,species,speciestype,diet,lifespan,migrationpattern){
        super(nameofpark,species,speciestype)
        this.diet=diet
        this.lifespan=lifespan
        this.migrationpattern=migrationpattern
    }
    dietofspecies(){
        return super.dietofspecies
    }

}

// # question5
// # Create a class called Product with attributes for name, price, and quantity.
// # Implement a method to calculate the total value of the product (price * quantity).
// # Create multiple objects of the Product class and calculate their total values.
class Product{
    constructor(name,price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }
    calculatetotal(){
        total=this.price*this.quantity
        return total
    }
}
// question6
// Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.
class Student{
    constructor(name,age,grades){
        this.name=name
        this.age=age
        this.grades=grades
    }
    calculateAverage(){
        let sum=this.grades.reduce((total,each)=>total+each,0)
        average=sum/this.grades.length
        if(average>60){
            return `${this.name} has passed`
        }
        else{
            return `${this.name} has failed`
        }
        
    }
}
       

  
