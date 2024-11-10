// Unit of length: Unit.INCH
rotate_extrude(angle = 360.0, convexity = 10, $fs = 0.01)
{
   translate(v = [1.0, 0.0])
   {
      circle(d = 1.0, $fn = 100);
   }
}
