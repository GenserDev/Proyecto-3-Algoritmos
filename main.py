#!/usr/bin/env python3
"""
Proyecto No. 3 -- Analisis y Diseno de Algoritmos
Seccion 10 -- Gabriel Brolo | 2026

Algoritmos implementados
------------------------
  MTF  : Move-to-Front
  IMTF : Improved Move-to-Front  (Mohanty & Tripathy)

Modelo de costo
---------------
  Acceder al elemento en la posicion i (1-indexada) de la lista
  tiene costo i.  El movimiento al frente se realiza en O(1) directo;
  solo el costo de busqueda (posicion) se contabiliza.
"""

import sys
# Force UTF-8 output so special chars don't break on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ─────────────────────────────────────────────────────────────────────────────
# Utilidades de presentacion
# ─────────────────────────────────────────────────────────────────────────────

def _section(title: str) -> None:
    bar = "=" * 70
    print(f"\n{bar}")
    print(f"  {title}")
    print(bar)


def _rule(wide: bool = False) -> None:
    print("-" * (78 if wide else 68))


# ─────────────────────────────────────────────────────────────────────────────
# MTF -- Move-to-Front
# ─────────────────────────────────────────────────────────────────────────────

def run_mtf(config: list, requests: list,
            label: str = "MTF", verbose: bool = True) -> int:
    """
    Ejecuta el algoritmo MTF sobre *requests* partiendo de *config*.

    Regla: al acceder al elemento en la posicion k (1-indexada), ese
    elemento se mueve al frente de la lista.  El costo del acceso es k.

    Retorna el costo total de accesos.
    """
    lst = list(config)
    total = 0

    if verbose:
        print(f"\n  [ {label} ]")
        print(f"  Config inicial : {lst}")
        print(f"  Solicitudes    : {requests}")
        _rule()
        print(f"  {'Config antes':<24}  {'Req':>3}  {'Costo':>5}  Config despues")
        _rule()

    for req in requests:
        before = list(lst)
        pos = lst.index(req) + 1          # posicion 1-indexada = costo
        total += pos
        lst.remove(req)
        lst.insert(0, req)               # mover al frente

        if verbose:
            print(f"  {str(before):<24}  {req:>3}  {pos:>5}  {lst}")

    if verbose:
        _rule()
        print(f"  Costo total de acceso: {total}\n")

    return total


# ─────────────────────────────────────────────────────────────────────────────
# IMTF -- Improved Move-to-Front  (Mohanty & Tripathy)
# ─────────────────────────────────────────────────────────────────────────────

def run_imtf(config: list, requests: list,
             label: str = "IMTF", verbose: bool = True) -> int:
    """
    Ejecuta el algoritmo IMTF sobre *requests* partiendo de *config*.

    Regla (look-ahead): al acceder al elemento en la posicion i, se mueve
    al frente SI Y SOLO SI el elemento aparece en los siguientes i-1
    elementos de la secuencia de solicitudes.

    Retorna el costo total de accesos.
    """
    lst = list(config)
    total = 0

    if verbose:
        print(f"\n  [ {label} ]")
        print(f"  Config inicial : {lst}")
        print(f"  Solicitudes    : {requests}")
        _rule(wide=True)
        print(f"  {'Config antes':<24}  {'Req':>3}  {'Costo':>5}  {'Mueve?':>7}  Config despues")
        _rule(wide=True)

    for idx, req in enumerate(requests):
        before = list(lst)
        pos = lst.index(req) + 1          # posicion 1-indexada = costo
        total += pos

        # Ventana look-ahead: proximos pos-1 elementos en la secuencia
        window = requests[idx + 1 : idx + pos]
        move = req in window

        if move:
            lst.remove(req)
            lst.insert(0, req)

        if verbose:
            flag = "Si" if move else "No"
            print(f"  {str(before):<24}  {req:>3}  {pos:>5}  {flag:>7}  {lst}")

    if verbose:
        _rule(wide=True)
        print(f"  Costo total de acceso: {total}\n")

    return total


# ─────────────────────────────────────────────────────────────────────────────
# Generadores de secuencias para las preguntas 3 y 4
# ─────────────────────────────────────────────────────────────────────────────

def build_min_cost_sequence(config: list, length: int = 20) -> tuple:
    """
    Construye una secuencia de *length* solicitudes con el MINIMO costo
    total de acceso en MTF.

    Estrategia: solicitar siempre el elemento que ya ocupa la posicion 1.
    Cada acceso cuesta 1 -> costo total = length.

    Justificacion de optimalidad: ningun acceso puede costar menos que 1
    (posicion minima posible), por lo que length x 1 es la cota inferior
    absoluta y la secuencia [config[0]] x length la alcanza.
    """
    seq = [config[0]] * length
    cost = run_mtf(config, seq,
                   label=f"TAREA 3 -- Minimo costo  (siempre solicitar '{config[0]}')",
                   verbose=True)
    return seq, cost


