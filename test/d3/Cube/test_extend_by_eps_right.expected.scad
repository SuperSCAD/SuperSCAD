// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      cube(size = [11.0, 10.0, 10.0], center = false);
   }
   translate(v = [-1.0, -1.0, -1.0])
   {
      cube(size = [11.0, 12.0, 12.0], center = false);
   }
}
