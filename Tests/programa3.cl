class Person {
   name : String;
   energy : Int <- 100;
   
   walk(steps : Int) : SELF_TYPE {
      {
         energy <- energy - steps;
         self;
      }
   };
};

class Main {
   
   my_person : Person  <- (new Person);

   print(my_string: String) : SELF_TYPE {
      {
         out_string(my_string);
      }
   };

   main() : Person {
      {
         print("Type the name of your character: ");
         my_person.name <- in_string();
         print("Type the number of steps you want it to walk: ");
         my_person <- my_person.walk(in_int());
         print("The energy of your character is: ");
         out_int(my_person.energy);
         my_person;
      }
   };
};

