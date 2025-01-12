// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0, -0.5])
      {
         cube(size = [40.0, 20.0, 11.0], center = true);
      }
   }
   translate(v = [0.0, 0.0, 0.5])
   {
      cube(size = [42.0, 22.0, 11.0], center = true);
   }
}
