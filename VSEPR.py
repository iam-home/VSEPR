from ursina import *
app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False
window.color = color.black

BONDING = 0
LONEPAIR = 0

angle = math.radians(120)

def bonding():
    global BONDING
    if BONDING < 4:
        BONDING += 1

def cancelBonding():
    global BONDING
    BONDING -= 1
    if BONDING < 4:
        addBonding.enable()


def lonepair():
    global LONEPAIR
    if LONEPAIR < 2:
        LONEPAIR += 1

def cancelLonePair():
    global LONEPAIR
    LONEPAIR -= 1
    if LONEPAIR < 2:
        addLonePair.enable()


def addCancleBonding():
    global deleteBonding
    deleteBonding = Entity(model='cube', texture='texture/X.png', parent=camera.ui, collider='box', on_click=cancelBonding, scale=.05, position=(.74, -.25))

def addCancelLonePair():
    global deleteLonePair
    deleteLonePair = Entity(model='cube', texture='texture/X.png', parent=camera.ui, collider='box', on_click=cancelLonePair, scale=.05, position=(.74, -.36))

onlyBonding_group = Entity(name='onlyBonding')
linear_group = Entity(name='linear')
trigonalPlanar_group = Entity(name='trigonal_planar')
tetrahedral_group = Entity(name='tetrahedral')
trigonalPyramidal_group = Entity(name='trigonal_pyramidal')
bent_group = Entity(name='bent_group')

def onlyBonding():
    bondatom = Entity(model='sphere', parent=onlyBonding_group, color=color.white, scale=0.7, x=2)
    Entity(model=Mesh(vertices=[(0,0,0), (2,0,0)], mode='line'), color=color.white, parent=onlyBonding_group)
def linear(): # 180
    Entity(model=Mesh(vertices=[(0,0,0), (2,0,0)], mode='line'), color=color.white, parent=linear_group)
    bondatom = Entity(model='sphere', parent=linear_group, color=color.white, scale=0.7, x=2)
    Entity(model=Mesh(vertices=[(0,0,0), (-2,0,0)], mode='line'), color=color.white, parent=linear_group)
    bondatom = Entity(model='sphere', parent=linear_group, color=color.white, scale=0.7, x=-2)
def trigonalPlanar(): # 120
    Entity(model=Mesh(vertices=[(0,0,0), (2,0,0)], mode='line'), color=color.white, parent=trigonalPlanar_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, x=2)
    Entity(model=Mesh(vertices=[(0,0,0), (-1, 2*sqrt(3)/2, 0)], mode='line'), color=color.white, parent=trigonalPlanar_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, x=math.cos(angle)*2, y=math.sin(angle)*2)
    Entity(model=Mesh(vertices=[(0,0,0), (-1, 2*-sqrt(3)/2, 0)], mode='line'), color=color.white, parent=trigonalPlanar_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, x=math.cos(angle)*2, y=-math.sin(angle)*2)
def tetrahedral(): # 109.5
    Entity(model=Mesh(vertices=[(0,0,0), (2/sqrt(3), 2/sqrt(3), 2/sqrt(3))], mode='line'), color=color.white, parent=tetrahedral_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, position=(2/sqrt(3), 2/sqrt(3), 2/sqrt(3)))
    Entity(model=Mesh(vertices=[(0,0,0), (2/sqrt(3), -2/sqrt(3), -2/sqrt(3))], mode='line'), color=color.white, parent=tetrahedral_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, position=(2/sqrt(3), -2/sqrt(3), -2/sqrt(3)))
    Entity(model=Mesh(vertices=[(0,0,0), (-2/sqrt(3), 2/sqrt(3), -2/sqrt(3))], mode='line'), color=color.white, parent=tetrahedral_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, position=(-2/sqrt(3), 2/sqrt(3), -2/sqrt(3)))
    Entity(model=Mesh(vertices=[(0,0,0), (-2/sqrt(3), -2/sqrt(3), 2/sqrt(3))], mode='line'), color=color.white, parent=tetrahedral_group)
    bondatom = Entity(model='sphere', parent=trigonalPlanar_group, color=color.white, scale=0.7, position=(-2/sqrt(3), -2/sqrt(3), 2/sqrt(3)))
def trigonalPyramidal():
    lonepairAtom = Entity(model='models/LonePair.gltf', parent=trigonalPyramidal_group, color=color.gray, rotation_x=-54.74, rotation_z=225)
    bondatom = Entity(model='sphere', parent=trigonalPyramidal_group, color=color.white, scale=0.7, position=(sqrt(3), sqrt(3), 0))
    bondatom = Entity(model='sphere', parent=trigonalPyramidal_group, color=color.white, scale=0.7, position=(sqrt(3), 0, -sqrt(3)))
    bondatom = Entity(model='sphere', parent=trigonalPyramidal_group, color=color.white, scale=0.7, position=(0, sqrt(3), -sqrt(3)))
    Entity(model=Mesh(vertices=[(0, 0, 0), (sqrt(3), sqrt(3), 0)], mode='line'), color=color.white, parent=trigonalPyramidal_group)
    Entity(model=Mesh(vertices=[(0, 0, 0), (sqrt(3), 0, -sqrt(3))], mode='line'), color=color.white, parent=trigonalPyramidal_group)
    Entity(model=Mesh(vertices=[(0, 0, 0), (0, sqrt(3), -sqrt(3))], mode='line'), color=color.white, parent=trigonalPyramidal_group)
