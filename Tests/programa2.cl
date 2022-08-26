class Main {
   
   current_number : Int  <- 1;
   last_number : Int  <- 1;
   back_up_number : Int;
   n : Int;
   control : Bool <- true;

   main() : Int {
      {
         n <- in_int();
         out_int(current_number);
         (let y : Int <- 1 in
            while(control) loop {
               back_up_number <- current_number;
               current_number <- current_number + last_number;
               last_number <- back_up_number;
               out_int(current_number);
               n <- n-1; 
            } pool
         );
         n;
      }
   };
};
