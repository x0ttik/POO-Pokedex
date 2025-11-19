# Pokedex como examen de la materia de Programacion Orientada a objetos
# Estudiantes:
# Paul Eduardo Toraya Gonzalez 
# Cristopher Alexander Santos

# Bibliotecas
from abc import ABC, abstractmethod

# Clase principal (PokemonBase)
class PokemonBase(ABC):
    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado):
        
        # Atributos

        # nombre
        if not nombre:
            self.nombre = "Sin pokemon"
        else:
            self.nombre = nombre

        # descripcion
        if not descripcion:
            self.descripcion = "No descripcion"
        else:
            self.descripcion = descripcion
        
        # ataque
        if nivel is None: 
            self.ataque = 0
        elif ataque >= 1 and ataque <= 1000:
            self.ataque = ataque
        
        # defensa
        if defensa is None:
            self.defensa = 0
        elif defensa >= 1 and defensa <= 1000:
            self.defensa = defensa

        # vida
        if vida is None:
            self.vida = 0
        elif vida >= 1 and vida <= 1000:
            self.vida = vida
        
        # nivel
        if nivel is None:
            self.nivel = 1

        elif nivel >= 1 and nivel <= 100:
            self.nivel = nivel

        # evolucion
        if evolucion is None:
            self.evolucion = 1
        else:
            if evolucion in range(1, 4): # *** VALIDACION DE CLASE HIJA
                self.evolucion = evolucion
    
        # atrapado
        self.atrapado = False
    
    # Metodos

    # Metodo abstracto (Pokemon hable)
    @abstractmethod
    def Hablar(self):
        pass

    # Metodo abstracto (Actualizar atributos pokemon)
    @abstractmethod
    def Actualizar(self):
        pass
    
    # Metodo abstracto (Detalles del pokemon)
    @abstractmethod
    def DetallesPokemon(self):
        pass

class detallesPokemon(PokemonBase):
    
    # Metodo (Detalles del pokemon)
    def DetallesPokemon(self):
        print(f"--------{self.nombre}--------")
        print(f"Descripcion: {self.descripcion}")
        print("-------------------------------")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print(f"Evolucion: {self.evolucion}")
        print("-------------------------------")
        print(f"Atrapado: {self.atrapado}")
        print("-------------------------------")

    # Metodo (Pokemon habla)
    def Hablar(self):
        print(f"¡¡¡ {self.nombre} !!!") 

    # Metodo (Entrenar pokemon (ataque - defensa - nivel))
    def Entrenar(self):
        self.ataque = self.ataque + 10
        self.defensa = self.defensa + 10
        self.nivel = self.nivel + 10
  
        if self.nivel >= 100:
            contadorEvolucion = 1
            if self.evolucion in range(1, 4):
                self.nivel = self.nivel + contadorEvolucion
    
    # Metodo (Entrena individualemnte (Ataque))
    def subirAtaque(self):
        boost_ataque = 20
        self.ataque = self.ataque + boost_ataque

    # Metodo (Entrena individualemnte (Defensa))
    def subirDefensa(self):
        boost_defensa = 20
        self.defensa = self.defensa + boost_defensa

    # Metodo (Entrena individualemnte (Ataque))
    def subirVida(self):
        boost_vida = 20
        self.vida = self.vida + boost_vida

    # Se actualizan todos los valores usando boosts
    def Actualizar(self):
        boost_ataque = 20
        boost_defensa = 20
        boost_vida = 20

        self.ataque = self.ataque + boost_ataque
        self.defensa = self.defensa + boost_defensa
        self.vida = self.vida + boost_vida

# Clase pokemon
class Pokemon(detallesPokemon):
    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado, ataque_especial):
        super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado)
        self.ataque_especial = ataque_especial
    
    # Metodo sobreescrito (Se actualizan todos los valores usando boosts)
    def Actualizar(self):
        super().Actualizar()

'''
TEMPORAL: PONERLE UN ATAQUE ESPECIAL A CADA ESPECIALIDAD
'''

# Clase pokemon con especializacion (Agua)
class PokemonAgua(Pokemon):
    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado, ataque_especial):
        super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado, ataque_especial)
        self.ataque_especial 

    # Metodo sobreescrito (Se actualizan todos los valores usando boosts)
    def Actualizar(self):
        super().Actualizar()
        print(f"Ataque especial: {self.ataque_especial}")

# Clase pokemon con especializacion (Fuego)
class PokemonFuego(Pokemon):
    # Metodo sobreescrito (Se actualizan todos los valores usando boosts)
    def Actualizar(self):
        super().Actualizar()
        print(f"Ataque especial: {self.ataque_especial}")

# Clase pokemon con especializacion (Electrico)
class PokemonElectrico(Pokemon):
    # Metodo sobreescrito (Se actualizan todos los valores usando boosts)
    def Actualizar(self):
        super().Actualizar()
        print(f"Ataque especial: {self.ataque_especial}")

# Clase pokemon con especializacion (Hierba)
class PokemonHierba(Pokemon):
    # Metodo sobreescrito (Se actualizan todos los valores usando boosts)
    def Actualizar(self):
        super().Actualizar()
        print(f"Ataque especial: {self.ataque_especial}")

class Entrenamiento(ABC):

    @abstractmethod
    def subirAtaque(self):
        pass

    @abstractmethod
    def subirDefensa(self):
        pass

    @abstractmethod
    def subirVida(self):
        pass

class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    def subirAtaque(self):
        boost_ataque = 20
        self.ataque = self.ataque + boost_ataque

    def subirDefensa(self):
        boost_defensa = 20
        self.defensa = self.defensa + boost_defensa

    def subirVida(self):
        boost_vida = 20
        self.vida = self.vida + boost_vida

pokemonPrueba = PokemonAgua("Squirtle", "Pokemon de agua", 50, 40, 60, 5, 1, False, "Pistola Agua")
pokemonPrueba.DetallesPokemon()
pokemonPrueba.Actualizar()