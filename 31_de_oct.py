"""
n1 = 10
msg = "hola"

print(n1,msg)
print(str(n1)+msg)
print(f"{n1} {msg}")

            # hacer una funcion que reciba el nombre de una persona
            # el año de macimiento y el año actual retornando el mensaje
            #                        "hola <nombre>, tienes <edad> años"
"""
""""
def mensaje(name: str, nacimiento: int, year_actual:int) -> str:
    edad = year_actual - nacimiento
    return f"hola {name}, tienes {edad} años"

def calcu_edad()

if __name__ == "__main__":
    print(mensaje("Arceo",2001,2022))
    res = mensaje("Arce",2001,2022)
    print(res)
"""

#alumnos = ({"neto", "brian", "arceo"})

#for i in range(len(alumnos)):
#    print(f"alumnos: {alumnos}")
""""""
#sets
""" companeros = {"neto", "brian", "arceo"}
    print(f"compañeros: {companeros}")
"""

#diccionarios
"""
alumnos = {"nombre": "hugo", "materia1": 10, "materia2": 5}
print(f"companeros: {companeros}")
print(f"companeros: {alumnos}")
print(f"companero:{alumnos['nombre']}")
"""
###diferencia de listas y sets
""""
numeros_list = [1,2,4,5,2,4,5,3,6,2,3,2,5]
numeros_set = {1,2,4,5,2,4,5,3,6,2,3,2,5}
print(numeros_list)
print(numeros_set)

e = ["nombre", "est dat", "prog func", "ingles"]
alumnos = ["neto", "brian", "arceo", "neri"]
m_e_d = [7,8,9,9]
m_p_f = [9,7,10,7]
m_i = [8,9,10,9]
print(f"{e[0]:^10} {e[1]:^10} {e[2]:^10} {e[3]:^10}")

for i in range(len(alumnos)):
    #print(f"{alumnos[i]:^10}")
    print(f"{alumnos[i]:^10}{m_e_d[i]:^10} {m_p_f[i]:^10} {m_i[i]:^10}")


    def numero(mul: int, coc: int):
        for i in range(1, mul + 1):
            print(i * coc)


if __name__ == "__main__":
        numero(5, 6)