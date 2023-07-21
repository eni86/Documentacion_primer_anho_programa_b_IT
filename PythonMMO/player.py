class Player():
    vocation="No vocation"
    hechizo = "Puff"
    movement_speed = 50
    def __init__(self, **kargs):
       self.hit_points = kargs.get("hit_points",50)
       self.mana = kargs.get("mana",50)
       self.nombre = input("Escribe el nombre de tu jugador: ")
    
    def __str__(self):
        return "{} es un {} tiene {} HP, {} mana, puede castear {} y corre con una velocidad de {}".format(self.nombre,
                                                                                                     self.vocation,
                                                                          self.hit_points,
                                                                          self.mana,
                                                                          self.lanzar_hechizo(),
                                                                          self.movement_speed)
    
    def lanzar_hechizo(self):
        return self.hechizo

#############Acá undica que hereda todos los atributos########
############Y metodos de Player ##############################
class Sorcerer (Player):
    vocation = "Sorcerer"
    hechizo = "Utevo Lux"
    movement_speed = 30
    def lanzar_hechizo(self):
        return "{} y exura".format(self.hechizo)

class Knight(Player):
    vocation = "Knight"
    hechizo = "Exori"
    movement_speed = 60

class Druid(Player):
    vocation = "Druida"
    hechizo = "Exura Sio"
    movement_speed = 20
    
class Paladin(Player):
    vocation = "Paladin"
    hechizo = "Exana"
    movement_speed = 80

