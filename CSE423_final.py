from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

quadric = None

helix,heliy,heliz=0,0,200
heliYaw=0
bladeang=0
helifallS=0
heliR=0
heliP=0
rotorS=25

def drawCopter():
    px=helix
    py=heliy
    pz=heliz

    glPushMatrix()
    glTranslatef(px,py,pz)
    glRotatef(heliYaw,0,0,1)
    glRotatef(heliP,0,1,0)
    glRotatef(heliR,1,0,0)

    glPushMatrix()
    glColor3f(0.16,0.20,0.23)
    glScalef(1.55,0.92,1.15)
    glutSolidSphere(28,16,12)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(24,0,2)
    glColor3f(0.18,0.23,0.26)
    glScalef(1,0.80,0.78)
    glutSolidSphere(22,16,12)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(39,0,1)
    glColor3f(0.06,0.28,0.40)
    glScalef(0.75,0.70,0.62)
    glutSolidSphere(17,12,10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-55,0,4)
    glColor3f(0.12,0.15,0.17)
    glScalef(3.4,0.24,0.24)
    glutSolidCube(22)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-89,0,5)
    glColor3f(0.12,0.15,0.17)
    glScalef(0.60,0.90,0.65)
    glutSolidCube(22)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-99,0,5)
    glRotatef(bladeang*2,1,0,0)
    glColor3f(0.04,0.04,0.04)
    glScalef(0.10,1.7,0.10)
    glutSolidCube(26)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,36)
    glColor3f(0.08,0.08,0.08)
    glutSolidSphere(8,10,8)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,45)
    glRotatef(bladeang,0,0,1)
    glColor3f(0.04,0.04,0.04)
    glScalef(4.8,0.10,0.07)
    glutSolidCube(36)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,45)
    glRotatef(bladeang+90,0,0,1)
    glColor3f(0.04,0.04,0.04)
    glScalef(4.8,0.10,0.07)
    glutSolidCube(36)
    glPopMatrix()

    for side in [-1,1]:
        glPushMatrix()
        glTranslatef(-2,side*25,-23)
        glColor3f(0.06,0.06,0.06)
        glScalef(2.8,0.12,0.12)
        glutSolidCube(25)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(22,side*25,-16)
        glColor3f(0.13,0.13,0.13)
        glRotatef(90,1,0,0)
        gluCylinder(quadric,2.4,2.4,22,8,2)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(8,side*22,-3)
        glColor3f(0.12,0.12,0.12)
        glScalef(1.7,0.12,0.12)
        glutSolidCube(20)
        glPopMatrix()

    glPushMatrix()
    glTranslatef(28,0,-18)
    glColor3f(0.09,0.09,0.09)
    glScalef(0.75,0.75,0.42)
    glutSolidSphere(13,10,8)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(36,0,-22)
    glColor3f(0.25,0.25,0.25)
    glScalef(0.65,0.65,1.7)
    gluCylinder(quadric,5,3,18,8,4)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(38,0,-7)
    if math.sin(time.time()*8)>0:
        glColor3f(1,0.05,0.03)
    else:
        glColor3f(0.22,0,0)
    glutSolidSphere(4.5,8,6)
    glPopMatrix()

    glPopMatrix()

FOV_Y=90
camYaw=0
camP=0
camMode=0

def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOV_Y,1.25,0.1,2000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    radYaw=math.radians(camYaw)
    radPitch=math.radians(camP)

    if camMode==0:
        dist=280
        cx=helix-dist*math.cos(radPitch)*math.cos(radYaw)
        cy=heliy-dist*math.cos(radPitch)*math.sin(radYaw)
        cz=max(30,heliz+80+dist*math.sin(radPitch))
        gluLookAt(cx,cy,cz,helix,heliy,max(5,heliz),0,0,1)
    elif camMode==1:
        cx=helix+40*math.cos(radYaw)
        cy=heliy+40*math.sin(radYaw)
        cz=heliz+5
        
        effPitch=radPitch-0.25
        lx=cx+math.cos(effPitch)*math.cos(radYaw)*100
        ly=cy+math.cos(effPitch)*math.sin(radYaw)*100
        lz=cz+math.sin(effPitch)*100
        gluLookAt(cx,cy,cz,lx,ly,lz,0,0,1)
    elif camMode==2:
        gluLookAt(helix,heliy+0.1,heliz+600,helix,heliy,heliz,0,0,1)

