import csv
import json

class TransformarCsv:

    def __init__(self):
        self._estudiantes = None


    def leer_archivo(self, ruta) -> bool:
        try:

            with open(ruta.strip(), 'r', newline='', encoding='utf-8') as archivo_csv:
                reader = csv.DictReader(archivo_csv)
                estudiantes = []
                for fila in reader:
                    estudiantes.append(fila)
            self._estudiantes = estudiantes
            return True
        except FileNotFoundError:
            print("El archivo CSV no fue encontrado.")
            return False
        except Exception as e:
            print("Ocurrió un error al leer el archivo CSV:", e)
            return False

    def escribir_archivo_json(self, ruta_destino):
        try:
            with open(ruta_destino, 'w', encoding='utf-8') as archivo_json:
                json.dump(self._estudiantes, archivo_json, indent=4, ensure_ascii=False)
            print("Archivo JSON creado exitosamente en:", ruta_destino)
        except Exception as e:
            print("Ocurrió un error al escribir el archivo JSON:", e)