class Main {
   
   n : Int;
   control : Bool <- true;

   main() : Int {
      {
         n <- 100;
         while(control) loop control<-false pool;
         n;
      }
   };
};