GRID_SIZE=600
tileS=40
trees=[]
clouds=[]

def genTrees(count=80):
    trees.clear()
    for x in range(count):
        tx=random.uniform(-GRID_SIZE+50,GRID_SIZE-50)
        ty=random.uniform(-GRID_SIZE+50,GRID_SIZE-50)
        if math.hypot(tx,ty)>100:
            scale = random.uniform(0.5,1.8)
            trees.append({'x':tx,'y':ty,'scale':scale})
    outer=GRID_SIZE*1.2
    inner=GRID_SIZE+25
    for x in range(35):
        tx=random.uniform(-outer,outer)
        ty=random.uniform(inner,outer)
        trees.append({'x':tx,'y': ty,'scale':random.uniform(0.7,1.6)})
    for x in range(35):
        tx=random.uniform(-outer,outer)
        ty=random.uniform(-outer,-inner)
        trees.append({'x':tx,'y':ty,'scale':random.uniform(0.7,1.6)})
    for x in range(35):
        tx=random.uniform(inner, outer)
        ty=random.uniform(-GRID_SIZE,GRID_SIZE)
        trees.append({'x':tx,'y':ty,'scale':random.uniform(0.7,1.6)})
    for x in range(35):
        tx=random.uniform(-outer,-inner)
        ty=random.uniform(-GRID_SIZE, GRID_SIZE)
        trees.append({'x': tx,'y':ty,'scale':random.uniform(0.7,1.6)})

def genClouds(count=25):
    clouds.clear()
    for x in range(count):
        cx=random.uniform(-GRID_SIZE, GRID_SIZE)
        cy=random.uniform(-GRID_SIZE, GRID_SIZE)
        cz=random.uniform(300,450)
        puffs=[]
        numP=random.randint(4,7)
        for x in range(numP):
            puffs.append({
                'ox':random.uniform(-25,25),'oy':random.uniform(-25,25),
                'oz':random.uniform(-10,10),'r':random.uniform(20,35)
            })
        clouds.append({'x':cx,'y':cy,'z':cz,'puffs':puffs})

def drawTs(tree):
    glPushMatrix()
    glTranslatef(tree['x'],tree['y'],0)
    s = tree['scale']
    glScalef(s,s,s)

    glColor3f(0.45,0.25,0.1)
    glPushMatrix()
    gluCylinder(quadric, 4,3,20,8,8)
    glPopMatrix()

    glColor3f(0,0.35,0.08)
    glPushMatrix()
    glTranslatef(0,0,15)
    gluCylinder(quadric,18,0,45,10,10)
    glPopMatrix()

    glPopMatrix()

def drawC(cloud):
    glColor3f(0.95,0.95,0.98)
    glPushMatrix()
    glTranslatef(cloud['x'],cloud['y'],cloud['z'])
    for puff in cloud['puffs']:
        glPushMatrix()
        glTranslatef(puff['ox'],puff['oy'],puff['oz'])
        gluSphere(quadric,puff['r'],10,10)
        glPopMatrix()

    glPopMatrix()

tanks=[]

def makeTank():
    tanks.append({
        'x':random.uniform(-GRID_SIZE+80,GRID_SIZE-80),
        'y':random.uniform(-GRID_SIZE+80,GRID_SIZE-80),
        'angle':random.uniform(0,360),
        'turret_angle':0,
        'shoot_timer':random.randint(560,840)
    })

