import os
import datetime
from pathlib import Path
from datetime import datetime

class DataAlmacen:
    def __init__(self):
        self.data = []
        self.path_raw_data = r"W:\DATA ALMACEN"
    
    def read_files(self):

        def get_files(base_path: str, files_paths: list[str] = None) -> list[str]:
            if files_paths is None: # Inicializmos nuestra lista vacía
                files_paths = []
            for path in os.listdir(base_path): # Listamos el nodo base
                new_path = os.path.join(base_path, path) # Creamos las nuevas rutas
                if os.path.isdir(new_path): # Si es un subnodo aplicamos el algoritmo nuevamente
                    get_files(new_path, files_paths)
                elif os.path.isfile(new_path): # Si es un nodo hijo lo agregamos a la lista
                    files_paths.append(new_path) 
            return files_paths
        
        self.data = get_files(self.path_raw_data)
        return self.data

    def append_data(self, dato):
        self.data.append(dato)

    def get_data(self):
        if not os.path.exists("data.csv"):
            new_data = []
            for path in self.data:
                path = Path(path)
                date = date = datetime.fromtimestamp(path.stat().st_ctime).strftime("%Y-%m-%d %H:%M:%S")
                directory = path.parent
                file_name = path.name
                status = "Nuevo"
                row = [date, directory, file_name, status]
                new_data.append(row)
            self.data = new_data
            self.save_data(Path("data.csv"))
        
            
        return self.data

    def save_data(self, file_path):
        print(f"Guardando datos en: {file_path.absolute()}")
        with open(file_path, "w") as f:
            for item in self.data:
                f.write(f"{item}\n")

    def limpiar_datos(self):
        self.data.clear()
    
if __name__ == "__main__":
    data_almacen = DataAlmacen()
    archivos = data_almacen.read_files()
    data_almacen.get_data()
