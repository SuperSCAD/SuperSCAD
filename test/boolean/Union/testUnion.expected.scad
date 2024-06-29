// Unit of length: Unit.MM
union()
{
   cylinder(h = 4, r = 1, center = true, $fn = 100);
   rotate(a = [90.0, 0.0, 0.0])
   {
      cylinder(h = 4, r = 0.9, center = true, $fn = 100);
   }
}
