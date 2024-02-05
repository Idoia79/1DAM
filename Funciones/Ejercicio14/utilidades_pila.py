def longitud_pila(pila):
    return len(pila)

def esta_vacia_pila(pila):
    return len(pila) == 0

def esta_llena_pila(pila, capacidad):
    return len(pila) == capacidad

def add_pila(elemento, pila, capacidad):
    if not esta_llena_pila(pila, capacidad):
        pila.append(elemento)
        print(f"Elemento '{elemento}' añadido a la pila.")
    else:
        print("La pila está llena. No se puede añadir más elementos.")

def sacar_de_la_pila(pila):
    if not esta_vacia_pila(pila):
        elemento = pila.pop()
        print(f"Elemento '{elemento}' sacado de la pila.")
        return elemento
    else:
        print("La pila está vacía. No se puede sacar más elementos.")
        return None

def escribir_pila(pila):
    if not esta_vacia_pila(pila):
        print("Elementos en la pila:")
        for elemento in reversed(pila):
            print(elemento)
    else:
        print("La pila está vacía.")

