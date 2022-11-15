class Main {
   
   current_number : Int  <- 1;
   last_number : Int  <- 1;
   back_up_number : Int;
   n : Int;
   control : Bool <- true;

   main() : Int {
      {
         n <- 60;
         if control then n <- n+1 else n <- 0 fi;
         n;
      }
   };
};
