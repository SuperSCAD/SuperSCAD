// Unit of length: Unit.MM
union()
{
   cube(size = 10.0, center = false);
   translate(v = [15.0, 0.0, 0.0])
   {
      scale(v = [2.0, 2.0, 2.0])
      {
         cube(size = 10.0, center = false);
      }
   }
}
