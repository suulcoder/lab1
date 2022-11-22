class Main {

   resultado : Int;
   control : Bool;

   factorial(number : Int ) : Int {
      {
         control <- number = 1;
         if control then 1 else number <- number * factorial(number - 1) fi;
         number;
      }
   };

   main() : Int {
      {
         resultado <- factorial(4);
         out_int(resultado);
         0;
      }
   };
};