def drawTT(tank):
    glPushMatrix()
    glTranslatef(tank['x'],tank['y'],8)
    glRotatef(tank['angle'],0,0,1)
    inRadar =cheatM and(math.hypot(tank['x']-helix,tank['y']-heliy)<=RR)

    for side in [-1,1]:
        glColor3f(0.12,0.12,0.12)
        glPushMatrix()
        glTranslatef(0,side*15,2)
        glScalef(2.2,0.35,0.5)
        glutSolidCube(24)
        glPopMatrix()

        glColor3f(0.05,0.05,0.05)
        for wx in [-18,-6,6,18]:
            glPushMatrix()
            glTranslatef(wx,side*15,-1)
            glRotatef(90,1,0,0)
            gluCylinder(quadric,3.5,3.5,3,10,10)
            glPopMatrix()

    if inRadar:
        glColor3f(0.9,0.1,0.1)
    else:
        glColor3f(0.22,0.35,0.15)

    glPushMatrix()
    glTranslatef(0,0,6)
    glScalef(2,1,0.45)
    glutSolidCube(22)
    glPopMatrix()

    if inRadar:
        glColor3f(1,0.2,0.1)
    else:
        glColor3f(0.28,0.42,0.18)

    glPushMatrix()
    glTranslatef(16,0,7)
    glRotatef(-25,0,1,0)
    glScalef(0.6,0.95,0.35)
    glutSolidCube(20)
    glPopMatrix()

    glColor3f(0.1,0.1,0.1)
    for side in [-6,6]:
        glPushMatrix()
        glTranslatef(-22,side,9)
        glRotatef(90,0,1,0)
        gluCylinder(quadric,1.2,1.2,4,8,8)
        glPopMatrix()

    glPushMatrix()
    glTranslatef(2,0,14)
    glRotatef(tank['turret_angle'],0,0,1)

    if inRadar:
        glColor3f(1,0,0)
    else:
        glColor3f(0.18,0.28,0.12)

    glPushMatrix()
    glScalef(1.2,1,0.5)
    glutSolidCube(18)
    glPopMatrix()

    glColor3f(0.1,0.1,0.1)
    glPushMatrix()
    glTranslatef(12,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,1.8,1.5,22,10,10)
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()
    glColor3f(1,1,1)

bombs=[]
explosions=[]

def fireBomb():
    if gameS==1:
        rad_yaw=math.radians(heliYaw)
        forwardx=math.cos(rad_yaw)
        forwardy=math.sin(rad_yaw)
        downz=-0.65
        mag=math.sqrt(forwardx**2+forwardy**2+downz**2)
        dx=forwardx/mag
        dy=forwardy/mag
        dz=downz/mag
        bombs.append({'x':helix+dx*45,'y':heliy+dy*45,'z':heliz-35,'dx':dx,'dy':dy,'dz':dz})

def drawBB(b):
    glPushMatrix()
    glTranslatef(b['x'],b['y'],b['z'])

    pitch=math.degrees(math.atan2(b['dz'],math.hypot(b['dx'],b['dy'])))
    yaw=math.degrees(math.atan2(b['dy'],b['dx']))
    glRotatef(yaw,0,0,1)
    glRotatef(-pitch,0,1,0)
    glScalef(2.2,2.2,2.2)

    glColor3f(0.2,0.32,0.18)
    glPushMatrix()
    glTranslatef(-8,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,3.2,3.2,18,12,12)
    glPopMatrix()

    glColor3f(0.95,0.1,0.1)
    glPushMatrix()
    glTranslatef(10,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,3.2,0,6,12,12)
    glPopMatrix()

    glColor3f(1,0.8,0)
    glPushMatrix()
    glTranslatef(8,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,3.25,3.25,2,12,12)
    glPopMatrix()

    glColor3f(0.1,0.1,0.1)
    glPushMatrix()
    glTranslatef(-13,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,2,3,5,10,10)
    glPopMatrix()

    glColor3f(0.12,0.12,0.12)
    for fin_angle in [0,90,180,270]:
        glPushMatrix()
        glTranslatef(-11,0,0)
        glRotatef(fin_angle,1,0,0)
        glScalef(0.5,0.1,1.1)
        glutSolidCube(10)
        glPopMatrix()

    glColor3f(0.1,0.1,0.1)
    for fin_angle in [45,135,225,315]:
        glPushMatrix()
        glTranslatef(2,0,0)
        glRotatef(fin_angle,1,0,0)
        glScalef(0.4,0.08,0.7)
        glutSolidCube(8)
        glPopMatrix()

    glPopMatrix()
    glColor3f(1,1,1)

