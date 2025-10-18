from abc import ABC, abstractmethod
import random
class Pokemon_base(ABC):
    def __init__(self):
        self.nombre = "Sin nombre"
        self.descripcion = "Sin descripción"
        self.ataque = 0
        self.defensa = 0
        self.vida = 0
        self.nivel = 0
        self.evolucion = 1
        self.max_evolucion = 3
        self.max_nivel = 100
        self.boost = 20
        self.atrapado = False
        self.maximo = False

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod    
    def actualizar(self):
        pass

    @abstractmethod
    def detalles_pokemon(self):
        pass

class Pokemon(Pokemon_base):
    def __init__(self):
        super().__init__()

    def detalles_pokemon(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Nivel: {self.nivel}")
        print(f"Evolución: {self.evolucion}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        if self.atrapado:
            print(f"Estatus: Atrapado")
        else:
            print("Estatus: Sin atrapar")

    def hablar(self):
        print(f"¡¡¡{self.nombre}!!!") 

    def entrenar(self):
        if not self.maximo:
            self.ataque += 10
            self.defensa += 10
            self.vida += 10
            self.nivel += 10
            print("Los atributos y el nivel aumentaron +10")
            print(f"Ataque: {self.ataque}")
            print(f"Ataque: {self.defensa}")
            print(f"Ataque: {self.vida}")
            print(f"Ataque: {self.nivel}")
            if self.nivel >= self.max_nivel:
                self.nivel = 0
                self.evolucion += 1
                if self.evolucion >= self.max_evolucion:
                    self.maximo = True
                    print(f"¡Felicidades {self.nombre} alcanzo el nivel maximo!")
        else:
            print(f"{self.nombre} ya ah alcanzado el nivel maximo")     
        
        #Estos metodos pertenecen a la seccion de entrenamiento
    def subir_ataque(self):
        self.ataque += self.boost
        print(f"El ataque a aumentado +{self.boost}")
        print(f"Nuevo ataque: {self.ataque}")

    def subir_defensa(self):
        self.defensa += self.boost
        print(f"La defensa aumento +{self.boost}")
        print(f"Nueva defensa: {self.defensa}")

    def subir_vida(self):
        self.vida += self.boost
        print(f"La vida aumento +{self.boost}")
        print(f"Nueva vida: {self.vida}")
    
    def actualizar(self):
        self.subir_ataque()
        print()
        self.subir_defensa()
        print()
        self.subir_vida()
    
    def editar_atributos(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.vida = int(vida)

    def editar_descripcion(self, descripcion):
        self.descripcion = descripcion

class Pokemon_agua(Pokemon):
    def __init__(self):
        super().__init__()
        self.especial = "Algo de agua"
        self.ataque_especial = 60

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print(f"Nuevo ataque {self.especial}: {self.ataque_especial}")

    def detalles_pokemon(self):
        super().detalles_pokemon()
        print("Estilo: Agua")
        print(f"Ataque especial {self.especial}: {self.ataque_especial}")

class Pokemon_fuego(Pokemon):
    def __init__(self):
        super().__init__()
        self.especial = "Algo de fuego"
        self.ataque_especial = 90

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print(f"Nuevo ataque {self.especial }: {self.ataque_especial}")

    def detalles_pokemon(self):
        super().detalles_pokemon()
        print("Estilo: Fuego")
        print(f"Ataque especial {self.especial}: {self.ataque_especial}")

class Pokemon_electrico(Pokemon):
    def __init__(self):
        super().__init__()
        self.especial = "Algo de electricidad"
        self.ataque_especial = 80

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print(f"Nuevo ataque {self.especial }: {self.ataque_especial}")

    def detalles_pokemon(self):
        super().detalles_pokemon()
        print("Estilo: Electrico")
        print(f"Ataque especial {self.especial}: {self.ataque_especial}")

class Pokemon_hierba(Pokemon):
    def __init__(self):
        super().__init__()
        self.especial = "Algo de hierba"
        self.ataque_especial = 50

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print(f"Nuevo ataque {self.especial }: {self.ataque_especial}")

    def detalles_pokemon(self):
        super().detalles_pokemon()
        print("Estilo: Hierba")
        print(f"Ataque especial {self.especial}: {self.ataque_especial}")

class Entrenamiento(ABC):
    @abstractmethod
    def subir_ataque(self):
        pass

    @abstractmethod
    def subir_defensa(self):
        pass
    
    @abstractmethod
    def subir_vida(self):
        pass

class Pokemon_con_entrenamiento(Entrenamiento, Pokemon):
    def subir_ataque(self):
        self.ataque += self.boost
        print(f"El ataque a aumentado +{self.boost}")
        print(f"Nuevo ataque: {self.ataque}")

    def subir_defensa(self):
        self.defensa += self.boost
        print(f"La defensa aumento +{self.boost}")
        print(f"Nueva defensa: {self.defensa}")

    def subir_vida(self):
        self.vida += self.boost
        print(f"La vida aumento +{self.boost}")
        print(f"Nueva vida: {self.vida}")

class Lista_pokemones:
    def __init__(self):
        self.lista = []

    def agregar_pokemon(self, pokemon):
        self.lista.append(pokemon)

    def visualizar_lista(self):
        for pokemon in self.lista:
            pokemon.detalles_pokemon()
            print()

    def remover_pokemon(self, pokemon):
        for pok in self.lista:
            if pok.nombre == pokemon.nombre:
                self.lista.remove(pok)

    def elegir_aleatorio(self):
        pokemones = self.lista
        elegido = random.choice(pokemones)
        return elegido
        

class Pokemones_atrapados(Lista_pokemones):
    def __init__(self):
        super().__init__()
    
    def agregar_pokemon(self, pokemon):
        super().agregar_pokemon(pokemon)
        pokemon.atrapado = True

def main():
    pokemones_enemigo = Lista_pokemones()
    pokemones_obtenidos = Pokemones_atrapados()

    charizard = Pokemon_fuego()
    charizard.editar_atributos("Charizard", 70, 80, 150)
    charizard.editar_descripcion("Cuando se enfurece de verdad, la llama de la punta" \
                                    " de su cola se vuelve de color azul claro.")
    
    pokemones_enemigo.agregar_pokemon(charizard)

    arcanine = Pokemon_fuego()
    arcanine.editar_atributos("Arcanine", 70, 70, 150)
    arcanine.editar_descripcion("Cuenta un antiguo pergamino que la gente se quedaba" \
                                " fascinada al verlo correr por las praderas.")
    
    pokemones_enemigo.agregar_pokemon(arcanine)

    kadabra = Pokemon()
    kadabra.editar_atributos("Kadabra", 40, 50, 100)
    kadabra.editar_descripcion("Duerme suspendido en el aire gracias a sus poderes psíquicos." \
                            " La cola, de una flexibilidad extraordinaria, hace las veces de almohada.")

    pokemones_enemigo.agregar_pokemon(kadabra)

    machop = Pokemon()
    machop.editar_atributos("Machop", 50, 50, 100)
    machop.editar_descripcion("Es una masa de músculos y, pese a su pequeño tamaño, tiene fuerza " \
                                 "de sobra para levantar en brazos a 100 personas.")
    
    pokemones_enemigo.agregar_pokemon(machop)

    pikachu = Pokemon_electrico()
    pikachu.editar_atributos("Pikachu", 40, 50, 100)
    pikachu.editar_descripcion("Cuando se enfada, este Pokémon descarga la energía que almacena en el" \
                                " interior de las bolsas de las mejillas.")
    
    pokemones_obtenidos.agregar_pokemon(pikachu)

    pokemones_enemigo.visualizar_lista()
    print()
    pokemones_obtenidos.visualizar_lista()

    elegido = pokemones_enemigo.elegir_aleatorio()
    print(f"{pikachu.nombre} tu contrincante es: {elegido.nombre}")

main()