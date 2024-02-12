size(800, 800)
grid = loadImage('grid.png')
image(grid, 0, 0)
noFill()
stroke('#FFFFFF')
strokeWeight(3)

beginShape() # begins recording vertices for a shape ...
vertex(100, 100)
vertex(200, 100)
vertex(200, 200)
vertex(100, 200)
endShape() # stops recording
