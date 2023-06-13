from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    al1.facultad = "Fes aragin EDOMEX"
    print(" cambio")
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print(vars(al1))
    print(vars(al2))
    print("modificar atributos publicos")

    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno ("Diego",19,"Ico")
    al2 = Alumno("Monse", 20, "Derecho")


    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))

main()