size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

'''arc(
    width/2, height/2,
    200, 200,
    0, 2
)'''
#arc(width/2, height/2, 300, 300, 0, PI)
#arc(width/2, height/2, 400, 400, 0, PI*2)
#arc(width/2, height/2, 350, 350, 3.4, (PI*2)-(PI/2), PIE)

#Begin of Analyzer code
 # Circles

#1st row
fill('#00aa4f')
arc(width/2, height/2, 400, 400, (((PI/7) * 4) + 3.1416), (((PI/7) * 5) + 3.1416), PIE)


# 2nd Row
fill('#eeaacc')
arc(width/2, height/2, 300, 300, PI, (((PI/7) * 2) + 3.1416), PIE)
arc(width/2, height/2, 300, 300, (((PI/7) * 2) + 3.1416), (((PI/7) * 4) + 3.1416), PIE)
fill('#00a1e1')
arc(width/2, height/2, 300, 300, (((PI/7) * 4) + 3.1416), (((PI/7) * 6) + 3.1416), PIE)
arc(width/2, height/2, 300, 300, (((PI/7) * 6) + 3.1416), (((PI/7) * 7) + 3.1416), PIE)

#3rd top row
fill('#eb5499')
arc(width/2, height/2, 200, 200, PI, (((PI/7) * 4) + 3.1416), PIE)
fill('#7456a4')
arc(width/2, height/2, 200, 200, (((PI/7) * 4) + 3.1416), (((PI/7) * 7) + 3.1416), PIE)

#1st bottom row
# Es toda la mitad de abajo, pero lo cubre el círculo con color de fondo
fill('#eb2d2e')
arc(width/2, height/2, 200, 200, 0, PI, PIE)

#Circulo de en medio
fill('#004477')
arc(width/2, height/2, 100, 100, 0, PI*2)
