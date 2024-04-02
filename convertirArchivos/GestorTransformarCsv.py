from TransformarCsv import TransformarCsv

class GestorTransformar:

    def __init__(self):
        self._transformar_csv = TransformarCsv

    def ejecutar(self):
        ruta_archivo_csv = input("Ingrese la ruta del archivo CSV: "
                                 "(ejemplo: C:/Users/sebas/Documents/software/Tarea3/estudiantes.csv): ")

        transformador = TransformarCsv()
        estudiantes = transformador.leer_archivo(ruta_archivo_csv.strip())
        if estudiantes:
            ruta_destino_json = ruta_archivo_csv.replace('.csv', '.json')
            transformador.escribir_archivo_json(ruta_destino_json)

    # Ejemplo de uso:
if __name__ == "__main__":
    gestor = GestorTransformar()
    gestor.ejecutar()

