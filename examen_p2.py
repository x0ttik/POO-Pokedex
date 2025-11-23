from abc import ABC, abstractmethod
import random
import os
import time

def limpiar_terminal():
    os.system('cls')

def efecto_espera():
    time.sleep(1) 

def continuar():
    print()
    input("Presiona 'Enter' para continuar")
    print()

class rango_invalido(Exception):
    pass

def validar_valor(min, max):
    valor = int(input(" >"))
    print()
    if valor < min or valor > max:
        raise rango_invalido(f"Valor fuera de rango")
    return valor

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
        self.name_evo = None
        self.name_evo_2 = None
        self.sonido = None


    def agregar_nombres_evo(self, a, b):
        self.name_evo = a
        self.name_evo_2 = b

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
        if self.sonido:
            print(f"¡¡¡{self.sonido}!!!")
        else:
            print(f"¡¡¡{self.nombre}!!!") 

    def agregar_sonido(self, sonido):
        self.sonido = sonido

    def entrenar(self):
        if not self.maximo:
            self.ataque += 10
            self.defensa += 10
            self.vida += 10
            self.nivel += 10
            print("Los atributos y el nivel aumentaron +10")
            print(f"Ataque: {self.ataque}")
            print(f"Defensa: {self.defensa}")
            print(f"Vida: {self.vida}")
            print(f"Nivel: {self.nivel}")
            if self.nivel >= self.max_nivel:
                self.nivel = 0
                self.evolucion += 1
                if self.evolucion == 2:
                    if self.name_evo:
                        print(f"¡¡¡{self.nombre} alcanzo la evolución {self.evolucion} ahora es {self.name_evo}!!!")
                        self.nombre = self.name_evo
                    else: 
                        print(f"¡¡{self.nombre} alcanzo la evolucion {self.evolucion}!!")    
                if self.evolucion >= self.max_evolucion:
                    self.maximo = True
                    if self.name_evo_2:
                        print(f"¡Felicidades {self.nombre} alcanzo el nivel maximo ahora es {self.name_evo_2} !")
                        self.nombre = self.name_evo_2
                    else:
                        print(f"¡¡¡{self.nombre} alcanzo en nivel de evolución maximo!!!")    
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
        self.ataque_especial = 80

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print("Ataque especial aumento +20")
        print(f"Ataque especial {self.especial }: {self.ataque_especial}")

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
        print("Ataque especial aumento +20")
        print(f"Ataque especial {self.especial }: {self.ataque_especial}")

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
        print("Ataque especial aumento +20")
        print(f"Ataque especial {self.especial }: {self.ataque_especial}")

    def detalles_pokemon(self):
        super().detalles_pokemon()
        print("Estilo: Electrico")
        print(f"Ataque especial {self.especial}: {self.ataque_especial}")

class Pokemon_hierba(Pokemon):
    def __init__(self):
        super().__init__()
        self.especial = "Algo de hierba"
        self.ataque_especial = 70

    def actualizar(self):
        super().actualizar()
        self.ataque_especial += self.boost
        print("Ataque especial aumento +20")
        print(f"Ataque especial {self.especial }: {self.ataque_especial}")

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
        for i, pokemon in enumerate(self.lista):
            print(i+1, "-")
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
    
    def cantidad_pokemones(self):
        return len(self.lista)
        

class Pokemones_atrapados(Lista_pokemones):
    def __init__(self):
        super().__init__()
    
    def agregar_pokemon(self, pokemon):
        super().agregar_pokemon(pokemon)
        pokemon.atrapado = True 

