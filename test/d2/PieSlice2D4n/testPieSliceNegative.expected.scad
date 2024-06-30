// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(r = 0.0);
   }
   rotate(a = 270.0)
   {
      square(size = 30.02, center = false);
   }
   rotate(a = 340.0)
   {
      square(size = 30.02, center = false);
   }
}
