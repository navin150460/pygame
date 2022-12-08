#  IMPORTS
import tkinter as tk
from tkinter import *
import winsound

#-------------------------------------#variable---------------------------------------------------------------------
# constan
SIZE_WIDTH = 1400
SIZE_HIEGHT = 700

UP = "right"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

isplay=False
islose=False
iswin=False

WALL1 = 1
MEN = 2
Enemy6 = 3
Enemy1 = 4
Enemy2 = 5
Enemy3 = 6
Enemy4 = 7
Enemy5 = 8
MASK = 9
HOSPITAL = 10
HOME = 11
EmptyCell = 0
ACOHOL = 12
MEDICINE = 13
VACCINE = 14
WALL2 = 15

# global
diractionEnemy1 = RIGHT
diractionEnemy2 = UP
diractionEnemy3 = UP
diractionEnemy4 = RIGHT
diractionEnemy5 = UP
diractionEnemy6 = UP

countMask = 0
countAcohol = 0
countMedicine = 0
countVaccine = 0

grid1 = [
        [ 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
        [ 15, 15, 15, 15, 15, 15, 15, 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 13, 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 9 , 1 , 0 , 0 , 0 , 0 , 1 , 12, 1 , 14, 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 12, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 0 , 14, 12, 0 , 1 , 12, 0 , 9 , 1 , 12, 1 , 1 , 1 , 9 , 1 , 9 , 12, 0 , 0 , 0 , 0 , 14, 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 1 , 1 , 0 , 1 , 13, 1 , 1 , 1 , 13, 0 , 1 , 12, 0 , 1 , 1 , 1 , 1 , 1 , 1 , 14, 1 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 12, 1 , 13, 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 12, 1 , 0 , 0 , 0 , 0 ,15],
        [ 15, 15, 15, 15, 15, 15, 15, 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 5 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 0 , 1 , 0 , 12, 13, 0 , 0 , 13, 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 12, 0 , 13, 0 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 12, 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 12, 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 1 , 1 , 1 , 1 , 0 , 1 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 12, 1 , 0 , 7 , 0 , 0 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 14, 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 8 , 0 , 0 , 1 , 0 , 9 , 1 , 12, 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 9 , 0 , 0 , 1 , 0 , 1 , 9 , 1 , 13, 1 , 9 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 13, 1 , 1 , 1 , 1 , 13, 9 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 11, 2 , 0 , 0 , 6 , 1 , 9 , 14, 0 , 1 , 0 , 0 , 0 , 1 , 0 , 12, 0 , 0 , 0 , 9 , 0 , 14, 1 , 0 , 12, 15],
        [ 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
       ]
grid2 = [
        [ 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
        [ 15, 15, 15, 15, 15, 15, 15, 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 13, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 9 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 14, 1 , 0 , 0 , 0 , 1 , 12, 0 , 9 , 1 , 12, 1 , 1 , 1 , 9 , 1 , 9 , 12, 0 , 1 , 12, 1 , 14, 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 0 , 1 , 0 , 1 , 13, 1 , 1 , 1 , 13, 0 , 1 , 12, 0 , 1 , 1 , 1 , 1 , 1 , 1 , 14, 1 , 0 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 12, 1 , 0 , 1 , 0 , 0 , 0 , 1 , 12, 9 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 12, 1 , 0 , 0 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 5 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 14, 1 , 0 , 1 , 0 , 12, 13, 0 , 0 , 13, 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 12, 0 , 13, 0 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 12, 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 12, 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 7 , 0 , 0 , 0 , 0 , 15, 0 , 1 , 0 , 1 , 12, 1 , 0 , 0 , 0 , 13, 0 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 14, 1 , 1 , 1 , 0 , 1 , 0 , 1 , 8 , 0 , 13, 1 , 0 , 9 , 1 , 1 , 12, 15],
        [ 15, 15, 15, 15, 15, 15, 15, 9 , 0 , 0 , 1 , 0 , 1 , 9 , 1 , 1 , 1 , 13, 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 9 , 15],
        [ 15, 15, 15, 15, 15, 15, 15, 11, 2 , 6 , 1 , 0 , 13, 9 , 14, 0 , 1 , 12, 0 , 0 , 0 , 0 , 12, 0 , 0 , 12, 9 , 0 , 14, 1 , 0 , 12, 15],
        [ 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
       ]

# ---------------------------------------------------------------------------------------------------------------------
# function
# ----------------------------------------------------------------------------------------------------------------------

def copyArr(arr):
    return list(map(list, arr))

# -------------------------------- drew---------------------------------------------------------------------------------
def GridGameDrawing():  
    global Enemygrid
    if lenenemy()==0:
        Enemygrid[13][32]=HOSPITAL
    if isplay:
        canvas.delete("all")
        canvas.create_image(0,0,image=City,anchor="nw")
        canvas.create_rectangle(40,10,190,55, outline="", fill="blue", tags="back2")
        canvas.create_text(110,30,text="Back",fill="white",tags="back2", font=("verdana",20, "bold"))
        canvas.tag_bind("back2", "<Button-1>", back2)

        canvas.create_rectangle(1180, 10, 1320, 55, outline="", fill = "red", tags="Exit")
        canvas.create_text(1250,30,text="Exit",fill="white", tags="Exit", font=("verdana",20, "bold"))
        canvas.tag_bind("Exit", "<Button-1>", clickToExit)
        for row in range(len(Enemygrid)):
            for col in range(len(Enemygrid[row])):
                if Enemygrid[row][col] != WALL1 and Enemygrid[row][col] != WALL2:
                    canvas.create_image(40+(40*col),80+(40*row),image=BG)
                if Enemygrid[row][col] == WALL1:
                    canvas.create_image(40+(40*col),80+(40*row),image=wall)
                if Enemygrid[row][col] == WALL2:
                    canvas.create_image(40+(40*col),80+(40*row),image=wall2)
                elif Enemygrid[row][col] == MEN:
                    canvas.create_image(40+(40*col),80+(40*row),image=DOCTOR)
                elif Enemygrid[row][col] == MASK:
                    canvas.create_image(40+(40*col),80+(40*row),image=Mask)
                elif Enemygrid[row][col] == Enemy6:
                    canvas.create_image(40+(40*col),80+(40*row), image=COVID6)
                elif Enemygrid[row][col] == Enemy1:
                    canvas.create_image(40+(40*col),80+(40*row), image=COVID1)
                elif Enemygrid[row][col] == Enemy2:
                    canvas.create_image(40+(40*col),80+(40*row),image=COVID2)
                elif Enemygrid[row][col] == Enemy3:
                    canvas.create_image(40+(40*col),80+(40*row),image=COVID3)
                elif Enemygrid[row][col] == Enemy4:
                    canvas.create_image(40+(40*col),80+(40*row),image=COVID4)
                elif Enemygrid[row][col] == Enemy5:
                    canvas.create_image(40+(40*col),80+(40*row),image=COVID5)
                elif Enemygrid[row][col] == HOSPITAL:
                    canvas.create_image(40+(40*col),80+(40*row),image=Hospital)
                elif Enemygrid[row][col] == HOME:
                    canvas.create_image(40+(40*col),80+(40*row),image=Home)
                elif Enemygrid[row][col] == ACOHOL:
                    canvas.create_image(40+(40*col),80+(40*row),image=Acohol)
                elif Enemygrid[row][col] == MEDICINE:
                    canvas.create_image(40+(40*col),80+(40*row),image=Medicine)
                elif Enemygrid[row][col] == VACCINE:
                    canvas.create_image(40+(40*col),80+(40*row),image=Vaccine)
   
        # score
        canvas.create_text(100,80,text="You score", font=('consolas', 20, 'bold'),fill="orange") 
        canvas.create_image(95,196,image=Point)          
        canvas.create_text(160,125,text=countMask, font=('consolas', 20, 'bold'),fill="orange")            
        canvas.create_text(160,170,text=countAcohol, font=('consolas', 20, 'bold'),fill="orange")                        
        canvas.create_text(160,220,text=countMedicine, font=('consolas', 20, 'bold'),fill="orange")         
        canvas.create_text(160,270,text=countVaccine, font=('consolas', 20, 'bold'),fill="orange")

        # instrution
        canvas.create_image(146,480,image=Instruction,)
            
def lost():
    global islose,isplay
    islose = True
    canvas.create_image(500,150,image=Youlose,anchor="nw")
    winsound.PlaySound("sound/lose.wav",winsound.SND_ASYNC)

def win():
    global iswin
    iswin = True
    canvas.create_image(400,150,image=Youwin,anchor="nw")
    winsound.PlaySound("sound/win.wav",winsound.SND_ASYNC)



# --------------------------------------------Men-------------------------------------------------------------------------------------------------
# find index of MEN
def startMoveMen(stadnrow,standcol,nextrow,nextcol):
    global Enemygrid,iswin,isplay
   
    if findEnemy( Enemygrid[nextrow][nextcol]):
        Enemy=kindEnemy(Enemygrid[nextrow][nextcol])
        Enemygrid[stadnrow][standcol]=EmptyCell
        Enemygrid[nextrow][nextcol]=Enemy
    elif Enemygrid[nextrow][nextcol]==HOSPITAL:
        isplay=False
        win()
    elif  Enemygrid[nextrow][nextcol]!=WALL1 and  Enemygrid[nextrow][nextcol]!=WALL2 and  Enemygrid[nextrow][nextcol]!=HOME:
        if findItem(Enemygrid[nextrow][nextcol]):
            winsound.PlaySound("sound/pick-up.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            increasItem(Enemygrid[nextrow][nextcol])
        Enemygrid[stadnrow][standcol]=EmptyCell
        Enemygrid[nextrow][nextcol]=MEN
    GridGameDrawing()

def positionMen():
    global Enemygrid
    indexOfone=[]
    for row in range(len(Enemygrid)):
        for col in range(len(Enemygrid[row])):
            if Enemygrid[row][col]==MEN:
             indexOfone.append(row)
             indexOfone.append(col)
    return indexOfone

def moveMen(move):
    posittion=positionMen()
    indexrow=posittion[0]
    indexcol=posittion[1]
    if move==RIDGE:
        startMoveMen(indexrow,indexcol,indexrow,indexcol+1)
    elif move==LEFT:
        startMoveMen(indexrow,indexcol,indexrow,indexcol-1)
    elif move==UP:
        startMoveMen(indexrow,indexcol,indexrow-1,indexcol)
    elif move==DOWN:
        startMoveMen(indexrow,indexcol,indexrow+1,indexcol)

def moveleft(event):
   
    moveMen(LEFT)   
def moveright(event):
    moveMen(RIDGE)   
def moveUp(event): 
    moveMen(UP)
def movedown(event):
    moveMen(DOWN)

# ---------------------------------item in game-------------------------------------------------------------------------
# find item in game
def findItem(column):
    return(column==MASK or column==ACOHOL or column==VACCINE or column==MEDICINE)

# icreas point
def increasItem(cell):
    global Enemygrid,countAcohol,countMask,countMedicine,countVaccine
    if cell==ACOHOL:
        countAcohol+=1
    elif cell==MEDICINE:
        countMedicine+=1
    elif cell==VACCINE:
        countVaccine+=1
    elif  cell==MASK:
         countMask+=1


# --------------------------------------------Enemy function-----------------------------------------------------------------------------------
# len enemy
def lenenemy():
    global Enemygrid
    countEnemy=0
    for row in Enemygrid:
        for col in row:
            if col==Enemy1 or col== Enemy2 or col==Enemy3 or col==Enemy4 or col==Enemy5 or col==Enemy6:
                countEnemy+=1

    return countEnemy

# find enemy  
def findEnemy(cell):
    return (cell==Enemy1 or cell==Enemy2 or cell==Enemy3 or cell==Enemy4 or cell==Enemy5 or cell==Enemy6)
   
# kind of enemy
def kindEnemy(cell):
    global countAcohol,countMask,countMedicine,countVaccine,isplay,islose
    KindEnemy=None
    if cell==Enemy1:
        if countMask>=4 and countVaccine>=3:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countMask-=4
            countVaccine-=3
        else:
            KindEnemy=Enemy1
            isplay=False
            lost()
    elif cell==Enemy2 :
        if countAcohol>=2 and countMedicine>=5:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countAcohol-=2
            countMedicine-=5
        else:
            KindEnemy=Enemy2
            isplay=False
            lost()
    elif cell==Enemy3 :
        if countMedicine>=3 and countMask>=2:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countMedicine-=3
            countMask-=2
        else:
            KindEnemy=Enemy3
            isplay=False
            lost()
    elif cell==Enemy4 :
        if countVaccine>=4 and countAcohol>=4:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countAcohol-=4
            countVaccine-=4
        else:
            
            KindEnemy=Enemy4
            isplay=False
            lost()
    elif cell==Enemy5 :
        if countAcohol>=6 and countMedicine>=1:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countAcohol-=6
            countMedicine-=1
        else:
            
            KindEnemy=Enemy5
            isplay=False
            lost()
    elif cell==Enemy6 :
        if countMask>=5 and countAcohol>=5:
            # winsound.PlaySound("sound/kill.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            winsound.PlaySound("sound/hit.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            KindEnemy=MEN
            countMask-=5
            countAcohol-=5
        else:

            KindEnemy=Enemy6
            isplay=False
            lost()
    return KindEnemy

# find position of enemy
def positionMonster():
    global Enemygrid
    indexEnemy1=[]
    indexEnemy2=[]
    indexEnemy3=[]
    indexEnemy4=[]
    indexEnemy5=[]
    indexEnemy6=[]
    for row in range(len(Enemygrid)):
        for col in range(len(Enemygrid[row])):
            if Enemygrid[row][col]==Enemy1:
                indexEnemy1.append(row)
                indexEnemy1.append(col)
            elif Enemygrid[row][col]==Enemy2:
                 indexEnemy2.append(row)
                 indexEnemy2.append(col)
            elif Enemygrid[row][col]==Enemy3:
                 indexEnemy3.append(row)
                 indexEnemy3.append(col)
            elif Enemygrid[row][col]==Enemy4:
                 indexEnemy4.append(row)
                 indexEnemy4.append(col)
            elif Enemygrid[row][col]==Enemy5:
                 indexEnemy5.append(row)
                 indexEnemy5.append(col)
            elif Enemygrid[row][col]==Enemy6:
                 indexEnemy6.append(row)
                 indexEnemy6.append(col)
    indexEnemy=[indexEnemy1,indexEnemy2,indexEnemy3,indexEnemy4,indexEnemy5,indexEnemy6]   
    return indexEnemy


def moveEn(En,standrow,standcol,nextrow,nextcol):
    global Enemygrid,isplay,islose
    if  Enemygrid[nextrow][nextcol]==MEN:
        isplay=False
        # islose=True
        lost()
    Enemygrid[standrow][standcol]=EmptyCell
    Enemygrid[nextrow][nextcol]=En
    
    GridGameDrawing()

# Enemy1
def moveEnemy1(): 
    global Enemygrid,diractionEnemy1
    indexOfMonster=positionMonster()
    # check index
    indexrow=indexOfMonster[0][0]
    indexcol=indexOfMonster[0][1]

    
    if (diractionEnemy1==RIGHT) and (indexcol==len(Enemygrid[0])-3): 
        diractionEnemy1=LEFT
    elif (diractionEnemy1==LEFT) and ( Enemygrid[indexrow][indexcol-1]==WALL2): 
        diractionEnemy1=RIGHT

    if  diractionEnemy1==RIGHT:
            moveEn(Enemy1,indexrow,indexcol,indexrow,indexcol+1)
    elif diractionEnemy1==LEFT:
        moveEn(Enemy1,indexrow,indexcol,indexrow,indexcol-1)
    canvas.after(500,lambda: moveEnemy1()) 
    

# Enemy2
def moveEnemy2(): 
    global Enemygrid,diractionEnemy2
    indexOfMonster=positionMonster()

    # check index
    indexrow=indexOfMonster[1][0]
    indexcol=indexOfMonster[1][1]
    if (diractionEnemy2==UP) and (Enemygrid[indexrow-1][indexcol]==WALL2): 
       diractionEnemy2=DOWN
    elif (diractionEnemy2==DOWN) and (indexrow==len(Enemygrid)-6): 
        diractionEnemy2=UP
    
    if  diractionEnemy2==UP:
        moveEn(Enemy2,indexrow,indexcol,indexrow-1,indexcol)
    elif diractionEnemy2==DOWN:
        moveEn(Enemy2,indexrow,indexcol,indexrow+1,indexcol)

    canvas.after(500,lambda: moveEnemy2()) 

# Enemy3
def moveEnemy3(): 
    global Enemygrid,diractionEnemy3
    indexOfMonster=positionMonster()

    # check index
    indexrow=indexOfMonster[2][0]
    indexcol=indexOfMonster[2][1]
    if (diractionEnemy3==UP) and (Enemygrid[indexrow-1][indexcol]==WALL1): 
       diractionEnemy3=DOWN
    elif (diractionEnemy3==DOWN) and ( Enemygrid[indexrow+1][indexcol]==WALL2): 
        diractionEnemy3=UP
    
    # 2 - Move   
    if  diractionEnemy3==UP:
        moveEn(Enemy3,indexrow,indexcol,indexrow-1,indexcol)
    elif diractionEnemy3==DOWN:
        moveEn(Enemy3,indexrow,indexcol,indexrow+1,indexcol)

    # 3 - Move again
    canvas.after(500,lambda: moveEnemy3()) 


# enemy4
def moveEnemy4(): 
    global Enemygrid,diractionEnemy4
    indexOfMonster=positionMonster()

    # check index
    indexrow=indexOfMonster[3][0]
    indexcol=indexOfMonster[3][1]
    if (diractionEnemy4==RIGHT) and (Enemygrid[indexrow][indexcol+1]==WALL2): 
        diractionEnemy4=LEFT
    elif (diractionEnemy4==LEFT) and ( Enemygrid[indexrow][indexcol-1]==WALL1): 
        diractionEnemy4=RIGHT
    
    # move   
    if  diractionEnemy4==RIGHT:
        moveEn(Enemy4,indexrow,indexcol,indexrow,indexcol+1)
    elif diractionEnemy4==LEFT:
        moveEn(Enemy4,indexrow,indexcol,indexrow,indexcol-1)
    # 3 - Move again
    canvas.after(500,lambda: moveEnemy4()) 
    
# Enemy5-
def moveEnemy5(): 
    global Enemygrid,diractionEnemy5
    indexOfMonster=positionMonster()

    # check index
    indexrow=indexOfMonster[4][0]
    indexcol=indexOfMonster[4][1]
    if (diractionEnemy5==UP) and (Enemygrid[indexrow-1][indexcol]==WALL1): 
       diractionEnemy5=DOWN
    elif (diractionEnemy5==DOWN) and ( Enemygrid[indexrow+1][indexcol]==WALL1): 
        diractionEnemy5=UP
    
    # move
    if  diractionEnemy5==UP:
        moveEn(Enemy5,indexrow,indexcol,indexrow-1,indexcol)
    elif diractionEnemy5==DOWN:
        moveEn(Enemy5,indexrow,indexcol,indexrow+1,indexcol)
    
    # 3 - Move again
    canvas.after(500,lambda: moveEnemy5()) 

# Enemy6
def moveEnemy6(): 
    global Enemygrid,diractionEnemy6
    indexOfMonster=positionMonster()

    # check index
    indexrow=indexOfMonster[5][0]
    indexcol=indexOfMonster[5][1]
    if (diractionEnemy6==RIGHT) and (Enemygrid[indexrow][indexcol+1]==WALL1): 
       diractionEnemy6=LEFT
    elif (diractionEnemy6==LEFT) and ( Enemygrid[indexrow][indexcol-1]==WALL1): 
        diractionEnemy6=RIGHT
    
    # 2 - Move   

    if  diractionEnemy6==RIGHT:
        moveEn(Enemy6,indexrow,indexcol,indexrow,indexcol+1)
    elif diractionEnemy6==LEFT:
        moveEn(Enemy6,indexrow,indexcol,indexrow,indexcol-1)
    
    # 3 - Move again
    canvas.after(500,lambda: moveEnemy6())      

# for kill enemy

# -------------------------------main---------------------------------------------------------------
root = tk.Tk()
root.geometry(str(SIZE_WIDTH)+"x"+str(SIZE_HIEGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")


# image----------------------------------------------------------------------------
back2_img = PhotoImage(file="image/back.png")
BG = PhotoImage(file="image/floor.png")
wall = PhotoImage(file="image/Brick1.png")
wall2 = PhotoImage(file="image/Brick2.png")
DOCTOR = PhotoImage(file="image/men.png")
Hospital = PhotoImage(file="image/door.png")
Home = PhotoImage(file="image/home.png")
Mask = PhotoImage(file="image/mask.png")
Acohol = PhotoImage(file="image/acohol.png")
Medicine = PhotoImage(file="image/medicine.png")
Vaccine = PhotoImage(file="image/vaccine.png")
City = PhotoImage(file="image/backround.png")
City2 = PhotoImage(file="image/backround2.png")
Instruction = PhotoImage(file="image/instructionImage.png")
Point = PhotoImage(file="image/pointImage.png")
LoseBG= PhotoImage(file="image/losebg.png")
Youlose =PhotoImage(file="image/you-lose-red-rubber-stamp-over-white-background-86701650.png")
WinBG = PhotoImage(file="image/winbg.png")
Youwin = PhotoImage(file="image/youwin.png")
bglevel= PhotoImage(file="image/backgroundlevel.png")
choose= PhotoImage(file="image/ChooseLevel.png")
back= PhotoImage(file="image/backbutton.png")
COVID1 = PhotoImage(file="virus/covid1.png")
COVID2 = PhotoImage(file="virus/covid2.png")
COVID3 = PhotoImage(file="virus/covid3.png")
COVID4 = PhotoImage(file="virus/covid4.png")
COVID5 = PhotoImage(file="virus/covid5.png")
COVID6 = PhotoImage(file="virus/covid6.png")
COVID7 = PhotoImage(file="virus/covid7.png")


# call function------------------------------------------------------------------------
def clickToExit(event):
	root.destroy()
def clickToStart(event):
   winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
   canvas.after(1000, lambda:level())
def level1(event):
     global Enemygrid, isplay
     isplay = True
     Enemygrid= copyArr(grid1)
     winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
     canvas.after(100,GridGameDrawing())
     moveEnemy1()
     moveEnemy2()
     moveEnemy3()
     moveEnemy4()
     moveEnemy5()
     moveEnemy6()
   
def level2(event):
   global Enemygrid, isplay
   isplay = True
   Enemygrid= copyArr(grid2)
   canvas.after(100,GridGameDrawing())
   moveEnemy1()
   moveEnemy2()
   moveEnemy3()
   moveEnemy4()
   moveEnemy5()
   moveEnemy6()
   

#Create canvas --------------------------------------------------------
	#Start game -------------------------------------------------------
canvas.delete("all")
canvas.create_image(0,0, image=City,anchor="nw")
canvas.create_rectangle(550,400,850,500, outline="" ,fill="red", tags="Start")
canvas.create_rectangle(550,250,850,350, outline="" ,fill="green", tags="Exit")
canvas.create_text( 700,300,text="Start", font=("courier","50", "bold"), tags="Start")
canvas.create_text( 700,450,text="Exit", font=("courier","50", "bold"), tags="Exit")
canvas.tag_bind("Start", "<Button-1>", clickToStart)
canvas.tag_bind("Exit", "<Button-1>", clickToExit)


# -----------------------------------------------------------------------
	# Level---------------------------------------------------------------
def level():
    global countAcohol,countMask,countVaccine,countMedicine
  
    countMask = 0
    countAcohol = 0
    countMedicine = 0
    countVaccine = 0
    canvas.delete('all')
    canvas.create_image(0,0, image=City,anchor="nw")
    canvas.create_image(270,150, image=bglevel,anchor="nw")
    canvas.create_image(500,150, image=bglevel,anchor="nw")
    canvas.create_image(550,200, image=choose,anchor="nw")
    canvas.create_image(400,300, image=choose,anchor="nw", tags="Level1")
    canvas.create_image(700,300, image=choose,anchor="nw", tags="Level2")
    canvas.create_image(1000,450, image=back,anchor="nw", tags="Level1")
    canvas.create_text(685,250, text=" Level",fill="orange", font=("courier","25", "bold"))
    canvas.create_text(540,350, text="Level1", font=("courier","20", "bold"), tags="Level1")
    canvas.create_text(840,350, text="Level2", font=("courier","20", "bold"), tags="Level2")
    canvas.tag_bind("Level2","<Button-1>", level2)
    canvas.tag_bind("Level1","<Button-1>", level1)

    
def back2(event):
    global islose, isplay
    islose = False
    isplay = False
    winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.after(100,level())


# -------------------------------------------------------------------------------

winsound.PlaySound("sound/startGame.wav",winsound.SND_LOOP | winsound.SND_ASYNC)
# event call function------------------------------------------------------------------
root.bind('<Left>',moveleft)
root.bind('<Right>',moveright)
root.bind('<Up>',moveUp)
root.bind('<Down>',movedown)
    


root.mainloop()