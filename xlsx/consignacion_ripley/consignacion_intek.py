import system
import wx
from procesar_ofertas_service import procesar_ofertas_a_liquidacion
from detalle_service import detalle_intek
from regularizacion_service import regularizacion_intek
from util import PeriodSelectorPanel

def main(liquidacion_path=None, ofertas_path=None):
    output_path = procesar_ofertas_a_liquidacion(ofertas_path, liquidacion_path) # Acá podemos agregar el outputname

    
    output_path = regularizacion_intek(output_path)
    data, columns = detalle_intek(output_path)
    
    print(f"\nSe procesaron {len(data)} filas de datos.")

class ViewMain(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Procesamiento de Liquidación Intek", size=(600, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Objetos Sobre Liquidación Automática

        input_liquidacion_label = wx.StaticText(panel, label="Ruta del archivo de liquidación:")
        self.input_liquidacion = wx.TextCtrl(panel, value=str(""), style=wx.TE_READONLY)
        select_path_liquidacion_btn = wx.Button(panel, label="Buscar")

        self.period_selector = PeriodSelectorPanel(panel)

        def on_select_input(event):
            with wx.FileDialog(self, "Seleccionar archivo de liquidación", wildcard="Archivos Excel (*.xlsx)|*.xlsx",
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # El usuario canceló la selección
                path = fileDialog.GetPath()
                self.input_liquidacion.SetValue(path)
                system.liquidacion_path = path  # Actualizamos la ruta en el sistema

        select_path_liquidacion_btn.Bind(wx.EVT_BUTTON, on_select_input)

        # Objetos sobre Ofertas
        input_ofertas_label = wx.StaticText(panel, label="Ruta del archivo de ofertas:")
        self.input_ofertas = wx.TextCtrl(panel, value=str(""), style=wx.TE_READONLY)
        select_path_ofertas_btn = wx.Button(panel, label="Buscar")
        period_label = wx.StaticText(panel, label="Periodo de ofertas")

        def on_select_ofertas(event):
            with wx.FileDialog(self, "Seleccionar archivo de ofertas", wildcard="Archivos Excel (*.xlsx)|*.xlsx",
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # El usuario canceló la selección
                path = fileDialog.GetPath()
                self.input_ofertas.SetValue(path)
                system.ofertas_path = path  # Actualizamos la ruta en el sistema

        select_path_ofertas_btn.Bind(wx.EVT_BUTTON, on_select_ofertas)

        # Botón procesar
        proccess_button = wx.Button(panel, label="Procesar")
        proccess_button.Bind(wx.EVT_BUTTON, self.on_start)

        # self.start_button = wx.Button(panel, label="Iniciar Procesamiento")
        # self.start_button.Bind(wx.EVT_BUTTON, self.on_start)
        sizer.Add(input_liquidacion_label, 0, wx.LEFT | wx.TOP, 5)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.input_liquidacion, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        hsizer.Add(select_path_liquidacion_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        sizer.Add(hsizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(input_ofertas_label, 0, wx.LEFT | wx.TOP, 5)
        hsizer.Add(self.input_ofertas, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        hsizer.Add(select_path_ofertas_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        sizer.Add(hsizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        sizer.Add(period_label, 0, wx.LEFT | wx.TOP, 5)
        sizer.Add(self.period_selector, 0, wx.EXPAND | wx.ALL, 5)

        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(proccess_button, 1, wx.EXPAND | wx.RIGHT | wx.BOTTOM | wx.LEFT, 5)
        sizer.Add(hsizer, 0, wx.EXPAND | wx.ALL, 5)

        self.entry_log = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(self.entry_log, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Show()

    def on_start(self, event):
        liquidacion_path = self.input_liquidacion.GetValue()
        liquidacion_ofertas = self.input_ofertas.GetValue()
        periodo = self.period_selector.GetPeriod()
        system.periodo = periodo  # Actualizamos el periodo en el sistema
        self.entry_log.AppendText("Iniciando procesamiento...\n")
        try:
            main(liquidacion_path=liquidacion_path, ofertas_path=liquidacion_ofertas)
            self.entry_log.AppendText("Procesamiento completado exitosamente.\n")
        except Exception as e:
            self.entry_log.AppendText(f"Error durante el procesamiento: {e}\n")
    

class App(wx.App):
    def OnInit(self):
        self.frame = ViewMain()
        self.SetTopWindow(self.frame)
        return True





if __name__ == "__main__":
    app = App()
    app.MainLoop()