def build_worst_case_sequence(config: list, length: int = 20) -> tuple:
    """
    Construye una secuencia de *length* solicitudes con el MAXIMO costo
    total de acceso en MTF (peor caso).

    Estrategia: solicitar siempre el elemento en la ULTIMA posicion de la
    lista actual.  Ese acceso cuesta n (tamano de la lista).  Tras moverlo
    al frente, el siguiente ultimo elemento tambien queda en posicion n
    siguiendo el ciclo  [n-1, n-2, ..., 0, n-1, n-2, ...].

    Justificacion de optimalidad: con n elementos, el costo maximo por
    acceso es n.  Ninguna secuencia puede superar n x length, y esta
    estrategia lo alcanza.
    """
    lst = list(config)
    seq = []
    for _ in range(length):
        last = lst[-1]
        seq.append(last)
        lst.remove(last)
        lst.insert(0, last)              # simular MTF para el siguiente paso

    cost = run_mtf(config, seq,
                   label="TAREA 4 -- Peor caso  (siempre acceder al ultimo elemento)",
                   verbose=True)
    return seq, cost


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    CONFIG = [0, 1, 2, 3, 4]

    # ── Tarea 1 ──────────────────────────────────────────────────────────────
    _section("TAREA 1 -- MTF | secuencia 0->4 repetida cuatro veces (20 solicitudes)")
    seq1 = [0,1,2,3,4, 0,1,2,3,4, 0,1,2,3,4, 0,1,2,3,4]
    run_mtf(CONFIG, seq1, label="TAREA 1")

    # ── Tarea 2 ──────────────────────────────────────────────────────────────
    _section("TAREA 2 -- MTF | secuencia 4 3 2 1 0 1 2 3 4 3 2 1 0 1 2 3 4 (17 elem)")
    seq2 = [4,3,2,1,0, 1,2,3,4,3, 2,1,0,1,2, 3,4]
    run_mtf(CONFIG, seq2, label="TAREA 2")

    # ── Tarea 3 ──────────────────────────────────────────────────────────────
    _section("TAREA 3 -- Secuencia de 20 solicitudes con MINIMO costo en MTF")
    min_seq, min_cost = build_min_cost_sequence(CONFIG, 20)
    print(f"  Secuencia de minimo costo : {min_seq}")
    print(f"  Costo minimo total        : {min_cost}")
    print()
    print("  Justificacion:")
    print(f"  El elemento '{CONFIG[0]}' ocupa la posicion 1 desde el inicio.")
    print("  Cada acceso tiene costo 1.  Ningun acceso puede costar < 1.")
    print(f"  Cota inferior absoluta = 20 x 1 = 20  -->  alcanzada.")

    # ── Tarea 4 ──────────────────────────────────────────────────────────────
    _section("TAREA 4 -- Secuencia de 20 solicitudes con MAXIMO costo en MTF (peor caso)")
    worst_seq, worst_cost = build_worst_case_sequence(CONFIG, 20)
    print(f"  Secuencia de peor caso : {worst_seq}")
    print(f"  Costo maximo total     : {worst_cost}")
    print()
    print("  Justificacion:")
    print("  Con lista de 5 elementos, el maximo costo por acceso es 5.")
    print("  El ciclo [4,3,2,1,0] garantiza que cada elemento se encuentre")
    print("  siempre en la posicion 5 antes de ser accedido.")
    print(f"  Cota superior absoluta = 20 x 5 = 100  -->  alcanzada.")

    # ── Tarea 5 ──────────────────────────────────────────────────────────────
    _section("TAREA 5 -- Secuencias con elemento repetido 20 veces")

    seq5a = [2] * 20
    cost5a = run_mtf(CONFIG, seq5a, label="TAREA 5a -- elemento 2 repetido 20 veces")

    seq5b = [3] * 20
    cost5b = run_mtf(CONFIG, seq5b, label="TAREA 5b -- elemento 3 repetido 20 veces")

    print("  Patron observado:")
    print("  " + "-" * 60)
    print("  Sea e el elemento repetido, p su posicion inicial (1-indexada)")
    print("  y n la cantidad de repeticiones.")
    print()
    print("  Costo total = p  +  (n - 1) x 1  =  p + n - 1")
    print()
    print("  Razonamiento:")
    print("   * El primer acceso encuentra a e en su posicion inicial p -> costo p.")
    print("   * MTF mueve e al frente; todos los accesos siguientes lo hallan")
    print("     en posicion 1 -> costo 1 cada uno.")
    print()
    for elem, p in [(2, 3), (3, 4)]:
        formula = p + 20 - 1
        obtained = cost5a if elem == 2 else cost5b
        print(f"   Elemento {elem} (p={p}): {p} + (20-1)x1 = {formula}  -->  obtenido: {obtained}")

    # ── Tarea 6 ──────────────────────────────────────────────────────────────
    _section("TAREA 6 -- IMTF aplicado al mejor y peor caso de MTF")

    print("\n  -- IMTF | secuencia de MINIMO costo de MTF --\n")
    imtf_min = run_imtf(CONFIG, min_seq,
                        label="TAREA 6a -- IMTF sobre mejor caso MTF")

    print("\n  -- IMTF | secuencia de MAXIMO costo de MTF --\n")
    imtf_worst = run_imtf(CONFIG, worst_seq,
                          label="TAREA 6b -- IMTF sobre peor caso MTF")

    # ── Resumen ──────────────────────────────────────────────────────────────
    _section("RESUMEN COMPARATIVO")
    print()
    print(f"  {'Escenario':<40}  {'MTF':>7}  {'IMTF':>7}")
    print(f"  {'-' * 56}")
    print(f"  {'Mejor caso  (minimo costo MTF)':<40}  {min_cost:>7}  {imtf_min:>7}")
    print(f"  {'Peor caso   (maximo costo MTF)':<40}  {worst_cost:>7}  {imtf_worst:>7}")
    print()
    print("  Observaciones:")
    print("   * Mejor caso: ambos algoritmos tienen el mismo costo (20).")
    print("     IMTF no mueve el elemento porque ya esta en posicion 1")
    print("     (ventana de look-ahead vacia cuando i=1).")
    print("   * Peor caso: IMTF es mas eficiente que MTF.")
    print("     El look-ahead nunca detecta el elemento accedido dentro de")
    print("     la ventana, por lo que no realiza movimientos; la lista")
    print("     permanece estatica y los costos de acceso son menores.")
    print()


if __name__ == "__main__":
    main()
