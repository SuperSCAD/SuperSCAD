// Unit of length: Unit.MM
difference()
{
   cube(size = 10.0, center = true);
   translate(v = [0.0, 0.0, 5.0])
   {
      union()
      {
         rotate(a = [0.0, 90.0, 0.0])
         {
            cylinder(h = 20.0, d = 4.0, center = true, $fn = 40);
         }
         *union()
         {
            rotate(a = [90.0, 0.0, 0.0])
            {
               #union()
               {
                  cylinder(h = 20.0, d = 4.0, center = true, $fn = 40);
               }
            }
         }
      }
   }
}
