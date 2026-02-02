def calcular_centroide(poligono):
    n = len(poligono)
    area = 0
    cx = 0
    cy = 0
    for i in range(n):
        x_i, y_i = poligono[i]
        x_sig, y_sig = poligono[(i + 1) % n]
        producto_cruz = (x_i * y_sig) - (x_sig * y_i)
        area += producto_cruz
        cx += (x_i + x_sig) * producto_cruz
        cy += (y_i + y_sig) * producto_cruz
    area *= 0.5
    cx = cx / (6.0 * area)
    cy = cy / (6.0 * area)

    return (cx, cy)

def Crea_poligono():
    poligono = []
    vertices=int(input("Cuantos vertices tiene tu poligono? "))
    print("Da los vercites del poligono en sentido horario")
    for n in range(vertices):
        entrada = input(f"Vértice {n + 1} - Ingresa X y Y separados por coma: ")
        coordenadas = tuple(int(i.strip()) for i in entrada.split(","))
        poligono.append(coordenadas)
    return poligono

def main():
    poligono = Crea_poligono()
    centroide = calcular_centroide(poligono)
    print(f"El centroide del poligono es: {centroide}")

main()