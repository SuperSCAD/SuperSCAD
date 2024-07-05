// Unit of length: Unit.MM
union()
{
   translate(v = [5.0, 5.0])
   {
      polygon(points = [[0.0, 0.0], [10.0, 0.0], [0.0, 5.0]]);
   }
   rotate(a = [0.0, 180.0])
   {
      translate(v = [5.0, 5.0])
      {
         polygon(points = [[0.0, 0.0], [10.0, 0.0], [0.0, 5.0]]);
      }
   }
}
