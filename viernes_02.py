
enca = ["nombre", "est dat", "prog func", "ingles"]
alumnos = ["neto", "brian" "arceo", "neri"]
m_e_d = [7, 8, 9, 9]
m_p_f = [9, 7, 10, 7]
m_i = [8, 9, 10, 9]

def reporte(fmt: int):
    print(f"{enca[0]:^{fmt}} {enca[1]:^{fmt})} {enca[2]:^{fmt}} {enca[3]:^{fmt}}")
    for i in range(len(alumnos)):
        print(f"{alumnos[i]:^10}{m_e_d[i]:^10} {m_p_f[i]:^10} {m_i[i]:^10}")

if __name__ == "__main__":
    reporte(15)
"""
#separacion por coma
numerobig = 123458295567
print(f"{numerobig:,d}")  # decima

#fijar decimales
numero_Pi = 3.14156878345546789
print(f"{numero_Pi:.3f}")

#notacion cientifica
numero_Pi = 3.14156878345546789
print(f"{numero_Pi:e}")
print(f"{numero_Pi:.2e}")

#porcentaje
num_porciento = 0.2543617745
print(f"{num_porciento:%}")
print(f"{num_porciento:.2%}")

#numeros binarios
print(f"{15:b}")

#unicodes
print(f"{65:c}")
print(f"{65:x}")
print(f"{255:o}")
"""
"""
def producto(num1: int,num2: int,fmt: int):
    return num1*num2
def tablas(eme: int, ene: int,fmt: int):
    for i in range(1,m+1):
        tabla(n,i,fmt)
        #mul=5*i
        #print(f"5 * {i} = {mul}")
def tabla():
    mul=5*i
    print(f"5 * {i} = {mul}")
if __name__ == "__main__":
    tabla()
"""


"""
tabla_desde = 1 #tablas del 1...
tabla_hasta = 10 #...al 10
desde = 1 #multiplicaciones desde el 1...
hasta = 10 #...hasta el 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print() #línea en blanco al final de cada tabla
	"""