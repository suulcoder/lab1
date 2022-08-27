class Main {
   
   myString1 : String  <- "Hola ";
   myString2 : String  <- " un gusto!";
   nombre : String;

   main() : String {
      {
         nombre <- in_string();
         nombre <- myString1 + nombre + myString2;
         out_string(nombre33);
         nombre;
      }
   };
};

