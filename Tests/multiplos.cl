class Main {
   
   n : Int;
   --m : Int <- 2;
   --m : Int <- 3;
   m : Int <- 5;
   --m : Int <- 7;
   control : Bool <- true;

   main() : Int {
      {
         n <- 0;
         control <- not n = 210; 
         while(control) loop {
            n <- n+5;
            control <- not n = 210; 
         } pool;
         out_int(n);
         n;
      }
   };
};

