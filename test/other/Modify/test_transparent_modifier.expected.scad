// Unit of length: Unit.MM
difference()
{
   cylinder(h = 12.0, d = 10.0, center = true, $fn = 100);
   rotate(a = [90.0, 0.0, 0.0])
   {
      cylinder(h = 15.0, d = 2.0, center = true, $fn = 100);
   }
   %union()
   {
      rotate(a = [0.0, 90.0, 0.0])
      {
         cylinder(h = 15.0, d = 6.0, center = true, $fn = 100);
      }
   }
}
