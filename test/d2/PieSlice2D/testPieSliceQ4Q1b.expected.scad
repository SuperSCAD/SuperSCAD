// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(r = 30.0);
      circle(r = 10.0);
   }
   polygon(points = [[0.0, 0.0], [0.0074, -42.429], [42.4364, -0.0], [0.0, 42.4364], [0.0074, 42.429]], convexity = 2);
}
