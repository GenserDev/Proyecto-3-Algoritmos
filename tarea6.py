"""
Tarea 6 -- IMTF (Improved MTF, Mohanty & Tripathy) aplicado al mejor y peor
caso de MTF.

Regla look-ahead: al acceder al elemento en posicion i, se mueve al frente
solo si aparece en los proximos i-1 elementos de la secuencia de solicitudes.
"""

from algorithms import section, run_imtf
from tarea3 import build_sequence as min_seq
from tarea4 import build_sequence as worst_seq

CONFIG = [0, 1, 2, 3, 4]


def tarea6() -> tuple:
    """Retorna (costo_imtf_mejor, costo_imtf_peor)."""
    section("TAREA 6 -- IMTF aplicado al mejor y peor caso de MTF")

    best  = min_seq(CONFIG, 20)
    worst = worst_seq(CONFIG, 20)

    print("\n  -- IMTF | secuencia de MINIMO costo de MTF --\n")
    cost_min = run_imtf(CONFIG, best,
                        label="TAREA 6a -- IMTF sobre mejor caso MTF")

    print("\n  -- IMTF | secuencia de MAXIMO costo de MTF --\n")
    cost_worst = run_imtf(CONFIG, worst,
                          label="TAREA 6b -- IMTF sobre peor caso MTF")

    print("  Resumen comparativo:")
    print(f"  {'Escenario':<38}  {'MTF':>7}  {'IMTF':>7}")
    print(f"  {'-' * 54}")
    print(f"  {'Mejor caso  (minimo costo MTF)':<38}  {20:>7}  {cost_min:>7}")
    print(f"  {'Peor caso   (maximo costo MTF)':<38}  {100:>7}  {cost_worst:>7}")
    print()
    print("  Observaciones:")
    print("   * Mejor caso: IMTF == MTF (20). El elemento ya esta en pos 1;")
    print("     la ventana de look-ahead es vacia (i-1=0), nunca se mueve.")
    print("   * Peor caso: IMTF (60) < MTF (100). El look-ahead no detecta")
    print("     el elemento en la ventana -> no hay movimientos -> lista")
    print("     estatica [0,1,2,3,4] -> ciclo de costo 5+4+3+2+1=15 x 4 = 60.")

    return cost_min, cost_worst


if __name__ == "__main__":
    tarea6()