def bent():
    lonepairAtom = Entity(model='models/LonePair.gltf', parent=bent_group, color=color.gray, rotation_x=-90+56)
    lonepairAtom = Entity(model='models/LonePair.gltf', parent=bent_group, color=color.gray, rotation_x=-90-56)
    bondatom = Entity(model='sphere', parent=bent_group, color=color.white, scale=0.7, position=(2*sin(52.25), 0, -2*cos(52.25)))
    bondatom = Entity(model='sphere', parent=bent_group, color=color.white, scale=0.7, position=(-2*sin(52.25), 0, -2*cos(52.25)))
    Entity(model=Mesh(vertices=[(0, 0, 0), (2*sin(52.25), 0, -2*cos(52.25))], mode='line'), color=color.white, parent=bent_group)
    Entity(model=Mesh(vertices=[(0, 0, 0), (-2*sin(52.25), 0, -2*cos(52.25))], mode='line'), color=color.white, parent=bent_group)

Linear = Text(text="Molecular geometry : Linear", position=(-.75,-.3))
Trigonalplanar = Text(text="Molecular geometry : Trigonal planar", position=(-.75,-.3))
Tetrahedral = Text(text="Molecular geometry : Tetrahedral", position=(-.75,-.3))
Trigonalpyramidal = Text(text="Molecular geometry : Trigonal pyramidal", position=(-.75,-.3))
Bent = Text(text="Molecular geometry : Bent", position=(-.75,-.3))
bondAngles = Text(text="Bond Angles : 0°", position=(-.75,-.35))

Linear.disable()
Trigonalplanar.disable()
Tetrahedral.disable()
Trigonalpyramidal.disable()
Bent.disable()
bondAngles.disable()

def update():
    global deleteBonding, deleteLonePair, BONDING, LONEPAIR, addBonding, addLonePair, Linear, trigonalPlanar, tetrahedral, trigonalPyramidal, bent, bondAngles

    if BONDING == 1 and deleteBonding is None:
        addCancleBonding()

    if LONEPAIR == 1 and deleteLonePair is None:
        addCancelLonePair()

    if BONDING <= 0 and deleteBonding is not None:
        destroy(deleteBonding)
        deleteBonding = None

    if LONEPAIR <= 0 and deleteLonePair is not None:
        destroy(deleteLonePair)
        deleteLonePair = None


    destroy(onlyBonding_group)
    destroy(linear_group)
    destroy(trigonalPlanar_group)
    destroy(tetrahedral_group)
    destroy(trigonalPyramidal_group)
    destroy(bent_group)

    globals()['onlyBonding_group'] = Entity(name='onlyBonding')
    globals()['linear_group'] = Entity(name='linear')
    globals()['trigonalPlanar_group'] = Entity(name='trigonal_planar')
    globals()['tetrahedral_group'] = Entity(name='tetrahedral')
    globals()['trigonalPyramidal_group'] = Entity(name='trigonalPyramidal')
    globals()['bent_group'] = Entity(name='bent')

    if BONDING == 1 and LONEPAIR == 0:
        onlyBonding()

    if BONDING == 2 and LONEPAIR == 0: # 180
        linear()
        Linear.enable()
        bondAngles.text = "Bond Angles : 180°"
    else:
        Linear.disable()

    if BONDING == 3 and LONEPAIR == 0: # 120
        trigonalPlanar()
        Trigonalplanar.enable()
        bondAngles.text = "Bond Angles : 120°"
    else:
        Trigonalplanar.disable()


    if BONDING == 4 and LONEPAIR == 0: # 109.5
        tetrahedral()
        Tetrahedral.enable()
        bondAngles.text = "Bond Angles : 109.5°"
    else:
        Tetrahedral.disable()

    if BONDING == 3 and LONEPAIR == 1: # 107
        trigonalPyramidal()
        Trigonalpyramidal.enable()
        bondAngles.text = "Bond Angles : 107°"
    else:
        Trigonalpyramidal.disable()

    if BONDING == 2 and LONEPAIR == 2: # 104.5
        bent()
        Bent.enable()
        bondAngles.text = "Bond Angles : 104.5°"
    else:
        Bent.disable()

    if (len(linear_group.children) > 0 or
        len(trigonalPlanar_group.children) > 0 or
        len(tetrahedral_group.children) > 0 or
        len(trigonalPyramidal_group.children) > 0 or
        len(bent_group.children)) > 0:
        bondAngles.enable()
    else:
        bondAngles.disable()


    if BONDING >= 4:
        addBonding.disable()

    if LONEPAIR >= 2:
        addLonePair.disable()

    if BONDING < 4 and addBonding is None:
        addBonding = Entity(model='cube', texture='texture/bonding.png', parent=camera.ui, collider='box', on_click=bonding, scale=(.2, .1), position=(.6, -.25))
    if LONEPAIR < 2 and addLonePair is None:
        addLonePair = Entity(model='cube', texture='texture/lonepair.png', parent=camera.ui, collider='box', on_click=lonepair, scale=(.2, .1), position=(.6, -.36))


centerAtom = Entity(
    model="sphere",
    color=color.red,
    scale=0.7,
)

addBonding = Entity(model='cube', texture='texture/bonding.png', parent=camera.ui, collider='box', on_click=bonding, scale=(.2, .1), position=(.6, -.25))
addLonePair = Entity(model='cube', texture='texture/lonepair.png', parent=camera.ui, collider='box', on_click=lonepair, scale=(.2, .1), position=(.6, -.36))
deleteBonding = None
deleteLonePair = None

EditorCamera()
app.run()