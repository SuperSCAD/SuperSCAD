// Unit of length: Unit.MM
translate(v = [0.0, 0.0, -1.0])
{
   linear_extrude(height = 21.0, center = false, twist = 0.0, scale = 1.0)
   {
      circle(d = 2.0);
   }
}
