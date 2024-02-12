from random import randint
class Actor:
    def __init__(self) -> None:
        self.hp:int = 10 #health
        self.maxhp:int = self.hp #max health
        self.ap:int = 3  #action points
        self.att1:int = [2,2,0] #lowest damage, highest damage, ap cost
        self.att2:int = [1,6,3] #lowest danage, highest damage, ap cost second attack
    
    def attack(attack:int, Target:Actor, self):
        if attack == 1:
            att = self.att1
        else:
            att = self.att2

        if self.ap >= att[2]:
            Target.damage(randint(att[0],att[1]))
            self.ap -= att[2]
            return 1
        else:
            return 0
    def defend():
        pass
    def damage(amoment:int):
        pass
