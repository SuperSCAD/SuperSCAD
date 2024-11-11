// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      polygon(points = [[-10.0, -5.0], [-10.0, 5.0], [-10.0, 5.5], [10.5, 5.5], [10.5, -5.0], [10.0, -5.0]]);
   }
   square(size = [20.0, 10.0], center = true);
}
