import globals as gl
def setup():
    size(800, 400)
    gl.posBalle = PVector(gl.xballe, gl.yballe)
    gl.vitBalle = PVector(gl.xvit, gl.yvit)
    gl.gravite = PVector(gl.xgrvt, gl.ygrvt)
def draw():
    background(200)
    gl.posBalle.add(gl.vitBalle)
    if gl.posBalle.y >= 370:
        gl.posBalle.y = 370
        gl.vitBalle.mult(0.8)
        gl.vitBalle.y = -abs(gl.vitBalle.y)
        
        
    
    
    gl.vitBalle.add(gl.gravite)
    fill(255, 0, 0)
    ellipse(gl.posBalle.x, gl.posBalle.y, 20, 20)
    fill(150, 150, 150)
    rect(0, 380, 800, 20)
