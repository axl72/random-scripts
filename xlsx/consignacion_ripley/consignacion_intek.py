import system

path_ofertas_intek: str | None = None
liquidacion_path: str | None = None

from procesar_ofertas_service import procesar_ofertas_a_liquidacion
from detalle_service import detalle_intek
from regularizacion_service import regularizacion_intek

def main():
    output_path = procesar_ofertas_a_liquidacion(path_ofertas_intek, liquidacion_path, nombre_hoja="MAYO", nombre_tabla="Tabla")

    
    output_path = regularizacion_intek(output_path)
    data, columns = detalle_intek(output_path)
    
    print(f"\nSe procesaron {len(data)} filas de datos.")

if __name__ == "__main__":
    main()