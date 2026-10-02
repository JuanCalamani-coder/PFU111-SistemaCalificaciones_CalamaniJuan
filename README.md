# Sistema de Registro de Calificaciones

## Descripción
Programa que permite registrar tres calificaciones de un estudiante, calcular su promedio y determinar si aprueba o reprueba. Incluye validación completa de entradas y manejo de errores para evitar fallos inesperados.

## Funcionalidades
- Registro de nombre del estudiante
- Ingreso de tres calificaciones
- Cálculo automático del promedio
- Determinación de estado: Aprobado / Reprobado
- Visualización detallada de resultados

## Validaciones implementadas
- Nombre no puede estar vacío
-  Calificaciones entre 0 y 100
-  Rechazo de valores negativos
-  Rechazo de valores mayores a 100
-  Rechazo de texto donde se espera número

## Manejo de errores
- Entrada de texto en campos numéricos → solicita nuevamente
- Valores fuera de rango → informa y vuelve a pedir
- Valores vacíos → rechaza y solicita corrección
- El programa *nunca se cierra inesperadamente*

## Tecnologías utilizadas
-  Python 3
-  Git — Control de versiones
-  GitHub — Alojamiento del repositorio
-# PFU111-SistemaCalificaciones_CalamaniJuan
Sistema de Registro de calificaciones-PFU-111 Semana9
