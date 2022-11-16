class Main {
   
   current_number : Int  <- 1;
   last_number : Int  <- 1;
   control : Bool;

   main() : Int {
      {
         control <- true;
         if control then current_number <- 0 else last_number <- 0 fi;
      }
   };
};
