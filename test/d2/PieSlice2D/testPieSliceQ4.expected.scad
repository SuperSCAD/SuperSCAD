// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [6.3617, -36.0789], [36.0789, -6.3617]], convexity = 2);
}
