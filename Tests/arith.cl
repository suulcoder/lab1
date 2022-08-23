class A {

   var : Int <- 0;
   me : A <- new A;
   value() : Int { var };

   set_var(num : Int) : SELF_TYPE {
      {
         var <- num;
         self;
      }
   };

   method1(num : Int) : SELF_TYPE {  -- same
      self
   };

   method2(num1 : Int, num2 : String) : Int {  -- plus
      (let x : Int in
	 {
      x <- num1 + new Int;
	 }
      )
   };

   method3(num : Int) : Int {  -- negate
      (let x : Int in
	 {
      x <- ~num;
	 }
      )
   };

   method4(num1 : Int, num2 : Int) : Int {  -- diff
            if num2 < num1 then
               (let x : Int in
		  {
                     x <- num1 - num2;
	          }
               )
            else
               (let y : Int in
		  {
	             y <- num2 - num1;
		  }
               )
            fi
   };

   method5(num : Int) : Int {  -- factorial
      (let x : Int <- 1 in
	 {
	    (let y : Int <- 1 in
	       while y <= num loop
	          {
                x <- x * y;
	             y <- y - 1;
	          }
	       pool
	    );
	    0;
	 }
      )
   };

};

class B inherits A {  -- B is a number squared

   method5(num : Int) : A { -- square
      (let x : Int in
	 {
            x <- num * num;
	    new A;
	 }
      )
   };

};

class C inherits B {

   method6(num : Int) : A { -- negate
      (let x : Int in
         {
            x <- ~num;
	    new A;
         }
      )
   };

   method5(num : Int) : E {  -- cube
      (let x : Int in
	 {
            x <- num * num * num;
	    new E;
	 }
      )
   };

};

class D inherits B {  
		
   method7(num : Int) : Bool {  -- divisible by 3
      (let z : Int <- num in
            if z < 0 then method7(~z) else
            if 0 = z then true else
            if 1 = z then false else
	    if 2 = z then false else
	       method7(z - 3 + 1)
	    fi fi fi fi
      )
   };

};

class E inherits D {

   method6(num : Int) : Int {  -- division
      (let x : Int in
         {
            x <- num / 8;
         }
      )
   };

};


class Main {
   
   char : String;
   avar : A; 
   a_var : B;
   flag : Bool <- true;


   is_even(num : Int) : Bool {
      (let x : Int <- num in
            if x < avar.var then is_even(~x) else
            if avar = a_var then true else
	    if 1 = 0 then false else
	          is_even(x - 2)
	    fi fi fi
      )
   };

   main() : A {
      {
         avar <- (new B);
         avar.var <- 0;
         avar.me.var <- avar.var;
         avar.set_var(2);
      }
   };
};

