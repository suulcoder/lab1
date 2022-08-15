class A {

   var : Int <- 0;
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

   method2(num1 : String, num2 : String) : B {  -- plus
      (let x : String in
	 {
            x <- num1 + num2;
	    (new B).set_var(x);
	 }
      )
   };

   method3(num : Int) : C {  -- negate
      (let x : Int in
	 {
            x <- ~num;
	    (new C).set_var(x);
	 }
      )
   };

   method4(num1 : Int, num2 : Int) : D {  -- diff
            if num2 < num1 then
               (let x : Int in
		  {
                     x <- num1 - num2;
	             (new D).set_var(x);
	          }
               )
            else
               (let x : Int in
		  {
	             x <- num2 - num1;
	             (new D).set_var(x);
		  }
               )
            fi
   };

   method5(num : Int) : E {  -- factorial
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
	    (new E).set_var(x);
	 }
      )
   };

};

class B inherits A {  -- B is a number squared

   method5(num : Int) : E { -- square
      (let x : Int in
	 {
            x <- num * num;
	    (new E).set_var(x);
	 }
      )
   };

};

class C inherits B {

   method6(num : Int) : A { -- negate
      (let x : Int in
         {
            x <- ~num;
	    (new A).set_var(x);
         }
      )
   };

   method5(num : Int) : E {  -- cube
      (let x : Int in
	 {
            x <- num * num * num;
	    (new E).set_var(x);
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

   method6(num : Int) : A {  -- division
      (let x : Int in
         {
            x <- num / 8;
	    (new A).set_var(x);
         }
      )
   };

};


class Main {
   
   char : String;
   avar : A; 
   a_var : A;
   flag : Bool <- true;



   is_even(num : Int) : Bool {
      (let x : Int <- num in
            if x < 0 then is_even(~x) else
            if 0 = x then true else
	    if 1 = x then false else
	          is_even(x - 2)
	    fi fi fi
      )
   };

   main() : Object {
      {
         avar <- (new A);
         avar.set_var(2);

      }
   };
};

