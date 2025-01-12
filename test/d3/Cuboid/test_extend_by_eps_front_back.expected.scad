// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, -1.0, 0.0])
      {
         cube(size = [40.0, 22.0, 10.0], center = false);
      }
   }
   translate(v = [-1.0, 0.0, -1.0])
   {
      cube(size = [42.0, 20.0, 12.0], center = false);
   }
}