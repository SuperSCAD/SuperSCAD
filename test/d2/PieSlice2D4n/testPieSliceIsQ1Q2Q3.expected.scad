// Unit of length: Unit.MM
intersection()
{
   circle(d = 60.0, $fn = 360);
   polygon(points = [[0.0, 0.0], [30.01, 0.0], [30.0071, 30.0071], [-30.0071, 30.0071], [-30.0071, -30.0071], [0.0, -30.01]], convexity = 2);
}
