// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 2, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 60.0, $fn = 360);
      polygon(points = [[0.0, 0.0], [30.01, -8.0412], [30.01, 8.0412]], convexity = 2);
   }
}
