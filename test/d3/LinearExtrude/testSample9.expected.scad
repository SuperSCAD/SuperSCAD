// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = true, convexity = 10, twist = 0.0, scale = [1.0, 5.0], slices = 20, $fn = 100)
{
   translate(v = [2.0, 0.0])
   {
      circle(r = 1.0);
   }
}
