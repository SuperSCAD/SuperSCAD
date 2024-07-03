// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [0.0052, 30.01], [-30.01, 30.01], [-30.01, -30.01], [-30.01, -0.0052]], convexity = 1);
}
