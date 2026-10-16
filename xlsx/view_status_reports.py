from pathlib import Path
import pandas as pd

reports_path = r"C:\Users\abernabel\Desktop\.REPORTES"

reports = {
    r"C:\Users\abernabel\Desktop\.REPORTES\Tottus.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\VEGA NUEVO.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Ripley.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Falabella.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Tai Loy.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Ilahui.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Cencosud.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Multicenter.xlsx", 
    r"C:\Users\abernabel\Desktop\.REPORTES\Estilos.xlsx"
}

reports_df = {}
for report in reports:
    report_path = Path(report)
    print(f"Leyendo archivo {report_path}")
    sells_df = pd.read_excel(report_path, sheet_name="VENTAS")
    print(f"Fecha máxima de ventas: {sells_df['FECHA'].max()}")
    stock_df = pd.read_excel(report_path, sheet_name="STOCK")
    print(f"Fecha máxima de stock: {stock_df['FECHA'].max()}")
    df_list = [sells_df, stock_df]
    reports_df[report] = df_list





