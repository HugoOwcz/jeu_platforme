
import pyxel , time

pyxel.init(150, 80, title='Pyxel Adventure', fps=60)
pyxel.load("image.pyxres")
pyxel.playm(0, True)

# 0 sol classic 8 de haut, 1 trou, 2 plateforme 2 de haut, 3 checpoint, 4 mur, 5 vide 5 de haut, 6 drapeau arrivée
# chaque chiffre correspond à 10 pixel de large

monde=[[5,5,5,5,5,5,5,5,2,2,2,2,2,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
       [5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,2,4,5,5,5,5,5,2,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
       [2,2,2,5,5,2,2,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,2,2,2,5,5,5,5,4,5,5,5,5,5,2,2,5,5,4,5,2,2,5,5,5,5,5,5,5,5,5,4,5,5,5,5,2,5,2,5,2,5,5,5,5,5,2,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,2,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5],
       [5,5,5,5,5,5,5,5,2,5,5,2,2,2,4,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,2,2,5,5,5,5,5,4,5,5,5,5,2,2,2,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,2,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,2,5,2,5,2,5,5,5,4,4,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5],
       [5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,4,5,3,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,4,5,2,5,2,5,5,2,5,5,5,2,5,4,5,5,5,5,4,4,4,5,2,5,2,5,5,2,5,2,5,4,5,5,5,4,5,5,6,5],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0]]

def update():
    joueur.mouvement()
    joueur.victoire()
    checkpoint.interraction()
    arrivee.interraction()
    checkpoint_debut.interraction()
    boss_1.mouvement()
    boss_1.collision()
    boss_1.mort()
    boss_1.fin_jeu()
    boss_2.mouvement()
    boss_2.collision()
    boss_2.mort()
    boss_2.fin_jeu()
    boss_3.mouvement()
    boss_3.collision()
    boss_3.mort()
    boss_3.fin_jeu()
    boss_4.mouvement()
    boss_4.collision()
    boss_4.mort()
    boss_4.fin_jeu()
    tortue_1.mouvement()
    tortue_2.mouvement()
    tortue_3.mouvement()
    tortue_4.mouvement()
    tortue_5.mouvement()
    tortue_6.mouvement()
    tortue_7.mouvement()
    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and (joueur.perso['vie']==0 or joueur.perso['gagne']):
        if 43<pyxel.mouse_x<103 and 37<pyxel.mouse_y<51:
            joueur.perso={'x':25,'y':63,'saut':1,'vie':5,'co_spawn':(25,63),'gagne':False,'kill':0,'etat':1}
            joueur.pos=15
            joueur.pos_mort=15
            joueur.orientation=True
            joueur.mort=[False,0]
            checkpoint.objet={'nom':'ck','etat':False,'x':None}
            checkpoint_debut.objet={'nom':'ckd','etat':False,'x':None}
            arrivee.objet={'nom':'ar','etat':False,'x':None}
            boss_1.ennemi={'etat':'vivant','vie':1,'x':0,'y':64,'nom':'B1','orientation':'gauche'}
            boss_2.ennemi={'etat':'vivant','vie':1,'x':110,'y':48,'nom':'B2','orientation':'gauche'}
            boss_3.ennemi={'etat':'vivant','vie':1,'x':0,'y':40,'nom':'B3','orientation':'gauche'}
            boss_4.ennemi={'etat':'vivant','vie':1,'x':80,'y':24,'nom':'B4','orientation':'gauche'}
            tortue_1.tortue={'y':8,'mouvement':True}
            tortue_2.tortue={'y':10,'mouvement':True}
            tortue_3.tortue={'y':12,'mouvement':False}
            tortue_4.tortue={'y':10,'mouvement':False}
            tortue_5.tortue={'y':8,'mouvement':True}
            tortue_6.tortue={'y':10,'mouvement':True}
            tortue_7.tortue={'y':12,'mouvement':False}
    if joueur.perso['vie']<=0:
        joueur.perso['co_spawn']=(1000,1000)
        joueur.perso['x']=joueur.perso['co_spawn'][0]
        joueur.perso['y']=joueur.perso['co_spawn'][1]
    if joueur.perso['y']>=85 and joueur.perso['vie']>0:
        pyxel.play(0,5)
        joueur.perso['vie']-=1
        if joueur.perso['vie']>0:
            joueur.perso['x']=joueur.perso['co_spawn'][0]
            joueur.perso['y']=joueur.perso['co_spawn'][1]
            joueur.pos=joueur.pos_mort
            joueur.mort=[True,60]
    if joueur.perso['vie']>0:
        if joueur.perso['x']>=120 and joueur.pos!=0:
            if joueur.pos < len(monde[0])-15:
                joueur.perso['x']-=10
                joueur.pos+=1
        if joueur.perso['x']<=30 and joueur.pos!=0:
            if joueur.pos > 0:
                joueur.perso['x']+=10
                joueur.pos-=1

def draw():
    if joueur.perso['vie']>0:
        pyxel.mouse(False)
        pyxel.cls(5)
        for i in range(len(monde)-1,-1,-1):
            pos=joueur.pos
            while pos<joueur.pos+15 and pos<len(monde[i]):
                if i==5:
                    if monde[i][pos]==0:
                        pyxel.blt(10*(pos-joueur.pos),72,0,0,32,5,8)
                        pyxel.blt(10*(pos-joueur.pos)+5,72,0,8,32,5,8)
                if i==4:
                    if monde[i][pos]==3:
                        if pos>38 and pos<58:
                            if checkpoint.objet['etat']:
                                checkpoint.objet['x']=None
                                pyxel.blt(10*(pos-joueur.pos),64,0,32,8,8,8)
                            else:
                                checkpoint.objet['x']=10*(pos-joueur.pos)
                                pyxel.blt(10*(pos-joueur.pos),64,0,24,8,8,8)
                        if 0<=pos<30:
                            if checkpoint_debut.objet['etat']:
                                checkpoint_debut.objet['x']=None
                                pyxel.blt(10*(pos-joueur.pos),64,0,32,8,8,8)
                            else:
                                checkpoint_debut.objet['x']=10*(pos-joueur.pos)
                                pyxel.blt(10*(pos-joueur.pos),64,0,24,8,8,8)
                    if monde[i][pos]==6:
                        if arrivee.objet['etat']:
                            arrivee.objet['x']=None
                            pyxel.blt(10*(pos-joueur.pos),64,0,33,0,7,8)
                        else:
                            arrivee.objet['x']=10*(pos-joueur.pos)
                            pyxel.blt(10*(pos-joueur.pos),64,0,24,0,7,8)
                    if monde[i][pos]==4:
                        if monde[i-1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),64,0,0,64,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,64,0,8,64,5,8)
                        else:
                            pyxel.blt(10*(pos-joueur.pos),64,0,0,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,64,0,8,56,5,8)
                    if monde[i][pos]==2:
                        pyxel.rect(10*(pos-joueur.pos),64,10,2,7)
                if i==3:
                    if monde[i][pos]==4:
                        if monde[i-1][pos]!=4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),56,0,0,64,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,56,0,8,64,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),56,0,0,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,56,0,8,56,5,8)
                        if monde[i-1][pos]!=4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),56,0,0,40,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,56,0,8,40,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),56,0,0,48,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,56,0,8,48,5,8)
                    if monde[i][pos]==2:
                        pyxel.rect(10*(pos-joueur.pos),56,10,2,7)
                if i==2:
                    if monde[i][pos]==4:
                        if monde[i-1][pos]!=4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),48,0,0,64,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,48,0,8,64,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),48,0,0,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,48,0,8,56,5,8)
                        if monde[i-1][pos]!=4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),48,0,0,40,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,48,0,8,40,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),48,0,0,48,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,48,0,8,48,5,8)
                    if monde[i][pos]==2:
                        pyxel.rect(10*(pos-joueur.pos),48,10,2,7)
                if i==1:
                    if monde[i][pos]==4:
                        if monde[i-1][pos]!=4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),40,0,0,64,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,40,0,8,64,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),40,0,0,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,40,0,8,56,5,8)
                        if monde[i-1][pos]!=4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),40,0,0,40,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,40,0,8,40,5,8)
                        if monde[i-1][pos]==4 and monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),40,0,0,48,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,40,0,8,48,5,8)
                    if monde[i][pos]==2:
                        pyxel.rect(10*(pos-joueur.pos),40,10,2,7)
                if i==0:
                    if monde[i][pos]==4:
                        if monde[i+1][pos]!=4:
                            pyxel.blt(10*(pos-joueur.pos),32,0,0,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,32,0,8,56,5,8)
                            pyxel.blt(10*(pos-joueur.pos),27,0,0,40,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,27,0,8,40,5,8)
                        if monde[i+1][pos]==4:
                            pyxel.blt(10*(pos-joueur.pos),32,0,0,48,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,32,0,8,48,5,8)
                            pyxel.blt(10*(pos-joueur.pos),27,0,0,40,5,8)
                            pyxel.blt(10*(pos-joueur.pos)+5,27,0,8,40,5,8)
                    if monde[i][pos]==2:
                        pyxel.rect(10*(pos-joueur.pos),32,10,2,7)
                pos+=1
        #pyxel.blt(142,0,0,16,24,8,8,0)
        if joueur.pos==0:
            if boss_1.ennemi['vie']==1:
                pyxel.blt(boss_1.ennemi['x'],boss_1.ennemi['y'],0,0,0,5,8)
            if boss_2.ennemi['vie']==1:
                pyxel.blt(boss_2.ennemi['x'],boss_2.ennemi['y'],0,0,8,5,8)
            if boss_3.ennemi['vie']==1:
                pyxel.blt(boss_3.ennemi['x'],boss_3.ennemi['y'],0,8,0,5,8)
            if boss_4.ennemi['vie']==1:
                pyxel.blt(boss_4.ennemi['x'],boss_4.ennemi['y'],0,8,8,5,8)
        else:
            if joueur.orientation:
                pyxel.blt(10,tortue_1.tortue['y'],0,24,16,8,8)
                pyxel.blt(30,tortue_2.tortue['y'],0,24,24,8,8)
                pyxel.blt(50,tortue_3.tortue['y'],0,24,32,8,8)
                pyxel.blt(70,tortue_4.tortue['y'],0,24,40,8,8)
                pyxel.blt(90,tortue_5.tortue['y'],0,24,32,8,8)
                pyxel.blt(110,tortue_6.tortue['y'],0,24,24,8,8)
                pyxel.blt(130,tortue_7.tortue['y'],0,24,16,8,8)
            else:
                pyxel.blt(10,tortue_1.tortue['y'],0,32,16,8,8)
                pyxel.blt(30,tortue_2.tortue['y'],0,32,24,8,8)
                pyxel.blt(50,tortue_3.tortue['y'],0,32,32,8,8)
                pyxel.blt(70,tortue_4.tortue['y'],0,32,40,8,8)
                pyxel.blt(90,tortue_5.tortue['y'],0,32,32,8,8)
                pyxel.blt(110,tortue_6.tortue['y'],0,32,24,8,8)
                pyxel.blt(130,tortue_7.tortue['y'],0,32,16,8,8)
        for i in range(5):
            if i <= joueur.perso['vie']-1:
                pyxel.blt(8*i,0,0,16,8,8,8)
            else:
                pyxel.blt(8*i,0,0,16,16,8,8)
        if joueur.mort[0]:
            pyxel.text(joueur.perso['x'],joueur.perso['y']-10,' -1 vie',0)
            joueur.mort[1]-=1
            if joueur.mort[1]==0:
                joueur.mort[0]=False
        if joueur.perso['etat']==1:
            pyxel.blt(joueur.perso['x'],joueur.perso['y'],0,8,16,5,8,0)
        if joueur.perso['etat']==2:
            pyxel.blt(joueur.perso['x'],joueur.perso['y'],0,8,24,5,8,0)
        if joueur.perso['etat']==3:
            pyxel.blt(joueur.perso['x'],joueur.perso['y'],0,0,16,5,8,0)
        if joueur.perso['etat']==4:
            pyxel.blt(joueur.perso['x'],joueur.perso['y'],0,0,24,5,8,0)
    if joueur.perso['vie']==0:
        pyxel.cls(8)
        pyxel.blt(40,20,0,0,96,8,8)
        pyxel.blt(48,20,0,8,96,8,8)
        pyxel.blt(56,20,0,0,104,8,8)
        pyxel.blt(64,20,0,8,104,8,8)
        pyxel.blt(77,20,0,0,112,8,8)
        pyxel.blt(85,20,0,8,112,8,8)
        pyxel.blt(93,20,0,0,120,8,8)
        pyxel.blt(101,20,0,8,120,8,8)
        pyxel.mouse(True)
        pyxel.rectb(43,37,60,14,0)
        pyxel.blt(45,40,0,32,96,8,8)
        pyxel.blt(53,40,0,40,96,8,8)
        pyxel.blt(61,40,0,32,104,8,8)
        pyxel.blt(69,40,0,40,104,8,8)
        pyxel.blt(77,40,0,32,112,8,8)
        pyxel.blt(85,40,0,40,112,8,8)
        pyxel.blt(93,40,0,32,120,8,8)
    if joueur.perso['gagne']:
        pyxel.cls(8)
        pyxel.blt(45,20,0,16,96,8,8)
        pyxel.blt(53,20,0,24,96,8,8)
        pyxel.blt(61,20,0,16,104,8,8)
        pyxel.blt(69,20,0,24,104,8,8)
        pyxel.blt(77,20,0,16,112,8,8)
        pyxel.blt(85,20,0,24,112,8,8)
        pyxel.blt(93,20,0,16,120,8,8)
        pyxel.mouse(True)
        pyxel.rectb(43,37,60,14,0)
        pyxel.blt(45,40,0,32,96,8,8)
        pyxel.blt(53,40,0,40,96,8,8)
        pyxel.blt(61,40,0,32,104,8,8)
        pyxel.blt(69,40,0,40,104,8,8)
        pyxel.blt(77,40,0,32,112,8,8)
        pyxel.blt(85,40,0,40,112,8,8)
        pyxel.blt(93,40,0,32,120,8,8)

