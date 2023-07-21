import random

class Arma:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

class Personaje:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.arma_actual = None
        self.nivel = 1
        self.experiencia = 0

    def equipar_arma(self, arma):
        self.arma_actual = arma

    def atacar(self, enemigo):
        if not self.arma_actual:
            print(f"{self.nombre} no tiene un arma equipada.")
            return

        danio = self.fuerza + self.arma_actual.poder
        print(f"{self.nombre} ataca a {enemigo.nombre} con {self.arma_actual.nombre} y causa {danio} de daño.")
        enemigo.recibir_danio(danio)

    def recibir_danio(self, danio):
        danio_recibido = max(0, danio - self.defensa)
        self.vida -= danio_recibido
        print(f"{self.nombre} recibe {danio_recibido} de daño.")
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{self.nombre} tiene {self.vida} puntos de vida restantes.")

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        print(f"{self.nombre} gana {experiencia} puntos de experiencia.")
        if self.experiencia >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        print(f"{self.nombre} ha subido de nivel a {self.nivel}!")
        self.vida += 10
        self.fuerza += 5
        self.defensa += 2

class Enemigo:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa

    def atacar(self, personaje):
        danio = self.fuerza
        print(f"{self.nombre} ataca a {personaje.nombre} y causa {danio} de daño.")
        personaje.recibir_danio(danio)

def main():
    espada = Arma("Espada", 10)
    personaje_principal = Personaje("Héroe", 100, 20, 5)
    personaje_principal.equipar_arma(espada)

    enemigo = Enemigo("Dragón", 150, 25, 8)

    while personaje_principal.vida > 0 and enemigo.vida > 0:
        personaje_principal.atacar(enemigo)
        if enemigo.vida > 0:
            enemigo.atacar(personaje_principal)

    if personaje_principal.vida <= 0:
        print("Has sido derrotado. Game Over.")
    else:
        print("¡Has derrotado al enemigo!")

if __name__ == "__main__":
    main()