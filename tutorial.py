from ursina import *
app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False
window.color = color.black

page = 1

def left():
    global page
    if page > 1:
        page -= 1
def right():
    global page
    if page < 7:
        page += 1


def update():
    global page
    if page > 1:
        leftArrow.enable()
    if page == 1:
        leftArrow.disable()

# -----------------------------
    if page == 1: # running
        running.enable()
    else:
        running.disable()
# -----------------------------
    if page == 2: # linear
        linear.enable()
        linear2.enable()
    else:
        linear.disable()
        linear2.disable()
# -----------------------------
    if page == 3: # trigonalplanar
        trigonalplanar.enable()
        trigonalplanar2.enable()
    else:
        trigonalplanar.disable()
        trigonalplanar2.disable()
# -----------------------------
    if page == 4: # tetrahedral
        tetrahedral.enable()
        tetrahedral2.enable()
    else:
        tetrahedral.disable()
        tetrahedral2.disable()
# -----------------------------
    if page == 5: # trigonalpyramidal
        trigonalpyramidal.enable()
        trigonalpyramidal2.enable()
    else:
        trigonalpyramidal.disable()
        trigonalpyramidal2.disable()
# -----------------------------
    if page == 6: # bent
        bent.enable()
        bent2.enable()
    else:
        bent.disable()
        bent2.disable()
# -----------------------------
    if page == 7: # total
        total.enable()
        rightArrow.disable()
    else:
        total.disable()
        rightArrow.enable()


leftArrow = Entity(model='quad', texture='texture/triangle.png', rotation_z=43.7, x=-6, collider='box', on_click=left, enabled=False)
rightArrow = Entity(model='quad', texture='texture/triangle.png', rotation_z=-137, x=6, collider='box', on_click=right)


running = Entity(model='quad', texture='texture/running.jpg', scale=(15,9), enabled=False)
linear = Entity(model='quad', texture='texture/linear.jpg', scale=4, x=-2, enabled=False)
linear2 = Entity(model='quad', texture='texture/linear2.jpg', scale=4, x=2.5, enabled=False)

trigonalplanar = Entity(model='quad', texture='texture/trigonalPlanar.jpg', scale=4, x=-2, enabled=False)
trigonalplanar2 = Entity(model='quad', texture='texture/trigonalPlanar2.jpg', scale=4, x=2.5, enabled=False)

tetrahedral = Entity(model='quad', texture='texture/tetrahedral.jpg', scale=4, x=-2, enabled=False)
tetrahedral2 = Entity(model='quad', texture='texture/tetrahedral2.jpg', scale=4, x=2.5, enabled=False)

trigonalpyramidal = Entity(model='quad', texture='texture/trigonalPyramidal.jpg', scale=4, x=-2, enabled=False)
trigonalpyramidal2 = Entity(model='quad', texture='texture/trigonalPyramidal2.jpg', scale=4, x=2.5, enabled=False)

bent = Entity(model='quad', texture='texture/bent.jpg', scale=4, x=-2, enabled=False)
bent2 = Entity(model='quad', texture='texture/bent2.jpg', scale=4, x=2.5, enabled=False)

total = Entity(model='quad', texture='texture/total.jpg', parent=camera.ui, enabled=False)

app.run()