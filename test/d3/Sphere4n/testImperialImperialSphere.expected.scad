// Unit of length: Unit.INCH
rotate_extrude(angle = 360.0, $fn = 360)
{
   rotate(a = 270.0)
   {
      intersection()
      {
         circle(d = 40.0, $fn = 360);
         translate(v = [-20.01, 0.0])
         {
            square(size = [40.02, 20.01], center = false);
         }
      }
   }
}
