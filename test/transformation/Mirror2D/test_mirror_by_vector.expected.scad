// Unit of length: Unit.MM
union()
{
   translate(v = [5.0, 5.0])
   {
      polygon(points = [[0.0, 0.0], [10.0, 0.0], [0.0, 5.0]]);
   }
   mirror(v = [0.7071, 0.7071])
   {
      translate(v = [5.0, 5.0])
      {
         polygon(points = [[0.0, 0.0], [10.0, 0.0], [0.0, 5.0]]);
      }
   }
}
