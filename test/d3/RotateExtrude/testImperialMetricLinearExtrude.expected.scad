// Unit of length: Unit.MM
rotate_extrude(angle = 360.0, convexity = 10, $fs = 0.254)
{
   translate(v = [25.4, 0.0])
   {
      circle(d = 25.4, $fn = 100);
   }
}
