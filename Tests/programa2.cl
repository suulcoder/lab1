class Main {
   
   current_number : Int  <- 1;
   last_number : Int  <- 1;
   back_up_number : Int;
   n : Int;
   control : Bool <- true;

   main() : Int {
      {
         n <- 5;
         control <- not n = 0; 
         while(control) loop {
            back_up_number <- current_number;
            current_number <- current_number + last_number;
            last_number <- back_up_number;
            n <- n-1;
            control <- not n = 0; 
         } pool;
         out_int(last_number);
         n;
      }
   };
};

