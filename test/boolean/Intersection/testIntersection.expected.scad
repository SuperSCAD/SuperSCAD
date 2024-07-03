// Unit of length: Unit.MM
intersection()
{
   cylinder(h = 4.0, d = 2.0, center = true, $fn = 100);
   rotate(a = [90.0, 0.0, 0.0])
   {
      cylinder(h = 4.0, d = 1.8, center = true, $fn = 100);
   }
}
