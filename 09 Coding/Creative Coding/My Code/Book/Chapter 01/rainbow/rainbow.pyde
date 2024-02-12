# Rainbow
'''
Dark blue: #5d55a4
Light blue: #458bcb
Green: #62bb46
Yellow: #f5eb00
Orange: #f89a1c
Red: #c02b32
'''

size(600, 300)
background("#004477")
noStroke()

fill('#c02b32')
circle(300, 300, 500)

fill('#f89a1c')
circle(300, 300, 450)

fill('#f5eb00')
circle(300, 300, 400)

fill('#62bb46')
circle(300, 300, 350)

fill('#458bcb')
circle(300, 300, 300)

fill('#5d55a4')
circle(300, 300, 250)


fill('#004477')
circle(300, 300, 200)# bands
fill('#FF0000')
circle(300, 300, 550)
fill('#FF9900')
circle(300, 300, 500)
fill('#FFFF00')
circle(300, 300, 450)
fill('#00FF00')
circle(300, 300, 400)
fill('#0099FF')
circle(300, 300, 350)
fill('#6633FF')
circle(300, 300, 300)

# center circle (mask)
fill('#004477')
circle(300, 300, 250)

save('rainbow.png')
