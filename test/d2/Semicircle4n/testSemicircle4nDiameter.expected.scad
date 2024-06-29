// Unit of length: Unit.MM
intersection()
{
   circle(d = 20.0, $fn = 360);
   translate(v = [-10.01, 0.0])
   {
      square(size = [20.02, 10.01], center = false);
   }
}
