#!/usr/bin/env python3
"""
Proyecto No. 3 -- Analisis y Diseno de Algoritmos
Seccion 10 -- Gabriel Brolo | 2026

Menu principal.  Cada tarea vive en su propio modulo; este archivo
solo las importa y expone un menu interactivo.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from tarea1 import tarea1
from tarea2 import tarea2
from tarea3 import tarea3
from tarea4 import tarea4
from tarea5 import tarea5
from tarea6 import tarea6


MENU = """
======================================================================
  Proyecto 3 -- MTF / IMTF
======================================================================
  1. Tarea 1 -- MTF | secuencia 0->4 x4
  2. Tarea 2 -- MTF | secuencia mixta
  3. Tarea 3 -- Secuencia de minimo costo (20 solicitudes)
  4. Tarea 4 -- Secuencia de peor caso   (20 solicitudes)
  5. Tarea 5 -- Elemento repetido 20 veces + patron
  6. Tarea 6 -- IMTF sobre mejor y peor caso de MTF
  7. Ejecutar todas las tareas
  0. Salir
----------------------------------------------------------------------
  Opcion: """

TASKS = {
    "1": tarea1,
    "2": tarea2,
    "3": tarea3,
    "4": tarea4,
    "5": tarea5,
    "6": tarea6,
}


def run_all() -> None:
    for fn in TASKS.values():
        fn()


def main() -> None:
    while True:
        choice = input(MENU).strip()
        if choice == "0":
            print("\n  Hasta luego!\n")
            break
        elif choice == "7":
            run_all()
        elif choice in TASKS:
            TASKS[choice]()
        else:
            print("  Opcion no valida, intente de nuevo.")


if __name__ == "__main__":
    main()
