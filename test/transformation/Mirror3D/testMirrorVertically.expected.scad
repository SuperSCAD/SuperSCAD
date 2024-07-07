// Unit of length: Unit.MM
union()
{
   translate(v = [10.0, 10.0, 10.0])
   {
      polyhedron(points = [[20.0, 20.0, 0.0], [20.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 20.0, 0.0], [20.0, 20.0, 20.0]], faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], [1, 0, 3], [2, 1, 3]]);
   }
   mirror(v = [0.0, 1.0, 0.0])
   {
      translate(v = [10.0, 10.0, 10.0])
      {
         polyhedron(points = [[20.0, 20.0, 0.0], [20.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 20.0, 0.0], [20.0, 20.0, 20.0]], faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], [1, 0, 3], [2, 1, 3]]);
      }
   }
}
