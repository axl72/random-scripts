from pathlib import Path
import pandas as pd
from datetime import date

def load_database(path: Path, index: str = None, sheet_name: str =  None) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name, dtype=str) if sheet_name else pd.read_excel(path, dtype=str)
    df.set_index(index, inplace=True) if index else None
    return df

def parsear_fecha(fecha_str: str, format= "%d-%m-%Y") -> date:
    return date.strptime(fecha_str, format)

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