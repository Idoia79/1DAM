def longitud_cola(cola):
    return len(cola)

def esta_vacia_cola(cola):
    return len(cola) == 0

def esta_llena_cola(cola, capacidad):
    return len(cola) == capacidad

def add_cola(elemento, cola, capacidad):
    if not esta_llena_cola(cola, capacidad):
        cola.append(elemento)
        print(f"Elemento '{elemento}' añadido a la cola.")
    else:
        print("La cola está llena. No se puede añadir más elementos.")

def sacar_de_la_cola(cola):
    if not esta_vacia_cola(cola):
        elemento = cola.pop(0)
        print(f"Elemento '{elemento}' sacado de la cola.")
        return elemento
    else:
        print("La cola está vacía. No se puede sacar más elementos.")
        return None

def escribir_cola(cola):
    if not esta_vacia_cola(cola):
        print("Elementos en la cola:")
        for elemento in cola:
            print(elemento)
    else:
        print("La cola está vacía.")