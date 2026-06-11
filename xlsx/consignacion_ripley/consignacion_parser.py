import argparse
from pathlib import Path
from datetime import datetime

def parsear_argumentos():
    parser = argparse.ArgumentParser(
        description="Procesar liquidación de consignación Ripley/Intek",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "path_liquidacion",
        type=Path,
        help="Ruta al archivo de liquidación original (ej: INTEK PERU_01-31.xlsx)"
    )

    parser.add_argument(
        "path_ofertas",
        type=Path,
        help="Ruta al archivo de ofertas (ej: INTEK PERU - BAZAR JUGUETES - OFERTAS - MAYO 2026.xlsx)"
    )

    parser.add_argument(
        "--periodo",
        type=str,
        nargs=2,

    )

    parser.add_argument(
        "--date-format",
        type=str
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output.xlsx"),
        help="Ruta del archivo de salida (default: output.xlsx)"
    )

    args = parser.parse_args()

    if args.periodo:
        args.periodo = tuple(datetime.strptime(fecha, "%Y-%m-%d").date() for fecha in args.periodo)


    return args

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    args = parsear_argumentos()
    
    print(f"Ruta liquidación: {args.path_liquidacion} type: {type(args.path_liquidacion)}")
    print(f"Ruta ofertas: {args.path_ofertas} type: {type(args.path_ofertas)}")
    print(f"Periodo: {args.periodo} type: {type(args.periodo)}")
    print(f"Formato fecha: {args.date_format} type: {type(args.date_format)}")
    print(f"Archivo de salida: {args.output} type: {type(args.output)}")