class Personnage():
    def __init__(self):
        self.perso={'x':25,'y':63,'saut':1,'vie':5,'co_spawn':(25,63),'gagne':False,'kill':0,'etat':1}
        self.pos=15
        self.pos_mort=15
        self.orientation=True
        self.mort=[False,0]
    def victoire(self):
        if boss_1.ennemi['vie']==0 and boss_2.ennemi['vie']==0 and boss_3.ennemi['vie']==0 and boss_4.ennemi['vie']==0:
            self.perso['gagne']=True
    def mouvement(self):
        if pyxel.btnr(pyxel.KEY_UP) and self.perso['saut']==1:
            case_moins=20
            for i in range(20,-1,-1):
                for j in range(5):
                    if pyxel.pget(self.perso['x']+j,self.perso['y']-i)==11 or pyxel.pget(self.perso['x']+j,self.perso['y']-i)==7 or pyxel.pget(self.perso['x']+j,self.perso['y']-i)==13:
                        case_moins=i-1
                        break
            pyxel.play(0,6)
            self.perso['y']-=case_moins
            self.perso['saut']=0
        else:
            sol=False
            for i in range(5):
                if pyxel.pget(self.perso['x']+i,self.perso['y']+8)==11 or pyxel.pget(self.perso['x']+i,self.perso['y']+8)==7 or pyxel.pget(self.perso['x']+i,self.perso['y']+8)==13:
                    sol=True
            if sol:
                self.perso['saut']=1
            else:
                self.perso['y']+=0.5
        if pyxel.btn(pyxel.KEY_RIGHT) and self.perso['x']<145:
            self.orientation=True
            possible=True
            for i in range(8):
                if pyxel.pget(self.perso['x']+5,self.perso['y']+i)==11 or pyxel.pget(self.perso['x']+5,self.perso['y']+i)==7 or pyxel.pget(self.perso['x']+5,self.perso['y']+i)==13:
                    possible=False
            if possible:
                self.perso['x']+=1
        if pyxel.btn(pyxel.KEY_LEFT) and self.perso['x']>0:
            self.orientation=False
            possible=True
            for i in range(8):
                if pyxel.pget(self.perso['x']-1,self.perso['y']+i)==11 or pyxel.pget(self.perso['x']-1,self.perso['y']+i)==7 or pyxel.pget(self.perso['x']-1,self.perso['y']+i)==13:
                    possible=False
            if possible:
                self.perso['x']-=1

