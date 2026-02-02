# Input: point (x,y), polygon vertices [(x1,y1), (x2,y2), ..., (xn,yn)]
# Output: True if point is inside polygon, False otherwise

def is_point_in_polygon(point, vertices):#funcion
    num_intersections = 0
    num_vertices = len(vertices)

    for i in range(num_vertices):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % num_vertices]  # wrap around to first vertex for last edge
        if ((v1[1] > point[1]) != (v2[1] > point[1])) and \
                (point[0] < (v2[0] - v1[0]) * (point[1] - v1[1]) / (v2[1] - v1[1]) + v1[0]):
            num_intersections += 1
    return num_intersections % 2 == 1

# Para poder utilizar la funcion recibe un par ordenado como punto y como poligono una lista de pares ordenados

def Crea_poligono():
    poligono = []
    vertices=int(input("Cuantos vertices tiene tu poligono? "))
    print("Da los vercites del poligono en sentido horario")
    for n in range(vertices):
        entrada = input(f"Vértice {n + 1} - Ingresa X y Y separados por coma: ")
        coordenadas = tuple(int(i.strip()) for i in entrada.split(","))
        poligono.append(coordenadas)
    return poligono

def Crea_cordenada():
    entrada = input("Ingresa las coordenada del punto  X y Y separadas por una coma: ")
    coordenada = [int(n) for n in entrada.split(",")]
    return coordenada

def main():
    poligono=Crea_poligono()
    punto=Crea_cordenada()
    resultado = is_point_in_polygon(punto,poligono)
    if (resultado==True):
        print("El punto esta dentro del poligono")
    else:
        print("El punto no esta dentro del poligono")

main()