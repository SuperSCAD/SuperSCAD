// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 10, twist = -500.0, scale = 1.0)
{
   translate(v = [2.0, 0.0])
   {
      circle(r = 1.0);
   }
}
