// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(d = 20.0, $fn = 360);
   }
   polygon(points = [[0.0, 0.0], [5.2916, 30.01], [-5.2916, 30.01]], convexity = 1);
}
