// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(d = 20.0, $fn = 360);
   }
   polygon(points = [[0.0, 0.0], [-7.8869, 29.4345], [-32.5082, 27.2776], [-27.2776, -32.5082], [32.5082, -27.2776], [30.3568, -2.6559]], convexity = 2);
}
