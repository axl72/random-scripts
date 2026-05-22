import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font



def obtener_diccionario_desde_excel(ruta_fotos, hoja=0):
    df = pd.read_excel(ruta_fotos, sheet_name=hoja, dtype=str)

    # Normalizar columnas
    df.columns = df.columns.str.strip().str.lower()

    # Limpiar valores clave
    df["sku"] = df["sku"].str.strip()

    # Crear estructura
    resultado = (
        df.set_index("sku")[["imagenes link", "video link"]]
        .rename(columns={
            "imagenes link": "image_url",
            "video link": "video_url"
        })
        .to_dict(orient="index")
    )

    return resultado

def insertar_links_excel(
    archivo_entrada,
    archivo_salida,
    also_video_links=False,
    col_codigo="C", # Columna donde se encuentra el código SKU
    col_image_link="A", # Columna donde se insertará el link de la imagen
    col_video_link="B", # Columna donde se insertará el link del video
    dic_links=None,
    hoja=0
):
    """
    Inserta hipervínculos comparando siempre como strings.
    """
    if dic_links is None:
        raise ValueError("Debes pasar un diccionario de links {codigo: {image_url: url}}")

    wb = load_workbook(archivo_entrada)
    ws = wb[wb.sheetnames[hoja]] if isinstance(hoja, int) else wb[hoja]

    for row in range(2, ws.max_row + 1):
        valor_celda = ws[f"{col_codigo}{row}"].value
        
        if valor_celda is None:
            continue

        # PARSEO CRÍTICO: Convertimos el valor de Excel a string y limpiamos espacios
        codigo_excel = str(valor_celda).strip()

        if codigo_excel not in dic_links:
            continue 

        image_url = dic_links[codigo_excel]["image_url"]
        video_url = dic_links[codigo_excel]["video_url"]

        if image_url is not None and str(image_url).strip() and str(image_url).lower() != "nan":
            cell = ws[f"{col_image_link}{row}"]
            cell.value = "Ver Foto"  # Texto que se verá en la celda
            cell.hyperlink = image_url
            cell.font = Font(color="0000FF", underline="single")
        
        if video_url is not None and str(video_url).strip() and str(video_url).lower() != "nan":
            cell = ws[f"{col_video_link}{row}"]
            cell.value = "Ver Video"  # Texto que se verá en la celda
            cell.hyperlink = video_url
            cell.font = Font(color="0000FF", underline="single")

    wb.save(archivo_salida)
    print(f"Archivo guardado exitosamente en: {archivo_salida}")



if __name__ == "__main__":
    path = "C:\\Users\\dberrospi\\Desktop\\INTEK\\CATALOGO\\CATALOGO INTEK.xlsx"
    links = obtener_diccionario_desde_excel("C:/Users/dberrospi/Desktop/INTEK/MAESTRO PRODUCTOS INTEK.xlsx")
    insertar_links_excel(path, "CATALO INTEK .xlsx", dic_links=links, also_video_links=True)