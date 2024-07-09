// Unit of length: Unit.MM
rotate_extrude(angle = 360.0, $fn = 128)
{
   rotate(a = 270.0)
   {
      intersection()
      {
         circle(d = 4.0, $fn = 128);
         translate(v = [-2.01, 0.0])
         {
            square(size = [4.02, 2.01], center = false);
         }
      }
   }
}
