// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [-5.2915, -30.0098], [5.2915, -30.0098]], convexity = 2);
}
