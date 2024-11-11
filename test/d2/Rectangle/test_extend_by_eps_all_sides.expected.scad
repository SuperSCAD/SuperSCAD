// Unit of length: Unit.MM
union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      polygon(points = [[-0.5, -0.5], [-0.5, 10.5], [20.5, 10.5], [20.5, -0.5]]);
   }
   square(size = [20.0, 10.0], center = false);
}
