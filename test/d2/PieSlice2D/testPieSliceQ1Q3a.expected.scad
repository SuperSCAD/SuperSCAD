// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [29.4345, 7.8869], [27.2776, 32.5082], [-32.5082, 27.2776], [-27.2776, -32.5082], [-2.6559, -30.3568]], convexity = 2);
}