def mouseListener(button,state,x,y):
    if(gameS==1 and button==GLUT_LEFT_BUTTON and state==GLUT_DOWN):
        fireBomb()

score=0
lives=5

def awardScore(points=100):
    global score
    score+=points

def loseLife():
    global lives,helifallS,gameS
    lives-=1
    if lives<=0:
        lives=0
        helifallS=0.5
        gameS=4

bullets=[]

def TankBomb(bul):
    glPushMatrix()
    glTranslatef(bul['x'],bul['y'],bul['z'])

    pitch=math.degrees(math.atan2(bul['vz'],math.hypot(bul['vx'],bul['vy'])))
    yaw=math.degrees(math.atan2(bul['vy'],bul['vx']))
    glRotatef(yaw,0,0,1)
    glRotatef(-pitch,0,1,0)

    glScalef(1.4,1.4,1.4)

    glColor3f(0.55,0.55,0.58)
    glPushMatrix()
    glRotatef(90,0,1,0)
    gluCylinder(quadric,2.8,2.8,11,10,8)
    glPopMatrix()

    glColor3f(0.85,0.68,0.22)
    glPushMatrix()
    glTranslatef(5.8,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,2.8,1.2,4,10,6)
    glPopMatrix()

    glColor3f(0.18,0.18,0.18)
    glPushMatrix()
    glTranslatef(-5.8,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,2.2,2.8,3.5,10,6)
    glPopMatrix()

    glColor3f(1.0,0.32,0.05)
    glPushMatrix()
    glTranslatef(8.0,0,0)
    glutSolidSphere(1.8,8,6)
    glPopMatrix()

    glColor3f(0.12,0.12,0.12)
    for fin_angle in [45,135,225,315]:
        glPushMatrix()
        glTranslatef(-4.0,0,0)
        glRotatef(fin_angle,1,0,0)
        glScalef(0.45,0.08,0.8)
        glutSolidCube(7)
        glPopMatrix()

    glColor3f(1.0,0.75,0.18)
    glPushMatrix()
    glTranslatef(1.5,0,0)
    glRotatef(90,0,1,0)
    gluCylinder(quadric,3,3,1.2,10,6)
    glPopMatrix()

    glPopMatrix()
    glColor3f(1,1,1)

gameS=0

def draw_text(x,y,text):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0,1000,0,800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x,y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def reset():
    global helix,heliy,heliz,heliYaw,heliR,heliP
    global helifallS,rotorS,camYaw, camP,score,lives,gameS,radarfirecooldown
    helix,heliy,heliz=0,0,200
    heliYaw=0
    heliR=0
    heliP=0
    helifallS=0
    rotorS=25
    camYaw=0
    camP=0
    score=0
    lives=5
    gameS=1
    radarfirecooldown=0
    tanks.clear()
    bombs.clear()
    explosions.clear()
    bullets.clear()
    genTrees(80)
    genClouds(25)
    for x in range(5):
        makeTank()

def showScreen():
    glClearColor(0.4,0.7,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0,0,1000,800)

    setupCamera()
    world()

    if gameS==0:
        draw_text(446,450,f"SKY HUNTER")
        draw_text(425,400,f"Press SPACE to Start")
    elif gameS==1:
        draw_text(10,770,f"Score: {score}   Lives: {lives}")
        draw_text(10,50, f"C for Cheat: {'ON' if cheatM else 'OFF'}")
        draw_text(10,20,f"WASD for Move | LC for Bomb | AK for View | P for Pause")
    elif gameS == 2:
        draw_text(420, 420, "GAME PAUSED - Press 'P' to Resume")
    elif gameS == 3:
        draw_text(420,450,f"GAME OVER")
        draw_text(420,400,f"Final Score: {score}")
        draw_text(405,350,f"Press 'R' to Restart")

    glutSwapBuffers()

