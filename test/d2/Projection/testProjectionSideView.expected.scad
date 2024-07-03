// Unit of length: Unit.MM
projection(cut = false)
{
   translate(v = [0.0, 0.0, 25.0])
   {
      rotate(a = [90.0, 0.0, 0.0])
      {
         intersection()
         {
            difference()
            {
               union()
               {
                  cube(size = 30.0, center = true);
                  translate(v = [0.0, 0.0, -25.0])
                  {
                     cube(size = [15.0, 15.0, 50.0], center = true);
                  }
               }
               union()
               {
                  cube(size = [50.0, 10.0, 10.0], center = true);
                  cube(size = [10.0, 50.0, 10.0], center = true);
                  cube(size = [10.0, 10.0, 50.0], center = true);
               }
            }
            translate(v = [0.0, 0.0, 5.0])
            {
               cylinder(h = 50.0, r2 = 5.0, r1 = 20.0, center = true);
            }
         }
      }
   }
}
