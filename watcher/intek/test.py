import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# ==========================================
# CONFIGURACIÓN
# ==========================================

CARPETA = Path(r"W:\DATA ALMACEN")


# ==========================================
# FUNCIÓN DE PROCESAMIENTO
# ==========================================

def procesar_archivo(archivo: Path):
    print(f"Procesando: {archivo}")

    # Aquí colocas tu lógica.
    # Ejemplo:
    #
    # if archivo.suffix.lower() == ".csv":
    #     import pandas as pd
    #     df = pd.read_csv(archivo)
    #     print(df.head())

    print(f"Terminado: {archivo.name}")


# ==========================================
# DETECTOR DE ARCHIVOS
# ==========================================

class NuevoArchivoHandler(FileSystemEventHandler):

    def on_created(self, event):

        # Ignorar carpetas
        if event.is_directory:
            return

        archivo = Path(event.src_path)

        print(f"\nNuevo archivo detectado: {archivo.name}")

        # Esperar a que termine de copiarse
        esperar_archivo(archivo)

        procesar_archivo(archivo)


# ==========================================
# ESPERAR A QUE TERMINE LA COPIA
# ==========================================

def esperar_archivo(archivo, segundos=2):

    tamaño_anterior = -1

    while True:

        if not archivo.exists():
            time.sleep(1)
            continue

        tamaño_actual = archivo.stat().st_size

        if tamaño_actual == tamaño_anterior:
            break

        tamaño_anterior = tamaño_actual

        time.sleep(segundos)


# ==========================================
# INICIAR WATCHER
# ==========================================

def main():

    print("=" * 50)
    print("MONITOR DE ARCHIVOS")
    print("=" * 50)

    print(f"Carpeta monitoreada:")
    print(CARPETA)

    print("\nEsperando nuevos archivos...")
    print("Presiona CTRL+C para detener.\n")

    event_handler = NuevoArchivoHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        str(CARPETA),
        recursive=False
    )

    observer.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nDeteniendo monitor...")

        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()