def iniciar_personajes():
    pokemones_enemigo = Lista_pokemones()
    pokemones_obtenidos = Pokemones_atrapados()
    pokemones_eleccion = Lista_pokemones()

    charizard = Pokemon_fuego()
    charizard.editar_atributos("Charizard", 80, 100, 150)
    charizard.editar_descripcion("Cuando se enfurece de verdad, la llama de la punta" \
                                    " de su cola se vuelve de color azul claro.")
    charizard.evolucion = 3
    charizard.maximo = True

    arcanine = Pokemon_fuego()
    arcanine.editar_atributos("Arcanine", 70, 90, 150)
    arcanine.editar_descripcion("Cuenta un antiguo pergamino que la gente se quedaba" \
                                " fascinada al verlo correr por las praderas.")
    arcanine.evolucion = 3
    arcanine.maximo = True

    kadabra = Pokemon()
    kadabra.editar_atributos("Abra", 40, 50, 100)
    kadabra.editar_descripcion("Duerme suspendido en el aire gracias a sus poderes psíquicos." \
                            " La cola, de una flexibilidad extraordinaria, hace las veces de almohada.")
    kadabra.agregar_nombres_evo("Kadabra", "Alakazam")

    machop = Pokemon()
    machop.editar_atributos("Machop", 50, 50, 100)
    machop.editar_descripcion("Es una masa de músculos y, pese a su pequeño tamaño, tiene fuerza " \
                                 "de sobra para levantar en brazos a 100 personas.")
    machop.agregar_nombres_evo("Machoke", "Machamp")
    
    pokemones_enemigo.agregar_pokemon(kadabra)
    pokemones_enemigo.agregar_pokemon(machop)
    pokemones_enemigo.agregar_pokemon(arcanine)
    pokemones_enemigo.agregar_pokemon(charizard)

    pikachu = Pokemon_electrico()
    pikachu.editar_atributos("Pichu", 40, 50, 100)
    pikachu.editar_descripcion("Cuando se enfada, este Pokémon descarga la energía que almacena en el" \
                                " interior de las bolsas de las mejillas.")
    pikachu.agregar_nombres_evo("Pikachu", "Raichu")

    squirtle = Pokemon_agua()
    squirtle.editar_atributos("Squirtle", 30, 50, 100)
    squirtle.editar_descripcion("Tras nacer, se le hincha el lomo y se le forma un caparazón. Escupe poderosa " \
                                "espuma por la boca.")
    squirtle.agregar_nombres_evo("Wartortle", "Blastoise")

    bulbasaur = Pokemon_hierba()
    bulbasaur.editar_atributos("Bulbasaur", 40, 70, 100)
    bulbasaur.editar_descripcion("Tras nacer, crece alimentándose durante un tiempo de los nutrientes que contiene el" \
                                    " bulbo de su lomo.")
    
    cyndaquil = Pokemon_fuego()
    cyndaquil.editar_atributos("Cyndaquil", 60, 80, 100)
    cyndaquil.editar_descripcion("Suele estar encorvado. Si se enfada o se asusta, lanzará llamas por el lomo")
    cyndaquil.agregar_nombres_evo("Quilava", "Typhlosion")

    pokemones_eleccion.agregar_pokemon(pikachu)
    pokemones_eleccion.agregar_pokemon(squirtle)
    pokemones_eleccion.agregar_pokemon(bulbasaur)
    pokemones_eleccion.agregar_pokemon(cyndaquil)

    print("Elige tu primer Pokemon...")

    efecto_espera()
    pokemones_eleccion.visualizar_lista()

    try:
        op = int(input(">>"))
        i = op - 1
        pokemon = pokemones_eleccion.lista[i]
    except IndexError:
        pokemon = pokemones_eleccion.elegir_aleatorio()
        print()
        print("Error de indice, se eligió un Pokemon aleatorio")
        continuar()
    except ValueError:
        pokemon = pokemones_eleccion.elegir_aleatorio()
        print("Error de valor, se esperaba un número entero")
        print("Se eligió un pokemon aleatorio")
        continuar()
    except:
        print("Error inensperado. Se eligio un pokemon aleatorio")
        pokemon = pokemones_eleccion.elegir_aleatorio()
        continuar()
    finally:
        pokemones_obtenidos.agregar_pokemon(pokemon)

    return pokemones_obtenidos, pokemones_enemigo

def mostrar_vida(vida):
    for i in range(vida):
        print("*", end = "")
    print(f"   {vida}")

