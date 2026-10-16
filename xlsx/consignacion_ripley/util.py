from pathlib import Path
import pandas as pd
from datetime import date
from datetime import datetime
import locale

try:
    locale.setlocale(locale.LC_ALL, 'es_PE.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'Spanish')

def load_database(path: Path, index: str = None, sheet_name: str =  None) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name, dtype=str) if sheet_name else pd.read_excel(path, dtype=str)
    df.set_index(index, inplace=True) if index else None
    return df

def load_data(sku_path: str, ofertas_path: str):
    print("Parametros pasados: ",sku_path, ofertas_path)
    df_sku = load_database(Path(sku_path), index="SKU", sheet_name="SKU")  # Carga y muestra el DataFrame para verificar que se lee correctamente

    df_ofertas = pd.read_excel(Path(ofertas_path), dtype=str)  # Carga y muestra el DataFrame para verificar que se lee correctamente
    df_ofertas = df_ofertas[["SKU RIPLEY", "DESCRIPCIÓN RIPLEY", "PRECIO MASTER", "PRECIO PROMO HOT SALES", "FECHA INICIO", "FECHA FIN", "STOCK UND", "RECO PROVEEDOR (SIN IGV)", "% DSCTO"]]
    df_ofertas.set_index("SKU RIPLEY", inplace=True)  # Establecer la columna "SKU RIPLEY" como índice
    
    return df_sku, df_ofertas

def parsear_fecha(fecha_str: str, format= "%d-%m-%Y") -> date:
    print("Fecha a parsear: ", fecha_str)
    meses = {
        "ene": 1,
        "feb": 2,
        "mar": 3,
        "abr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "ago": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dic": 12,
        "Set": 9,  # Para manejar la abreviatura "Set" como septiembre
    }

 


    fecha_str = fecha_str.split(" ")[0]  # Tomamos solo la parte de la fecha, ignorando la hora si está presente
    # año, mes, dia = fecha_str.split("-")
    # print(año, mes, dia[0])
    # input("Presiona Enter para continuar...")
    # fecha = datetime(int(año), int(mes), int(dia[0])).date()
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    
    return fecha

import wx
import wx.adv

class PeriodSelectorPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Selector de fecha inicial
        main_sizer.Add(wx.StaticText(self, label="Desde:"), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        self.picker_start = wx.adv.DatePickerCtrl(self, style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        main_sizer.Add(self.picker_start, 0, wx.RIGHT, 15)
        
        # Selector de fecha final
        main_sizer.Add(wx.StaticText(self, label="Hasta:"), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        self.picker_end = wx.adv.DatePickerCtrl(self, style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        main_sizer.Add(self.picker_end, 0)
        
        self.SetSizer(main_sizer)
        
        # Vincular eventos para validación de rango
        self.picker_start.Bind(wx.adv.EVT_DATE_CHANGED, self.validate_range)
        self.picker_end.Bind(wx.adv.EVT_DATE_CHANGED, self.validate_range)

    def validate_range(self, event):
        start = self.picker_start.GetValue()
        end = self.picker_end.GetValue()
        
        # Si la fecha de inicio es mayor a la de fin, igualamos la de fin
        if start.IsValid() and end.IsValid() and start > end:
            self.picker_end.SetValue(start)
        

    def GetPeriod(self):
        """Retorna una tupla con los objetos wx.DateTime de inicio y fin."""
        start_wx, end_wx =  self.picker_start.GetValue(), self.picker_end.GetValue()
        start_date = date(start_wx.GetYear(), start_wx.GetMonth() + 1, start_wx.GetDay()) if start_wx.IsValid() else None
        end_date = date(end_wx.GetYear(), end_wx.GetMonth() + 1, end_wx.GetDay()) if end_wx.IsValid() else None
        return start_date, end_date