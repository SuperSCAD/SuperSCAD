// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 2, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 1524.0, $fn = 360);
      polygon(points = [[0.0, 0.0], [850.1839, 227.8061], [0.0, 1077.9899], [-1077.9899, 0.0], [0.0, -1077.9899], [850.1839, -227.8061]], convexity = 2);
   }
}
