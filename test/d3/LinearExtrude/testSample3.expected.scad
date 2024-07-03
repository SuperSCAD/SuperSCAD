// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = true, convexity = 10, twist = 100.0, scale = 1.0)
{
   translate(v = [2.0, 0.0])
   {
      circle(r = 1.0);
   }
}
