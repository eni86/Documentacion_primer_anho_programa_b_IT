########################Clase Troll en General######################################################
class Troll:
    vocation="Simple troll"
    movement_speed = 50
    accion = {"attack" : 10,"heal" : 10, "run" : movement_speed}
    loot = ["una billetera con $50"]
    
    def __init__(self,**kargs):
       self.hit_points = kargs.get("hit_points",50)
       self.mana = kargs.get("mana",50)
       self.nombre = kargs.get("troll","Basic")

    
    def __str__(self):
        return "{} es un {} tiene {} HP, {} mana, su acción fué {} con una velocidad de {} y si lo matás te ganás {}".format(self.nombre,
                                                                                                     self.vocation,
                                                                          self.hit_points,
                                                                          self.mana,
                                                                          self.lanzar_accion()[2],
                                                                          self.movement_speed, self.loot())
    
    def lanzar_accion(self):
        if self.hit_points <= 10 and self.mana >= 5:
            self.mana -=5
            self.hit_points += self.accion["heal"]
            action = "heal"
            return self.hit_points,self.mana,action
        elif self.mana > 10:
            self.mana -= 10
            action="attack"
            return self.hit_points,self.mana,action,self.accion["attack"]
        
#################################################################################################################################

class TrollMedio(Troll):
    vocation="Troll Mediano"
    movement_speed = 60
    hit_points = 60
    mana = 60
    loot = ["1 encendedor","una billetera con $100","1 mochila con 1/2 kilo de leña y astillas"]

    def lanzar_accion(self):
        if self.hit_points <= 10 and self.mana < 5:
            self.mana -= 1
            accion = "run"
        return self.hit_points,self.mana,accion


class TrollGrande(Troll):
    vocation="Troll Grande"
    movement_speed = 60
    hit_points = 80
    mana = 60
    loot = ["1 encendedor","una billetera con $200","1 mochila con 1/2 kilo de leña y astillas"] 
    def lanzar_accion(self):
        if self.hit_points <= 15 and self.mana < 5:
            self.mana -= 1
            accion = "run"
        return self.hit_points,self.mana,accion
    
class TrollDificil(Troll):
    vocation="Troll Extragrande"
    movement_speed = 60
    hit_points = 100
    mana = 60
    loot = ["1 encendedor","una billetera con $500","1 mochila con 1 kilo de leña y astillas"]

    def lanzar_accion(self):
        if self.hit_points <= 20 and self.mana < 5:
            self.mana -= 1
            accion = "run"
        return self.hit_points,self.mana,accion
