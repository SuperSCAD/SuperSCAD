// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, convexity = 1, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(r = 30.0);
      polygon(points = [[0.0, 0.0], [30.01, -8.0412], [30.01, 8.0412]], convexity = 1);
   }
}
