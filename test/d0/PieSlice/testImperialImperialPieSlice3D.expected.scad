// Unit of length: Unit.INCH
linear_extrude(height = 10.0, center = false, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 60.0, $fa = 12.0, $fs = 2.0, $fn = 0);
      polygon(points = [[0.0, 0.0], [33.4718, 8.9687], [0.0, 42.4405], [-42.4405, 0.0], [0.0, -42.4405], [33.4718, -8.9687]], convexity = 2);
   }
}
