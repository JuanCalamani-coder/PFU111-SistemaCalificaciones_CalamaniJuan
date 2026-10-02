# ==========================================================
# SISTEMA DE REGISTRO DE CALIFICACIONES
# PFU-111 — Semana 9 — Grupo 1
# Estudiante: [Juan Sandy Calamani Ojeda]
# ==========================================================

def solicitar_nombre():
    """Solicita y valida el nombre del estudiante."""
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre == "":
            print("ERROR: El nombre no puede estar vacío. Inténtelo nuevamente.")
        else:
            return nombre

def solicitar_calificacion(numero):
    """Solicita y valida una calificación entre 0 y 100."""
    while True:
        entrada = input(f"Ingrese la calificación {numero} (0-100): ")
        
        try:
            calificacion = float(entrada)
        except ValueError:
            print(" ERROR: Debe ingresar un valor numérico. Inténtelo nuevamente.")
            continue
        
        if calificacion < 0:
            print("ERROR: La calificación no puede ser negativa. Inténtelo nuevamente.")
        elif calificacion > 100:
            print("ERROR: La calificación no puede ser mayor a 100. Inténtelo nuevamente.")
        else:
            return calificacion

def calcular_promedio(c1, c2, c3):
    """Calcula el promedio de tres calificaciones."""
    return (c1 + c2 + c3) / 3

def determinar_resultado(promedio):
    """Determina el resultado según el promedio."""
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

def main():
    print("=" * 50)
    print("    SISTEMA DE REGISTRO DE CALIFICACIONES")
    print("=" * 50)
    
    nombre = solicitar_nombre()
    cal1 = solicitar_calificacion(1)
    cal2 = solicitar_calificacion(2)
    cal3 = solicitar_calificacion(3)
    
    promedio = calcular_promedio(cal1, cal2, cal3)
    resultado = determinar_resultado(promedio)
    
    print("\n" + "-" * 50)
    print(f" ESTUDIANTE: {nombre}")
    print(f"   Calificación 1: {cal1:.1f}")
    print(f"   Calificación 2: {cal2:.1f}")
    print(f"   Calificación 3: {cal3:.1f}")
    print(f"   PROMEDIO: {promedio:.2f}")
    print(f"   RESULTADO: {resultado}")
    print("-" * 50)
    print("\n Proceso finalizado correctamente.")

if _name_ == "_main_":
  
    main()
