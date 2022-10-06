class Person {
   name : String;
   energy : Int <- 100;
   
   walk(steps : Int) : Int {
      {
         energy <- energy - steps;
         energy;
      }
   };
};

class Main {

   a : Int <- 0;
   b : Int <- 1;
   c : Int;
   d : Person;

   main() : Int {
      {
         c <- in_int();
         d <- new Person;
         a <- d.energy;
         d.walk(0);
         while isvoid b loop if a<c then  a + a * (b - c) + (b -c) * 4 else a * a fi pool;
         out_int(b);
         out_int(2);
         0;
      }
   };

   hello(here: Int) : Int {
      {
         0;
      }
   };
};