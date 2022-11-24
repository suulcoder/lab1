class Main {
   
   a : Int  <- 60;
   b : Int  <- 15;
   c : Bool;
   d : Int <- 1;

   main() : Int {
      {
         c <- b < a;
         if c then d <- 1000 else d <- 0 fi;
         0;
      }
   };
};
