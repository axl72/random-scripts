import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
import pandas as pd
from pathlib import Path

def procesar_ofertas_liquidacion(wb_liquidacion: openpyxl.Workbook, df_ofertas: pd.DataFrame) -> openpyxl.Workbook:
    """
    Lee una hoja de ofertas, la agrega como hoja nueva al libro de liquidación 
    (sin modificar el original) y guarda el resultado como un archivo nuevo.
    """
    nombre_tabla = "Tabla"
    nombre_hoja = "OFERTAS"

    
    # 3. Crear la hoja nueva en este libro cargado en memoria
    ws = wb_liquidacion.create_sheet(title=nombre_hoja)
    tmp_df_ofertas = df_ofertas.reset_index()
    # 4. Insertar los datos del DataFrame en la nueva hoja (conservando encabezados)
    for row in dataframe_to_rows(tmp_df_ofertas, index=False, header=True):
        ws.append(row)
        
    # 5. Convertir el rango de datos en una Tabla oficial de Excel
    max_fila = ws.max_row
    max_col = ws.max_column
    letra_col = get_column_letter(max_col)
    rango_tabla = f"A1:{letra_col}{max_fila}"
    
    nombre_tabla_limpio = nombre_tabla.replace(" ", "_")
    tabla = Table(displayName=nombre_tabla_limpio, ref=rango_tabla)
    
    # Estilo de tabla profesional con filas alternas
    estilo = TableStyleInfo(
        name="TableStyleMedium9", 
        showFirstColumn=False,
        showLastColumn=False, 
        showRowStripes=True,      
        showColumnStripes=False
    )
    tabla.tableStyleInfo = estilo
    ws.add_table(tabla)
    
    wb_liquidacion.save("temp-wb-ofertas.xlsx")
    return wb_liquidacion