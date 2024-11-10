// Unit of length: Unit.MM
union()
{
   translate(v = [-20.0, 0.0, 0.0])
   {
      difference()
      {
         intersection()
         {
            cube(size = 30.0, center = true);
            sphere(d = 45.0, $fn = 50);
         }
         translate(v = [15.0, 0.0, 0.0])
         {
            sphere(d = 6.0, $fn = 50);
         }
         union()
         {
            translate(v = [-7.5, 15.0, 7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, 15.0, -7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
         }
         union()
         {
            translate(v = [-7.5, 7.5, 15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [0.0, 0.0, 15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, -7.5, 15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
         }
         union()
         {
            translate(v = [-7.5, 7.5, -15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-7.5, -7.5, -15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, 7.5, -15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, -7.5, -15.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
         }
         union()
         {
            translate(v = [-7.5, -15.0, 7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-7.5, -15.0, -7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [0.0, -15.0, 0.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, -15.0, 7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [7.5, -15.0, -7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
         }
         union()
         {
            translate(v = [-15.0, -7.5, -7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-15.0, -7.5, 0.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-15.0, -7.5, 7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-15.0, 7.5, -7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-15.0, 7.5, 0.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            translate(v = [-15.0, 7.5, 7.5])
            {
               sphere(d = 6.0, $fn = 50);
            }
         }
      }
   }
   translate(v = [20.0, 0.0, 0.0])
   {
      rotate(a = [180.0, 0.0, 0.0])
      {
         difference()
         {
            intersection()
            {
               cube(size = 30.0, center = true);
               sphere(d = 45.0, $fn = 50);
            }
            translate(v = [15.0, 0.0, 0.0])
            {
               sphere(d = 6.0, $fn = 50);
            }
            union()
            {
               translate(v = [-7.5, 15.0, 7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, 15.0, -7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
            }
            union()
            {
               translate(v = [-7.5, 7.5, 15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [0.0, 0.0, 15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, -7.5, 15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
            }
            union()
            {
               translate(v = [-7.5, 7.5, -15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-7.5, -7.5, -15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, 7.5, -15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, -7.5, -15.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
            }
            union()
            {
               translate(v = [-7.5, -15.0, 7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-7.5, -15.0, -7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [0.0, -15.0, 0.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, -15.0, 7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [7.5, -15.0, -7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
            }
            union()
            {
               translate(v = [-15.0, -7.5, -7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-15.0, -7.5, 0.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-15.0, -7.5, 7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-15.0, 7.5, -7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-15.0, 7.5, 0.0])
               {
                  sphere(d = 6.0, $fn = 50);
               }
               translate(v = [-15.0, 7.5, 7.5])
               {
                  sphere(d = 6.0, $fn = 50);
               }
            }
         }
      }
   }
}
