// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, -0.5, 0.0])
      {
         cube(size = [40.0, 21.0, 10.0], center = true);
      }
   }
   translate(v = [0.0, 0.5, 0.0])
   {
      cube(size = [42.0, 21.0, 12.0], center = true);
   }
}
