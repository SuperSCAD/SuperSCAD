// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      polygon(points = [[0.0, 0.0], [0.0, 10.0], [0.0, 10.5], [20.0, 10.5], [20.0, 10.0], [20.0, 0.0]]);
   }
   square(size = [20.0, 10.0], center = false);
}
