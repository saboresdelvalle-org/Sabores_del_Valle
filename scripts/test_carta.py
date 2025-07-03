# scripts/test_carta.py
import sys
import re

# Ubicación del archivo de la carta digital
CARTA_FILE_PATH = "carta_digital/carta.md"

def print_resultado(mensaje, exitoso):
    """Función para imprimir los resultados de las pruebas con formato."""
    if exitoso:
        print(f"✅ PASÓ: {mensaje}")
    else:
        print(f"❌ FALLÓ: {mensaje}")

def run_tests():
    """Función principal que ejecuta todas las pruebas."""
    print(f"--- Iniciando pruebas para el archivo: {CARTA_FILE_PATH} ---")
    
    try:
        with open(CARTA_FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print_resultado(f"El archivo '{CARTA_FILE_PATH}' no fue encontrado.", False)
        sys.exit(1) # Termina con código de error

    # ---- INICIO DE LAS PRUEBAS ----
    
    # Prueba 1: Verificar que el archivo no está vacío
    test_contenido_no_vacio = bool(content.strip())
    print_resultado("El archivo de la carta tiene contenido.", test_contenido_no_vacio)
    if not test_contenido_no_vacio:
        sys.exit(1)

    # Prueba 2: Verificar que cada plato tiene una línea de precio
    platos = re.findall(r'###\s.*', content) # Busca líneas que empiezan con '### '
    errores_precio = 0
    if not platos:
        print_resultado("No se encontraron platos en el formato '### Nombre del Plato'.", False)
        sys.exit(1)

    print(f"Se encontraron {len(platos)} platos. Verificando precios...")

    for plato_line in platos:
        start_index = content.find(plato_line)
        end_index_search = content.find('###', start_index + 1)
        end_index = end_index_search if end_index_search != -1 else len(content)
        seccion_plato = content[start_index:end_index]
        
        if '**Precio:**' not in seccion_plato:
            print_resultado(f"El plato '{plato_line.strip()}' no tiene una línea de **Precio:**.", False)
            errores_precio += 1
    
    test_todos_tienen_precio = (errores_precio == 0)
    print_resultado("Todos los platos definidos tienen una línea de precio.", test_todos_tienen_precio)
    if not test_todos_tienen_precio:
        sys.exit(1)

    # Prueba 3: Simulación de "Compilación" exitosa
    print_resultado("La 'compilación' (verificación de formato básico) fue exitosa.", True)

    # ---- FIN DE LAS PRUEBAS ----
    
    print("\n--- ¡Todas las pruebas críticas pasaron exitosamente! ---")
    sys.exit(0)

if __name__ == "__main__":
    run_tests()