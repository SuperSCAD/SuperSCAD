// Unit of length: Unit.MM
union()
{
   square(size = 10.0, center = false);
   translate(v = [15.0, 0.0])
   {
      scale(v = [2.0, 2.0])
      {
         square(size = 10.0, center = false);
      }
   }
}
