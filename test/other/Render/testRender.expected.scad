// Unit of length: Unit.MM
render(convexity = 2)
{
   difference()
   {
      cube(size = [20.0, 20.0, 150.0], center = true);
      translate(v = [-10.0, -10.0, 0.0])
      {
         cylinder(h = 80.0, d = 20.0, center = true);
      }
      translate(v = [-10.0, -10.0, 40.0])
      {
         sphere(r = 10.0);
      }
      translate(v = [-10.0, -10.0, -40.0])
      {
         sphere(r = 10.0);
      }
   }
}
