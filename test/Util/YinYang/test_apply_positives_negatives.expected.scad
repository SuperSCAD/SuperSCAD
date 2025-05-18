// Unit of length: Unit.MM
difference()
{
   union()
   {
      square(size = 100.0, center = true);
      square(size = [120.0, 10.0], center = true);
   }
   square(size = 25.0, center = true);
}