def keyboardListener(key,x,y):
    global camMode,cheatM,gameS,helix,heliy,heliYaw,camYaw
    Kchar=key.decode("utf-8").lower() if isinstance(key, bytes) else str(key).lower()

    if(Kchar==' ' and gameS==0):
        reset()
        return
    if(Kchar=='p' and gameS in (1, 2)):
        gameS=2 if gameS==1 else 1
        return
    if (Kchar=='r'):
        reset()
        return

    if (gameS==1):
        rad=math.radians(heliYaw)
        if(Kchar=='w'):
            helix+=5*math.cos(rad)
            heliy+=5*math.sin(rad)
        elif(Kchar=='s'):
            helix-=5*math.cos(rad)
            heliy-=5*math.sin(rad)
        elif(Kchar=='a'):
            heliYaw=(heliYaw+3)%360
            camYaw=(camYaw+3)%360
        elif (Kchar=='d'):
            heliYaw=(heliYaw-3)%360
            camYaw=(camYaw-3)%360
        elif(Kchar=='v'):
            camMode=(camMode+1)%3
        elif(Kchar=='c'):
            cheatM=not cheatM

        helix=max(-GRID_SIZE+20,min(GRID_SIZE-20,helix))
        heliy=max(-GRID_SIZE+20,min(GRID_SIZE-20,heliy))

def specialKeyListener(key,x,y):
    global camP, camYaw
    if (gameS!=1):
        return

    if(key==GLUT_KEY_UP):
        camP=min(80,camP+2)
    elif (key==GLUT_KEY_DOWN):
        camP=max(-80,camP-2)
    elif(key==GLUT_KEY_LEFT):
        camYaw=(camYaw+3)%360
    elif(key==GLUT_KEY_RIGHT):
        camYaw=(camYaw-3)%360

cheatM=False
RR=250
radaranimr=0
radaranimdir=1
radarfirecooldown=0

def autoAttack():
    global radarfirecooldown
    if(not cheatM or gameS!=1):
        return
    if(radarfirecooldown>0):
        radarfirecooldown-=1
        return
    closestT=None
    minD=RR
    for tank in tanks:
        dist=math.hypot(tank['x']-helix,tank['y']-heliy)
        if (dist<=minD):
            minD=dist
            closestT=tank
    if (closestT):
        dx=closestT['x']- helix
        dy=closestT['y']- heliy
        dz=0.0-(heliz-35)
        length=math.sqrt(dx*dx+dy * dy + dz * dz)
        if(length>0):
            bombs.append({
                'x': helix,
                'y': heliy,
                'z': heliz-35,
                'dx':dx/length,
                'dy':dy/length,
                'dz':dz/length
            })
            radarfirecooldown = 45

def Rring():
    if not cheatM:
        return

    glColor3f(0.0,1.0,0.4)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    for i in range(36):
        a1=math.radians(i * 10)
        a2=math.radians((i+1)*10)
        glVertex3f(helix+RR*math.cos(a1),heliy+RR* math.sin(a1),1.5)
        glVertex3f(helix+RR*math.cos(a2),heliy+RR*math.sin(a2),1.5)
    glEnd()

    glColor3f(0.2,1.0,0.2)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    for i in range(36):
        a1=math.radians(i*10)
        a2=math.radians((i+1)*10)
        glVertex3f(helix+radaranimr*math.cos(a1),heliy+radaranimr*math.sin(a1),2.0)
        glVertex3f(helix+radaranimr*math.cos(a2),heliy+radaranimr*math.sin(a2),2.0)
    glEnd()

    glLineWidth(1.0)
    glColor3f(1.0,1.0,1.0)

