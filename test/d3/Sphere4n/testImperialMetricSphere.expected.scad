// Unit of length: Unit.MM
rotate_extrude(angle = 360.0, $fn = 360)
{
   rotate(a = 270.0)
   {
      intersection()
      {
         circle(d = 1016.0, $fn = 360);
         translate(v = [-508.254, 0.0])
         {
            square(size = [1016.508, 508.254], center = false);
         }
      }
   }
}
