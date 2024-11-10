// Unit of length: Unit.MM
union()
{
   translate(v = [-11.0, 0.0])
   {
      union()
      {
         polygon(points = [[0.0, 5.0], [10.0, 0.0], [-10.0, 0.0]]);
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [0.0, 5.0])
            {
               rotate(a = 270.0)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [10.0, 0.0])
            {
               rotate(a = 166.7175)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [-10.0, 0.0])
            {
               rotate(a = 13.2825)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
      }
   }
   translate(v = [11.0, 0.0])
   {
      union()
      {
         polygon(points = [[-10.0, 0.0], [10.0, 0.0], [0.0, 5.0]]);
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [-10.0, 0.0])
            {
               rotate(a = 13.2825)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [10.0, 0.0])
            {
               rotate(a = 166.7175)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            translate(v = [0.0, 5.0])
            {
               rotate(a = 270.0)
               {
                  translate(v = [0.0, -0.05])
                  {
                     square(size = [0.5, 0.1], center = false);
                  }
               }
            }
         }
      }
   }
}
