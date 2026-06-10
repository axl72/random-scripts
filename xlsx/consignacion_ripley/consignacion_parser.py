import argparse
from pathlib import Path
from datetime import datetime

def parsear_argumentos():
    parser = argparse.ArgumentParser(
        description="Procesar liquidación de consignación Ripley/Intek",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Rutas de archivos
    parser.add_argument(
        "--sku",
        type=Path,
        required=True,
        help="Ruta al archivo de SKUs (ej: Ripley.xlsx)"
    )
    parser.add_argument(
        "--ofertas",
        type=Path,
        required=True,
        help="Ruta al archivo de ofertas (ej: INTEK PERU - BAZAR JUGUETES - OFERTAS - MAYO 2026.xlsx)"
    )
    parser.add_argument(
        "--liquidacion",
        type=Path,
        required=True,
        help="Ruta al archivo de liquidación original (ej: INTEK PERU_01-31.xlsx)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output.xlsx"),
        help="Ruta del archivo de salida (default: output.xlsx)"
    )

    # Fechas
    parser.add_argument(
        "--inicio",
        type=str,
        required=True,
        help="Fecha de inicio de oferta en formato YYYY-MM-DD (ej: 2026-05-09)"
    )
    parser.add_argument(
        "--fin",
        type=str,
        required=True,
        help="Fecha de fin de oferta en formato YYYY-MM-DD (ej: 2026-05-31)"
    )

    args = parser.parse_args()

    # Validar formato de fechas
    try:
        args.inicio_oferta = datetime.strptime(args.inicio, "%Y-%m-%d").date()
        args.fin_oferta = datetime.strptime(args.fin, "%Y-%m-%d").date()
    except ValueError:
        parser.error("Las fechas deben estar en formato YYYY-MM-DD (ej: 2026-05-09)")

    # Eliminar los argumentos de string crudos ya que tenemos los objetos date
    del args.inicio
    del args.fin

    return args

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    args = parsear_argumentos()
    
    # Ahora puedes usarlos así:
    print(f"SKU: {args.sku}")
    print(f"Ofertas: {args.ofertas}")
    print(f"Liquidación: {args.liquidacion}")
    print(f"Salida: {args.output}")
    print(f"Periodo: {args.inicio_oferta} a {args.fin_oferta}")