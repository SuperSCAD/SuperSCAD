// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [0.0074, -42.4331], [42.4405, 0.0], [0.0, 42.4405], [0.0074, 42.4331]], convexity = 1);
}