def combatir(nosotros, contrincante):
    vida_nosotros = nosotros.vida
    vida_contrincante = contrincante.vida

    ataque_nosotros = nosotros.ataque
    ataque_contrincante = contrincante.ataque

    defensa_nosotros = nosotros.defensa
    defensa_contrincante = contrincante.defensa

    nosotros_esp = False
    contrincante_esp = False

    if isinstance(nosotros, (Pokemon_electrico, Pokemon_fuego, Pokemon_agua, Pokemon_hierba)):
        nosotros_esp = True
        nosotros_especial = nosotros.ataque_especial
    
    if isinstance(contrincante, (Pokemon_electrico, Pokemon_fuego, Pokemon_agua, Pokemon_hierba)):
        contrincante_esp = True
        contrincante_especial = contrincante.ataque_especial
    
    while True:
        print(f"{nosotros.nombre}:  ", end = "")
        mostrar_vida(vida_nosotros)
        print("Defensa:  ", end = "")
        mostrar_vida(defensa_nosotros)
        print()
        print(f"{contrincante.nombre}:  ", end = "")
        mostrar_vida(vida_contrincante)
        print(f"Defensa:  ", end= "")
        mostrar_vida(defensa_contrincante)
        print()
        print()
        if vida_contrincante == 0:
            return True
        elif vida_nosotros == 0:
            return False
        print("1- Atacar")
        print("2- Pasar turno")
        print("3- Huir")
        if nosotros_esp:
            print("4- Ataque especial")
        op = int(input(">>"))

        if op == 1:
            if defensa_contrincante > 0:
                defensa_contrincante -= ataque_nosotros
                if defensa_contrincante <= 0:
                    vida_contrincante += defensa_contrincante
                    defensa_contrincante = 0
                    if vida_contrincante <= 0:
                        vida_contrincante = 0
            elif vida_contrincante > 0:
                vida_contrincante -= ataque_nosotros
                if vida_contrincante <= 0:
                    vida_contrincante = 0

            print(f"{nosotros.nombre} atacó a {contrincante.nombre}")
        elif op == 2:
            print("Pasaste turno")
        elif op == 3:
            return False  
            
        elif nosotros_esp and op == 4:
            print(f"Usaste tu ataque especial {nosotros.especial}")
            if defensa_contrincante > 0:
                defensa_contrincante -= nosotros_especial
                if defensa_contrincante <= 0:
                    vida_contrincante += defensa_contrincante
                    defensa_contrincante = 0
                    if vida_contrincante <= 0:
                        vida_contrincante = 0
            elif vida_contrincante > 0:
                vida_contrincante -= nosotros_especial
                if vida_contrincante <= 0:
                    vida_contrincante = 0  
                    
        if contrincante_esp:
            op_contrincante = random.randint(1,3)
        else:
            op_contrincante = random.randint(1,2)

        if op_contrincante == 1:
            if defensa_nosotros > 0:
                defensa_nosotros -= ataque_contrincante
                if defensa_nosotros <= 0:
                    vida_nosotros += defensa_nosotros
                    defensa_nosotros = 0
                    if vida_nosotros <= 0:
                        vida_nosotros = 0
            elif vida_nosotros > 0:
                vida_nosotros -= ataque_contrincante
                if vida_nosotros <= 0:
                    vida_nosotros = 0

            print(f"{contrincante.nombre} atacó a {nosotros.nombre}")

        elif op_contrincante == 2:
            print("El contrincante paso su turno")
            
        elif contrincante_esp and op_contrincante == 3:
            print(f"El contrincante uso su ataque especial {contrincante.especial}")
            if defensa_nosotros > 0:
                defensa_nosotros -= contrincante_especial
                if defensa_nosotros <= 0:
                    vida_nosotros += defensa_nosotros
                    defensa_nosotros = 0
                    if vida_nosotros <= 0:
                        vida_nosotros = 0
            elif vida_nosotros > 0:
                vida_nosotros -= contrincante_especial
                if vida_nosotros <= 0:
                    vida_nosotros = 0  
        bloque()  

