// Unit of length: Unit.MM
$fn = 60;

union()
{
   translate(v = [0.0, 0.0, 0.0])
   {
      rotate(a = [0.0, 54.7356, 45.0])
      {
         cylinder(h = 17.3205, d = 1.0, center = false);
      }
   }
   translate(v = [10.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 54.7356, 45.0])
         {
            cylinder(h = 18.3205, d = 1.0, center = false);
         }
      }
   }
   translate(v = [20.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 54.7356, 45.0])
         {
            translate(v = [0.0, 0.0, -1.0])
            {
               cylinder(h = 18.3205, d = 1.0, center = false);
            }
         }
      }
   }
   translate(v = [30.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 54.7356, 45.0])
         {
            translate(v = [0.0, 0.0, -1.0])
            {
               cylinder(h = 19.3205, d = 1.0, center = false);
            }
         }
      }
   }
   translate(v = [40.0, 0.0, 0.0])
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         rotate(a = [0.0, 54.7356, 45.0])
         {
            cylinder(h = 17.3205, d = 3.0, center = false);
         }
      }
   }
   %union()
   {
      translate(v = [0.0, 0.0, 0.0])
      {
         cube(size = [10.0, 10.0, 10.0], center = false);
      }
   }
   translate(v = [10.0, 0.0, 0.0])
   {
      %union()
      {
         translate(v = [0.0, 0.0, 0.0])
         {
            cube(size = [10.0, 10.0, 10.0], center = false);
         }
      }
   }
   translate(v = [20.0, 0.0, 0.0])
   {
      %union()
      {
         translate(v = [0.0, 0.0, 0.0])
         {
            cube(size = [10.0, 10.0, 10.0], center = false);
         }
      }
   }
   translate(v = [30.0, 0.0, 0.0])
   {
      %union()
      {
         translate(v = [0.0, 0.0, 0.0])
         {
            cube(size = [10.0, 10.0, 10.0], center = false);
         }
      }
   }
   translate(v = [40.0, 0.0, 0.0])
   {
      %union()
      {
         translate(v = [0.0, 0.0, 0.0])
         {
            cube(size = [10.0, 10.0, 10.0], center = false);
         }
      }
   }
}