class Objet():
    def __init__(self,nom):
        self.objet={'nom':nom,'etat':False,'x':None}
    def interraction(self):
        if self.objet['x']!=None and self.objet['etat']==False:
            for i in range(5):
                for j in range(8):
                    if self.objet['x']+i==joueur.perso['x']+j and int(joueur.perso['y'])+1==64:
                        if self.objet['nom']=='ck':
                            self.objet['etat']=True
                            if joueur.perso['etat']==1 or joueur.perso['etat']==3:
                                joueur.perso['etat']+=1
                            joueur.perso['co_spawn']=(25,63)
                            joueur.pos_mort=51
                        if self.objet['nom']=='ar':
                            if checkpoint.objet['etat']:
                                self.objet['etat']=True
                                if joueur.perso['etat']==2:
                                    joueur.perso['etat']+=1
                                joueur.perso['co_spawn']=(135,63)
                                joueur.pos_mort=100
                                for i in range(0,5):
                                    monde[i][14]=5
                                monde[4][14]=3
                        if self.objet['nom']=='ckd':
                            self.objet['etat']=True
                            joueur.perso['co_spawn']=(135,63)
                            joueur.pos_mort=0
                            joueur.pos=0
                            joueur.perso['x']=135
                            joueur.perso['y']=63
                            if joueur.perso['etat']==3:
                                joueur.perso['etat']+=1

