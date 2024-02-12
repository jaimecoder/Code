size(500, 500)
grid = loadImage('grid.png')
image(grid, 0, 0)
noFill()
strokeWeight(3)

stroke('#0099FF') # pale blue
#line(100, 100, 400, 400)
curve(0, 0, 100, 100, 400, 400, 500, 500)

curveTightness(0.5) #Try values between -0.5 and 0.5
stroke('#FFFF00') # yellow
curve(0, 250, 100, 100, 400, 400, 500, 250)

stroke('#FF9900') # orange
# control point 1:
curve(0, 250, 0, 250, 100, 100, 400, 400)
# control point 2:
curve(100, 100, 400, 400, 500, 250, 500, 250)

# BEZIER CURVES
stroke('#FF99FF') # pink
cp1x = 200
cp1y = 250
cp2x = 320
cp2y = 420
bezier(400, 100, cp1x, cp1y, cp2x, cp2y, 100, 400)
stroke('#FF0000') # red
line(400, 100, cp1x, cp1y)
line(100, 400, cp2x, cp2y)
