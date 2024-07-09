// Unit of length: Unit.MM
rotate_extrude(angle = 360.0, convexity = 10, $fn = 100)
{
   translate(v = [2.0, 0.0])
   {
      circle(d = 2.0, $fn = 100);
   }
}
