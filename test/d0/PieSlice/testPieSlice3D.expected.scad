// Unit of length: Unit.MM
linear_extrude(height = 10.0, center = false, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      difference()
      {
         circle(d = 60.0);
         circle(d = 20.0);
      }
      polygon(points = [[0.0, 0.0], [36.0789, 6.3617], [6.3617, 36.0789]], convexity = 1);
   }
}
