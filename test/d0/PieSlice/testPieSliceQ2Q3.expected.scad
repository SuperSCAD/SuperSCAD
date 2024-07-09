// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [-30.01, 5.2916], [-30.01, -5.2916]], convexity = 1);
}
