import os
import sys
from yt_dlp import YoutubeDL

def mostrar_menu():
    print("\n" + "="*50)
    print("    DESCARGADOR UNIVERSAL ABSOLUTO (yt-dlp)    ")
    print("="*50)
    print("1. Descargar VIDEO (Máxima Calidad)")
    print("2. Descargar AUDIO (Convertir a MP3)")
    print("3. Salir")
    print("-"*50)

def descargar_universal(url, opcion):
    carpeta_salida = "Descargas_Multimedia"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Configuración avanzada para evadir bloqueos y restricciones de edad
    ydl_opts = {
        'outtmpl': f'{carpeta_salida}/%(title)s.%(ext)s',
        'noplaylist': True,
        
        # --- TRUCO UNIVERSAL: Lee las cookies de tu navegador actual ---
        # Cambia 'chrome' por 'edge', 'firefox' o 'brave' según el que uses.
        # Esto salta bloqueos de edad (adultos) y muros de Instagram/Facebook.
        'cookiesfrombrowser': ('chrome',), 
        
        # Simular ser un navegador web real para que no nos bloqueen
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        },
        'quiet': False,
        'no_warnings': False,
    }

    if opcion == '1':
        print("\n[Proceso] Extrayendo video en la máxima calidad disponible...")
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
    elif opcion == '2':
        print("\n[Proceso] Extrayendo y convirtiendo a MP3...")
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✨ ¡Completado! Guardado en la carpeta: '{carpeta_salida}'")
    except Exception as e:
        print(f"\n❌ Error crítico en la descarga. Revisa lo siguiente:\n-> {e}")

def main():
    while True:
        mostrar_menu()
        eleccion = input("Selecciona una opción (1-3): ").strip()

        if eleccion == '3':
            print("¡Nos vemos!")
            sys.exit()

        if eleccion in ['1', '2']:
            url_video = input("Pega la URL del video aquí: ").strip()
            if not url_video:
                print("❌ La URL no puede estar vacía.")
                continue
            
            descargar_universal(url_video, eleccion)
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()