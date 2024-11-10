// Unit of length: Unit.MM
intersection()
{
   circle(d = 4.0, $fn = 8);
   translate(v = [-2.01, 0.0])
   {
      square(size = [4.02, 2.01], center = false);
   }
}
