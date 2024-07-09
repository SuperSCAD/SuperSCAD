// Unit of length: Unit.MM
linear_extrude(height = 254.0, center = false, twist = 0.0, scale = 1.0)
{
   intersection()
   {
      circle(d = 1016.0, $fa = 12.0, $fs = 50.8, $fn = 0);
      translate(v = [-508.01, 0.0])
      {
         square(size = [1016.02, 508.01], center = false);
      }
   }
}
