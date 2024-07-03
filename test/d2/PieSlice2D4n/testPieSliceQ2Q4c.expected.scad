// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(d = 20.0, $fn = 360);
   }
   polygon(points = [[0.0, 0.0], [-30.01, 0.0052], [-30.01, -30.01], [30.01, -30.01], [0.0052, -30.01]], convexity = 1);
}
