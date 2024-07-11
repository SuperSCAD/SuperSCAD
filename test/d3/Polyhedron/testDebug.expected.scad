// Unit of length: Unit.ROYAL_CUBIT
union()
{
   polyhedron(points = [[0.0, 0.0, 0.0], [440.0, 0.0, 0.0], [440.0, 440.0, 0.0], [0.0, 440.0, 0.0], [220.0, 220.0, 280.0]], faces = [[0, 1, 2, 3], [0, 4, 1], [1, 4, 2], [2, 4, 3], [3, 4, 0]]);
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         sphere(d = 35.2, $fn = 16);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [440.0, 0.0, 0.0])
      {
         sphere(d = 35.2, $fn = 16);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [440.0, 440.0, 0.0])
      {
         sphere(d = 35.2, $fn = 16);
      }
   }
   color(c = [0.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 440.0, 0.0])
      {
         sphere(d = 35.2, $fn = 16);
      }
   }
   color(c = [0.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 90.0, 0.0])
         {
            cylinder(h = 440.0, d = 7.04, center = false, $fn = 16);
         }
      }
   }
   color(c = [0.0, 0.0, 0.0, 1.0])
   {
      translate(v = [440.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 90.0, 90.0])
         {
            cylinder(h = 440.0, d = 7.04, center = false, $fn = 16);
         }
      }
   }
   color(c = [0.0, 0.0, 0.0, 1.0])
   {
      translate(v = [440.0, 440.0, 0.0])
      {
         rotate(a = [0.0, 90.0, 180.0])
         {
            cylinder(h = 440.0, d = 7.04, center = false, $fn = 16);
         }
      }
   }
   color(c = [0.0, 0.0, 0.0, 1.0])
   {
      translate(v = [0.0, 440.0, 0.0])
      {
         rotate(a = [0.0, 90.0, -90.0])
         {
            cylinder(h = 440.0, d = 7.04, center = false);
         }
      }
   }
}
