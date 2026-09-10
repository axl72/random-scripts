from pathlib import Path
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from datetime import datetime
from util import load_database
from consignacion_parser import parsear_argumentos
import json

# with open("config.json", "r", encoding="utf-8") as f:
#     config = json.load(f)

# args = parsear_argumentos()

# Estilos
styles = {
    "fill_celeste": PatternFill(start_color="B7DEE8", end_color="B7DEE8", fill_type="solid"),
    "fill_naranja": PatternFill(start_color="E26B0A", end_color="E26B0A", fill_type="solid"),
    "font_negro_negrita": Font(bold=True, color="000000", size=8),
    "font_blanco": Font(bold=False, color="FFFFFF", size=10),
    "alignment_centro_ajustado": Alignment(horizontal="center", vertical="center", wrap_text=True),
    "formato_moneda": '_("S/"* #,##0.00_);_("S/"* -#,##0.00_);_("S/"* "-"??_);_(@_)'
}

# path_sku_intek = Path(config["path_sku_intek"])
path_ofertas_intek = Path(r"C:\Users\abernabel\Desktop\INTEK\7. CLIENTES\RIPLEY OFERTAS\INTEK PERU - BAZAR JUGUETES - OFERTAS  - JULIO 2026.xlsx")
# path_ofertas_intek = args.path_ofertas
liquidacion_path = Path(r"C:\Users\abernabel\Desktop\INTEK\7. CLIENTES\RIPLEY\CONSIGNACION\CONSIGNACION 2026 8 AGOSTO\INTEK PERU_01-31.xlsx")
# liquidacion_path = args.path_liquidacion
output_path = Path("output.xlsx")
# output_path = args.output

inicio_oferta = "2026-07-17"
fin_oferta = "2026-07-31"
inicio_oferta_dt = datetime.strptime(inicio_oferta, "%Y-%m-%d")
fin_oferta_dt = datetime.strptime(fin_oferta, "%Y-%m-%d")
periodo = (inicio_oferta_dt, fin_oferta_dt) # La variable periodo es una tupla de objetos datetime que representa el rango de fechas de las ofertas

date_format = "%d - %b - %Y"