// Unit of length: Unit.MM
$fn = 60;

union()
{
   cylinder(h = 10.0, d = 1.0, center = true);
   translate(v = [2.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, -5.0])
      {
         cylinder(h = 11.0, d = 1.0, center = false);
      }
   }
   translate(v = [4.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, -6.0])
      {
         cylinder(h = 11.0, d = 1.0, center = false);
      }
   }
   translate(v = [6.0, 0.0, 0.0])
   {
      cylinder(h = 12.0, d = 1.0, center = true);
   }
   translate(v = [9.0, 0.0, 0.0])
   {
      cylinder(h = 10.0, d = 3.0, center = true);
   }
}
