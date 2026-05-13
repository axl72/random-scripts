import undetected_chromedriver as uc
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

# Configuración de Logs
logging.basicConfig(
    filename='bot_ripley.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def esperar_archivo(nombre_parcial, carpeta_descargas, timeout=120):
    carpeta = Path(carpeta_descargas)
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < timeout:
        candidatos = list(carpeta.glob(f"*{nombre_parcial}*"))
        temporales = [f for f in candidatos if f.suffix == ".crdownload"]

        if candidatos and not temporales:
            return max(candidatos, key=lambda f: f.stat().st_mtime)

        time.sleep(1)

    raise TimeoutError(f"No se encontró el archivo '{nombre_parcial}' descargado.")



def ejecutar_scraping():
    options = uc.ChromeOptions()
    # options.add_argument('--headless') 
    # options.add_argument('--headless') # Ejecuta sin ventana
    options.add_argument('--disable-gpu') # Recomendado en Windows para evitar errores de renderizado
    # options.add_argument('--window-size=1920,1080') 
    options.add_argument('--disable-save-password-bubble')
    driver = uc.Chrome(options=options, version_main=147)
    wait = WebDriverWait(driver, 20) 

    try:
        logging.info("Iniciando navegación...")
        driver.get('https://b2b.ripley.com.pe/b2bWeb/portal/logon.do')

        # --- LOGIN ---
        user_field = wait.until(EC.presence_of_element_located((By.ID, "txtCodUsuario")))
        user_field.send_keys("2060076804")
        
        pass_field = driver.find_element(By.ID, "txtPassword")
        pass_field.send_keys("INTEK.peru$25")
        
        driver.find_element(By.ID, "btnLogin").click()
        logging.info("Login clickeado.")
        print("Login realizado, navegando...")

        # --- NAVEGACIÓN ---
        # CORRECCIÓN: Para cambiar por índice, se pasa el número directamente, sin By.INDEX
        wait.until(EC.frame_to_be_available_and_switch_to_it(0))
        
        btn_reportes = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Reportes consolidados')]")))
        btn_reportes.click()
        print("Navegado a Reportes consolidados.")

        btn_diario = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Reporte consolidado diario de ventas y stock')]")))
        btn_diario.click()
        print("Navegado a Reporte consolidado diario de ventas y stock.")
        logging.info("Navegado hasta el formulario de reporte.")

        # --- MANEJO DE IFRAMES ANIDADOS ---
        driver.switch_to.default_content()
        
        # Re-entramos al primer frame
        wait.until(EC.frame_to_be_available_and_switch_to_it(0))
        
        try:
            # Intentamos buscar el campo fecha
            date_input = wait.until(EC.visibility_of_element_located((By.ID, "fechaVenta")))
            print("Campo de fecha encontrado en el primer iframe.")
        except:
            # Si no está, bajamos un nivel más al iframe hijo
            driver.switch_to.frame(0) 

        for date in ["4-05-2026", "5-05-2026", "6-05-2026","7-05-2026", "8-05-2026", "9-05-2026", "10-05-2026", "11-05-2026", "12-05-2026"]:
        # --- ACCIÓN FINAL ---
            date_input = wait.until(EC.visibility_of_element_located((By.ID, "fechaVenta")))
            date_input.clear()
            date_input.send_keys(date)
            buscar_btn = driver.find_element(By.ID, "Buscar")
            buscar_btn.click()
            time.sleep(5) # Espera para que el reporte se genere
            export_btn = driver.find_element(By.ID, "ExportarBuscar")
            export_btn.click()
            print("Fecha ingresada, iniciando exportación...")
            logging.info("Exportación iniciada con éxito.")
            archivo = esperar_archivo("Consolidado Ventas Stock Diario", str(Path.home() / "Downloads"), timeout=20)

            print("Este fue el nombre de la ultima descarga:", archivo)

        driver.quit()
    except Exception as e:
        logging.error(f"Error detectado: {str(e)}")
        print(f"Error: {e}")
    
    finally:
        print("Proceso finalizado.")

if __name__ == "__main__":
    ejecutar_scraping()