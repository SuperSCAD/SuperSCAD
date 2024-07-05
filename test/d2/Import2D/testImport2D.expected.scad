// Unit of length: Unit.MM
linear_extrude(height = 5.0, center = true, convexity = 10, twist = 0.0, scale = 1.0)
{
   import(file = "../../slot.dxf", layer = "Sketch");
}
