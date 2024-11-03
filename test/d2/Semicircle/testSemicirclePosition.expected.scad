// Unit of length: Unit.MM
translate(v = [30.0, 20.0])
{
   intersection()
   {
      circle(d = 20.0);
      translate(v = [-10.01, 0.0])
      {
         square(size = [20.02, 10.01], center = false);
      }
   }
}
