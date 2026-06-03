from algorithms import section, run_mtf

CONFIG = [0, 1, 2, 3, 4]
LENGTH = 20


def tarea5() -> None:
    section("TAREA 5 -- Secuencias con elemento repetido 20 veces")

    seq_2 = [2] * LENGTH
    cost_2 = run_mtf(CONFIG, seq_2, label="TAREA 5a -- elemento 2 repetido 20 veces")

    seq_3 = [3] * LENGTH
    cost_3 = run_mtf(CONFIG, seq_3, label="TAREA 5b -- elemento 3 repetido 20 veces")

    print("  Patron observado:")
    print("  " + "-" * 58)
    print("  Costo total = p + (n - 1)  donde p = posicion inicial (1-indexada)")
    print()
    for elem, p, cost in [(2, 3, cost_2), (3, 4, cost_3)]:
        formula = p + LENGTH - 1
        print(f"   Elemento {elem} (p={p}): {p} + {LENGTH-1} = {formula}  -->  obtenido: {cost}")
    print()
    print("  El primer acceso 'paga' la posicion inicial.")
    print("  Desde el segundo acceso el elemento esta siempre al frente -> costo 1.")


if __name__ == "__main__":
    tarea5()
