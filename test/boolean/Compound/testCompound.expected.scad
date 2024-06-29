// Unit of length: Unit.MM
union()
{
   cube(size = 2.0, center = true);
   translate(v = [5.0, 0.0, 0.0])
   {
      sphere(r = 1.0);
   }
}
