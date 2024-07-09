// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 10, twist = -360.0, scale = 1.0, $fn = 100)
{
   translate(v = [2.0, 0.0])
   {
      circle(d = 2.0);
   }
}
