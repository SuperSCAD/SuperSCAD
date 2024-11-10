// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 10, twist = 0.0, scale = 3.0)
{
   translate(v = [2.0, 0.0])
   {
      circle(d = 2.0);
   }
}
