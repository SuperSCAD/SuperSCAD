// Unit of length: Unit.MM
rotate_extrude(angle = 360.0, $fn = 64)
{
   rotate(a = 270.0)
   {
      intersection()
      {
         circle(d = 2.0, $fn = 64);
         translate(v = [-1.01, 0.0])
         {
            square(size = [2.02, 1.01], center = false);
         }
      }
   }
}