def world():
    ground_size=GRID_SIZE*1.2
    glBegin(GL_QUADS)
    for x in range(int(-ground_size),int(ground_size),tileS):
        for y in range(int(-ground_size),int(ground_size),tileS):
            if(((x//tileS)+(y//tileS))%2==0):
                glColor3f(0.25, 0.55, 0.2)
            else:
                glColor3f(0.18,0.42,0.14)

            glVertex3f(x,y,0)
            glVertex3f(x+tileS,y,0)
            glVertex3f(x+tileS,y+tileS,0)
            glVertex3f(x,y+tileS,0)
    glEnd()
    Rring()

    rad_yaw=math.radians(camYaw)
    rad_pitch=math.radians(camP)
    dist=280.0

    if(camMode==0):
        cx=helix-dist*math.cos(rad_pitch)*math.cos(rad_yaw)
        cy=heliy-dist*math.cos(rad_pitch)*math.sin(rad_yaw)
        cz=max(30.0,heliz+80+dist*math.sin(rad_pitch))
    elif(camMode==1):
        cx=helix+40*math.cos(rad_yaw)
        cy=heliy+40*math.sin(rad_yaw)
        cz=heliz+5
    else:
        cx=helix
        cy=heliy + 0.1
        cz=heliz + 600

    tx=helix
    ty=heliy
    tz=max(5.0, heliz)

    vx=tx-cx
    vy=ty-cy
    vz=tz-cz
    vlen=math.sqrt(vx*vx+vy*vy+vz*vz)

    if(vlen>0.0001):
        vx/=vlen
        vy/=vlen
        vz/=vlen
    else:
        vx=0.0
        vy=0.0
        vz=-1.0

    def viewDepth(x,y,z):
        return (x-cx)*vx+(y-cy)*vy+(z-cz)*vz
    renderList=[]

    for tree in trees:
        d=viewDepth(tree['x'],tree['y'],22.0*tree['scale'])
        renderList.append((d,0,'tree',tree))

    for tank in tanks:
        d=viewDepth(tank['x'],tank['y'],8.0)
        renderList.append((d,1,'tank',tank))

    for b in bombs:
        d=viewDepth(b['x'],b['y'],b['z'])
        renderList.append((d,2,'bomb',b))

    for bul in bullets:
        d=viewDepth(bul['x'],bul['y'],bul['z'])
        renderList.append((d,3,'bullet',bul))

    for exp in explosions:
        d=viewDepth(exp['x'],exp['y'],exp.get('z',0))
        renderList.append((d,4,'explosion',exp))

    for cloud in clouds:
        d=viewDepth(cloud['x'],cloud['y'],cloud['z'])
        renderList.append((d,5,'cloud',cloud))

    if(camMode!=1):
        d=viewDepth(helix,heliy,heliz)
        renderList.append((d,6,'helicopter',None))
    renderList.sort(key=lambda item:(item[0],item[1]),reverse=True)

    for m,n,item_type, obj in renderList:
        if(item_type=='tree'):
            drawTs(obj)
        elif(item_type=='tank'):
            drawTT(obj)
        elif (item_type=='bomb'):
            drawBB(obj)
        elif(item_type=='bullet'):
            TankBomb(obj)
        elif(item_type=='explosion'):
            if obj.get('is_hit',False):
                glColor3f(1.0,0.2,0.1)
            else:
                glColor3f(1.0,0.5,0.0)

            glPushMatrix()
            glTranslatef(obj['x'], obj['y'], obj.get('z',0))
            gluSphere(quadric,obj['r'],10,10)
            glPopMatrix()
        elif(item_type=='cloud'):
            drawC(obj)
        elif(item_type=='helicopter'):
            drawCopter()

def idle():
    global bladeang,score,lives,gameS,radaranimr,radaranimdir
    global heliz,heliYaw,heliR,heliP,helifallS,rotorS

    if (gameS==1):
        autoAttack()
        if(cheatM):
            radaranimr+=3.0*radaranimdir
            if (radaranimr>=RR):
                radaranimr=RR
                radaranimdir=-1
            elif(radaranimr<=0.0):
                radaranimr=0.0
                radaranimdir=1

    if (gameS==4):
        helifallS=min(3.0,helifallS+0.05)
        heliz-=helifallS

        heliYaw=(heliYaw+3.5)%360
        heliR+=1.8
        heliP+=1.2
        rotorS=max(0.0,rotorS-0.1)
        bladeang=(bladeang+rotorS)%360

        if(heliz<=12.0):
            heliz=12.0
            explosions.append({'x': helix,'y': heliy,'z': 0,'r': 15.0,'max_r': 60.0,'is_hit':False})
            gameS=3

    elif (gameS==1):
        bladeang=(bladeang+rotorS)%360

        for cloud in clouds:
            cloud['x']+=0.2
            if(cloud['x']>GRID_SIZE):
                cloud['x']=-GRID_SIZE

        for b in bombs[:]:
            b['x']+=b['dx']*14
            b['y']+=b['dy']*14
            b['z']+=b['dz']*14
            
            hit_tank=False
            for tank in tanks:
                if(math.hypot(tank['x']-b['x'],tank['y']-b['y'])<40 and b['z']<=35):
                    hit_tank=True
                    break

            if(hit_tank or b['z']<=0):
                explosions.append({'x':b['x'],'y':b['y'],'z':max(0.0,b['z']),'r':10.0,'max_r':55.0,'is_hit':False})
                if(b in bombs):
                    bombs.remove(b)

        for exp in explosions[:]:
            exp['r']+=2.5 if exp.get('is_hit',False) else 2.5
            if(exp['r']>=exp.get('max_r',55.0)):
                if(exp in explosions):
                    explosions.remove(exp)
            else:
                if(not exp.get('is_hit',False)):
                    for tank in tanks[:]:
                        if(math.hypot(tank['x']-exp['x'],tank['y']-exp['y'])<exp['r']+35):
                            if(tank in tanks):
                                tanks.remove(tank)
                                awardScore(100)
                                makeTank()

        bound=GRID_SIZE-30
        for tank in tanks:
            nx=tank['x']+math.cos(math.radians(tank['angle']))*0.8
            ny=tank['y']+math.sin(math.radians(tank['angle']))*0.8

            if (abs(nx)>bound or abs(ny)>bound):
                tank['angle']=(tank['angle']+180)%360
            else:
                tank['x']=nx
                tank['y']=ny

            if(random.random()<0.02):
                tank['angle']+=random.uniform(-45,45)

            tx,ty=helix-tank['x'],heliy-tank['y']
            tank['turret_angle']=math.degrees(math.atan2(ty,tx))-tank['angle']
            tank['shoot_timer']-=1

            if(tank['shoot_timer']<=0):
                tank['shoot_timer']=random.randint(560, 840)
                tz=heliz-10
                dist=math.sqrt(tx*tx+ty*ty+tz*tz)
                if (dist> 0):
                    if(len(bullets)>=5):
                        bullets.pop(0)
                    bullets.append({
                        'x':tank['x'],'y':tank['y'],'z':15,
                        'vx': (tx / dist)*3.5,'vy':(ty/dist)*3.5,'vz':(tz/dist)*3.5
                    })

        for bul in bullets[:]:
            bul['x']+=bul['vx']; bul['y']+=bul['vy']; bul['z']+=bul['vz']
            if (math.sqrt((bul['x']-helix)**2+(bul['y']-heliy)**2 +(bul['z']-heliz)**2)<35):
                explosions.append({
                    'x':bul['x'],
                    'y':bul['y'],
                    'z':bul['z'],
                    'r':2.0,
                    'max_r':12.0,
                    'is_hit':True
                })

                if (not cheatM):
                    loseLife()
                if(bul in bullets):
                    bullets.remove(bul)
            elif(bul['z']<0 or bul['z']>600):
                if (bul in bullets):
                    bullets.remove(bul)

    if (gameS in (3,4)):
        for exp in explosions[:]:
            exp['r']+=2.0
            if(exp['r']>=exp.get('max_r',60.0)):
                if(exp in explosions):
                    explosions.remove(exp)
    glutPostRedisplay()

def main():
    global quadric
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Sky Hunter")
    quadric = gluNewQuadric()
    genTrees(80)
    genClouds(25)
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()