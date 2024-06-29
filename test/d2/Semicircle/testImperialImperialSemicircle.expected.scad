// Unit of length: Unit.INCH
intersection()
{
   circle(d = 40.0, $fa = 12.0, $fs = 2.0, $fn = 0);
   translate(v = [-20.01, 0.0])
   {
      square(size = [40.02, 20.01], center = false);
   }
}