class Ennemi():
    def __init__(self,x,y,nom):
        self.ennemi={'etat':'vivant','vie':1,'x':x,'y':y,'nom':nom,'orientation':'gauche'}
    def mouvement(self):
        if self.ennemi['nom']=='B1':
            if self.ennemi['x']<50 and self.ennemi['orientation']=='gauche':
                self.ennemi['x']+=0.5
            if self.ennemi['x']==50 and self.ennemi['orientation']=='gauche':
                self.ennemi['orientation']='droite'
            if self.ennemi['x']>0 and self.ennemi['orientation']=='droite':
                self.ennemi['x']-=0.5
            if self.ennemi['x']==0 and self.ennemi['orientation']=='droite':
                self.ennemi['orientation']='gauche'
        if self.ennemi['nom']=='B2':
            if self.ennemi['x']<136 and self.ennemi['orientation']=='gauche':
                self.ennemi['x']+=0.5
            if self.ennemi['x']==136 and self.ennemi['orientation']=='gauche':
                self.ennemi['orientation']='droite'
            if self.ennemi['x']>110 and self.ennemi['orientation']=='droite':
                self.ennemi['x']-=0.5
            if self.ennemi['x']==110 and self.ennemi['orientation']=='droite':
                self.ennemi['orientation']='gauche'
        if self.ennemi['nom']=='B3':
            if self.ennemi['x']<27 and self.ennemi['orientation']=='gauche':
                self.ennemi['x']+=0.5
            if self.ennemi['x']==27 and self.ennemi['orientation']=='gauche':
                self.ennemi['orientation']='droite'
            if self.ennemi['x']>0 and self.ennemi['orientation']=='droite':
                self.ennemi['x']-=0.5
            if self.ennemi['x']==0 and self.ennemi['orientation']=='droite':
                self.ennemi['orientation']='gauche'
        if self.ennemi['nom']=='B4':
            if self.ennemi['x']<126 and self.ennemi['orientation']=='gauche':
                self.ennemi['x']+=0.5
            if self.ennemi['x']==126 and self.ennemi['orientation']=='gauche':
                self.ennemi['orientation']='droite'
            if self.ennemi['x']>80 and self.ennemi['orientation']=='droite':
                self.ennemi['x']-=0.5
            if self.ennemi['x']==80 and self.ennemi['orientation']=='droite':
                self.ennemi['orientation']='gauche'
    def collision(self):
        if joueur.pos==0 and joueur.perso['vie']>0 and self.ennemi['vie']==1:
            for i in range(5):
                for j in range(8):
                    if (self.ennemi['x']+i>=joueur.perso['x'] and self.ennemi['x']+i<joueur.perso['x']+5) and (self.ennemi['y']+j>=joueur.perso['y'] and self.ennemi['y']+j<joueur.perso['y']+6):
                        pyxel.play(0,7)
                        joueur.perso['vie']-=1
                        joueur.perso['x']=135
                        joueur.perso['y']=63
                        joueur.mort=[True,60]
    def mort(self):
        if joueur.pos==0 and joueur.perso['vie']>0 and self.ennemi['vie']==1:
            for i in range(5):
                if (self.ennemi['x']+i>=joueur.perso['x'] and self.ennemi['x']+i<joueur.perso['x']+5) and self.ennemi['y']==joueur.perso['y']+7:
                    pyxel.play(0,8)
                    self.ennemi['vie']=0
    def fin_jeu(self):
        if joueur.perso['vie']<=0:
            self.ennemi['x']=-1000
            self.ennemi['y']=-1000

class Tortue():
    def __init__(self,y,mouv):
        self.tortue={'y':y,'mouvement':mouv}
    def mouvement(self):
        if self.tortue['mouvement']:
            if self.tortue['y']<12:
                self.tortue['y']+=0.25
            if self.tortue['y']==12:
                self.tortue['mouvement']=False
        else:
            if self.tortue['y']>8:
                self.tortue['y']-=0.25
            if self.tortue['y']==8:
                self.tortue['mouvement']=True

joueur=Personnage()
checkpoint=Objet('ck')
checkpoint_debut=Objet('ckd')
arrivee=Objet('ar')
boss_1=Ennemi(0,64,'B1')
boss_2=Ennemi(110,48,'B2')
boss_3=Ennemi(0,40,'B3')
boss_4=Ennemi(80,24,'B4')
tortue_1=Tortue(8,True)
tortue_2=Tortue(10,True)
tortue_3=Tortue(12,False)
tortue_4=Tortue(10,False)
tortue_5=Tortue(8,True)
tortue_6=Tortue(10,True)
tortue_7=Tortue(12,False)

pyxel.run(update,draw)