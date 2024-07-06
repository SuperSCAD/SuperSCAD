// Unit of length: Unit.MM
linear_extrude(height = 254.0, center = false, convexity = 2, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 1524.0, $fn = 360);
      polygon(points = [[0.0, 0.0], [849.9117, 227.7332], [0.0, 1077.6449], [-1077.6449, 0.0], [0.0, -1077.6449], [849.9117, -227.7332]], convexity = 2);
   }
}
