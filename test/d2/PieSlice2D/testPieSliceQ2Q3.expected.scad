// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [-30.01, 5.2916], [-30.01, -5.2916]], convexity = 2);
}
