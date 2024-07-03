// Unit of length: Unit.MM
difference()
{
   cylinder(h = 4.0, r = 1.0, center = true, $fn = 100);
   rotate(a = [90.0, 0.0, 0.0])
   {
      cylinder(h = 4.0, r = 0.9, center = true, $fn = 100);
   }
}
