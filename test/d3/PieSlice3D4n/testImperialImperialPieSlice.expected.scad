// Unit of length: Unit.INCH
linear_extrude(height = 10.0, center = false, convexity = 2, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 60.0, $fn = 360);
      polygon(points = [[0.0, 0.0], [33.4718, 8.9687], [0.0, 42.4405], [-42.4405, 0.0], [0.0, -42.4405], [33.4718, -8.9687]], convexity = 2);
   }
}