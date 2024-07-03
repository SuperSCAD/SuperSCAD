// Unit of length: Unit.MM
union()
{
   translate(v = [0.01, 60.0, 0.0])
   {
      rotate_extrude(angle = 270.0, convexity = 10)
      {
         translate(v = [40.0, 0.0])
         {
            circle(r = 10.0);
         }
      }
   }
   rotate_extrude(angle = 90.0, convexity = 10)
   {
      translate(v = [20.0, 0.0])
      {
         circle(r = 10.0);
      }
   }
   translate(v = [20.0, 0.01])
   {
      rotate(a = [90.0, 0.0, 0.0])
      {
         cylinder(h = 80.01, r = 10.0, center = false);
      }
   }
}
