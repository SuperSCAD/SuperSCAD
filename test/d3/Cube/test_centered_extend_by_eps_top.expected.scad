// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0, 0.5])
      {
         cube(size = [10.0, 10.0, 11.0], center = true);
      }
   }
   translate(v = [0.0, 0.0, -0.5])
   {
      cube(size = [12.0, 12.0, 11.0], center = true);
   }
}
