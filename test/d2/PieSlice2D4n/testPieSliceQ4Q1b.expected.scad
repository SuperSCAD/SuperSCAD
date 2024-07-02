// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(d = 20.0, $fn = 360);
   }
   polygon(points = [[0.0, 0.0], [0.0074, -42.429], [42.4364, 0.0], [0.0, 42.4364], [0.0074, 42.429]], convexity = 2);
}