def bloque():
    limpiar_terminal()
    print()
    print()
    print("---------------------------------------------------")
    print()
    print()
   
def menu():

    print("1- Seleccionar pokemon")
    print("2- Detalles de mi pokemon")
    print("3- Hablar pokemon")
    print("4- Entrenamiento")
    print("5- Combatir")
    print("6- Crear pokemon enemigo")
    print("7- Salir")
    


def main():
    nombre_usuario = input("Nombre: ")
    print(f"Bienvenido a la pokedex {nombre_usuario}")
    pokemones_obtenidos, pokemones_enemigos = iniciar_personajes()
    pokemon = pokemones_obtenidos.lista[0]
    bloque()

    print(f"Tu nuevo pokemon es {pokemon.nombre}")
    print()
    pokemon.detalles_pokemon()
    continuar()
    limpiar_terminal()

    while True:
        print()
        print("-"*48)
        print()

        print(f"Usuario: {nombre_usuario}")
        print()
        print(f"Pokemon actual: {pokemon.nombre}")
        print()
        print()

        menu()
        while True:
            try:
                opcion = int(input(">>"))
                break
            except ValueError:
                print("Error de valor. ¡Ingresa Una opción valida!") 
       

        if opcion == 1:
            bloque()
            print("Seleccionar Pokemon")
            print()
            pokemones_obtenidos.visualizar_lista()
            cantidad = pokemones_obtenidos.cantidad_pokemones()
            
            if cantidad == 1:
                print("No puedes elegir otra opción")
                continuar()
                limpiar_terminal()
            else:
                while True:
                    try:
                        op = int(input("Elige un pokemon: "))
                        i = op - 1     
                        pokemon = pokemones_obtenidos.lista[i]
                        print(f"Seleccionaste a {pokemon.nombre}")
                        break
                    except ValueError:
                        print("Error de valor. Escribe un numero entero")
                    except IndexError:
                        print(f"Error de indice. rango (1-{cantidad})")    
                                
        
        elif opcion == 2:
            bloque()
            print("Detalles de mi pokemon")
            pokemon.detalles_pokemon()
            continuar()
            limpiar_terminal()

        elif opcion == 3:
            bloque()
            print("Hablar")
            print()
            pokemon.hablar()
            continuar()
            limpiar_terminal()

        elif opcion == 4:
            while True:
                bloque()
                print("Entrenamiento") 
                print()
                print("1- Entrenamiento normal") 
                print("2- Entrenamiento individual")
                print("3- Entrenamiento intensivo")
                print("4- Entrenamiento personalizado")
                print("5- Volver al principio")

                while True:
                    try:
                        entrenar_op = validar_valor(1, 5)
                        break
                    except ValueError:
                        print("Error de valor. Ingresa un numero entero.")
                    except rango_invalido as e:
                        print("Error de rango. Elige una opcion valida.")

                if entrenar_op < 5:
                    bloque()
                    print("Entrenamiento")
                    print()
                    pokemon.detalles_pokemon()
                    print()

                if entrenar_op == 1:
                    print()
                    print("Entrenamiento normal")
                    print()
                    pokemon.entrenar()
                    continuar()
                elif entrenar_op == 2:
                    while True:
                        print()
                        print("Entrenamiento individual")
                        print()
                        print("1- Subir ataque")
                        print("2- Subir defensa")
                        print("3- Subir vida")
                        print("4- Volver")
    
                        try:
                            individual_op = validar_valor(1, 4)
                        except ValueError:
                            print("Error de valor. Escribe un numero entero")
                            efecto_espera()
                            bloque()
                            pokemon.detalles_pokemon()
                            continue
                        except rango_invalido:
                            print("Error de rango. Elige una de las opciones")
                            efecto_espera()
                            bloque()
                            pokemon.detalles_pokemon()
                            continue

                        if individual_op == 1:
                            pokemon.subir_ataque()
                        elif individual_op == 2:
                            pokemon.subir_defensa()
                        elif individual_op == 3:
                            pokemon.subir_vida()
                        elif individual_op == 4:
                            print("Volviendo...")
                            efecto_espera()
                            break
                        else: 
                            pass
                        
                        continuar()
                        limpiar_terminal()  
                        pokemon.detalles_pokemon()
                                
                elif entrenar_op == 3:
                    pokemon.actualizar()
                    continuar()

                elif entrenar_op == 4:
                    while True:
                        print("Entrenamiento personalizado")
                        print()
                        print("---Nuevos atributos---")
                        print()
                        print("Rango: 50 - 300")
                        print()
                        try:
                            print("Ataque")
                            ataque = validar_valor(50, 300)
                            print("Defensa")
                            defensa = validar_valor(50, 300)
                            print("Vida")
                            vida = validar_valor(50, 300)
                            break
                        except ValueError:
                            print("Los valores deben ser numeros enteros.")
                            efecto_espera()
                            bloque() 
                            pokemon.detalles_pokemon()
                        except rango_invalido as e:
                            print(e)
                            efecto_espera()
                            bloque() 
                            pokemon.detalles_pokemon()    
                    nombre = pokemon.nombre
                    pokemon.editar_atributos(nombre, ataque, defensa, vida )
                    print()
                    print("Resultados:")
                    print()
                    pokemon.detalles_pokemon()
                    continuar()
                elif entrenar_op == 5:
                    print("Volviendo...")
                    efecto_espera()
                    limpiar_terminal()
                    break    
                else:
                    pass

        elif opcion == 5:
            bloque()
            print("Combatir")
            if pokemones_enemigos.cantidad_pokemones():
                print("Eligiendo contrincante...")
                enemigo = pokemones_enemigos.elegir_aleatorio()
                print()
                print()
                print(f"{pokemon.nombre} VS {enemigo.nombre}")
                print()
                print()
                pokemon.detalles_pokemon()
                print()
                print()
                enemigo.detalles_pokemon()
                bloque()
                resultado = combatir(pokemon, enemigo)
                bloque()
                if resultado:
                    pokemones_obtenidos.agregar_pokemon(enemigo)
                    pokemones_enemigos.remover_pokemon(enemigo)
                    print(f"¡¡¡Felicidades has atrapado a {enemigo.nombre}!!!")
                    print()
                    print("Ahora lo puedes encontrar en la sección para seleccionar Pokemon")
                else:
                    print(f"¡{enemigo.nombre} te derroto, sigue entrenando!")

            else:
                print()
                print("Ya has atrapado a todos los pokemon en el programa")
                print("Crea un nuevo enemigo para seguir combatiendo")
                print()

        elif opcion == 6:
            bloque()
            print("Crear enemigo")
            nombre = input("Nombre del pokemon")
            descripcion = input("Descripción: ")
            ataque = int(input("Ataque(10-100): "))
            defensa = int(input("Defensa: "))
            vida = int(input("Vida: "))
            print("Naturaleza: ")
            print(" 1- N/A")
            print(" 2- Agua")
            print(" 3- Fuego")
            print(" 4- Electrico")
            print(" 5- Hierba")
            naturaleza = int(input(">>"))
              
            if naturaleza == 2:
                nuevo_pokemon = Pokemon_agua()
            elif naturaleza == 3:
                nuevo_pokemon = Pokemon_fuego()
            elif naturaleza == 4:
                nuevo_pokemon = Pokemon_electrico()
            elif naturaleza == 5:
                nuevo_pokemon = Pokemon_hierba()
            else:
                nuevo_pokemon = Pokemon()

            nuevo_pokemon.editar_atributos(nombre, ataque, defensa, vida)
            nuevo_pokemon.editar_descripcion(descripcion)

            pokemones_enemigos.agregar_pokemon(nuevo_pokemon)
            print(f"Se agrego {nuevo_pokemon.nombre} a la lista de enemigos")
            print("¡Ahora podras combatir contra el en la sección de combate!")

        elif opcion == 7:
            bloque()
            print("Saliendo del programa...")
            break
        else:
            bloque()
            print("Elige una opcion valida")
                


main()