#Mark Mariscal
#lab 4 
#vertical mirror:
def pic():
  return makePicture(pickAFile())

def copyMirror():
  catPict=pic()
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width/2):
    for y in range(0,height):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,width-x-1,y),color)
  show(catPict)
  show(canvas)
  return canvas

# picture horizontally either top-to-bottom:
def topbottom():
  catPict=pic()
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width):
    for y in range(0, height/2):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,x, height-1-y),color)
  show(catPict)
  show(canvas)
  return canvas

#or bottom-to-top:
def bottomtop():
  catPict=pic()
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width):
    for y in range(height/2, height -1):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,x, height - y),color)
  show(catPict)
  show(canvas)
  return canvas

#Mirror Pic
def copyAndMirrorCat():
  catPict=pic()
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width/2):
    for y in range(0, height/2):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas, width - x - 1, y),color)
      setColor(getPixel(canvas, x, height - y - 1), color)
      setColor(getPixel(canvas, width-x-1, height-y-1),color)
  show(catPict)
  show(canvas)
  return canvas

#Problem 2
def simpleCopy(pic):
  canvas=makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      setColor(getPixel(canvas, x, y), getColor(getPixel(pic, x, y)))
  show(pic)
  show(canvas)
  return canvas

#Problem 3
def rotatePic():
  picture=pic()
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(height, width)
  for x in range(0, width):
    for y in range(0, height):
      setColor(getPixel(canvas, y, getHeight(canvas)-x-1), getColor(getPixel(picture, x, y)))
  show(picture)
  show(canvas)

#Problem 4  
def shrinkPic():
  picture=pic()
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(width/2,height/2 )
  newWidth =getWidth(canvas)
  newHeight =getHeight(canvas)
  newX = 0
  newY = 0
  for x in range( 0, width, 2 ):
    for y in range ( 0, height, 2 ):
      if x/2 <= newWidth - 1 and y/2 <= newHeight - 1:
        setColor( getPixel(canvas, newX, newY ),  getColor(getPixel(picture, x, y)))
        newY = newY + 1
    newX = newX + 1
    newY = 0
  show(picture)
  show(canvas)
  return canvas

