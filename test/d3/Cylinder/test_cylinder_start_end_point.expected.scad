// Unit of length: Unit.MM
union()
{
   translate(v = [3.0, 2.0, 1.0])
   {
      rotate(a = [0.0, 74.4986, 33.6901])
      {
         cylinder(h = 33.6749, d = 0.1, center = false, $fn = 64);
      }
   }
   %union()
   {
      translate(v = [3.0, 2.0, 1.0])
      {
         cube(size = [27.0, 18.0, 9.0], center = false);
      }
   }
}
