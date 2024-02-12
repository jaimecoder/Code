# dimensions of the display window measured in pixels
size(500, 500)
background('#004477')
print('Hello, World!')
'''
This is a multiline comment.
Any code between the opening and closing triple-quotes is ignored
'''
print('How are you?')


stroke('#FFFFFF')
strokeWeight(3)

# small red rectangle
fill('#FF0000')
rect(100, 150, 200, 300)

# orange square
fill('#FF9900')
rect(50, 100, 150, 150)

# fill-less square
noFill()
square(250, 100, 150)

colorMode(HSB, 360, 100, 100)
fill(0, 100, 100)
