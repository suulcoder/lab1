class Person {
   name : String;
   energy : Int <- 100;
   energy_bool : Bool <- false;
   
   walk(steps : Int) : Int {
      {
         energy <- energy - steps;
         energy;
      }
   };
};

class Main {
   
   my_person : Person  <- (new Person);
   new_energy : Int;

   print(my_string: String) : String {
      {
         out_string(my_string);
         my_string;
      }
   };

   main() : Person {
      {
         print("Type the name of your character: ");
         my_person.name <- in_string();
         print("Type the number of steps you want it to walk: ");
         new_energy <- my_person.walk(2);
         print("The energy of your character is: ");
         out_int(new_energy);
         my_person;
      }
   };
};

