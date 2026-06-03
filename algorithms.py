"""
Nucleo compartido: algoritmos MTF e IMTF y utilidades de presentacion.
Importado por cada modulo de tarea.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ── Presentacion ──────────────────────────────────────────────────────────────

def section(title: str) -> None:
    bar = "=" * 70
    print(f"\n{bar}")
    print(f"  {title}")
    print(bar)


def rule(wide: bool = False) -> None:
    print("-" * (78 if wide else 68))


# ── MTF -- Move-to-Front ──────────────────────────────────────────────────────

def run_mtf(config: list, requests: list,
            label: str = "MTF", verbose: bool = True) -> int:
    """
    Ejecuta MTF sobre *requests* partiendo de *config*.

    Costo de acceso al elemento en posicion k (1-indexada) = k.
    Despues de cada acceso el elemento se mueve al frente.

    Retorna el costo total de accesos.
    """
    lst = list(config)
    total = 0

    if verbose:
        print(f"\n  [ {label} ]")
        print(f"  Config inicial : {lst}")
        print(f"  Solicitudes    : {requests}")
        rule()
        print(f"  {'Config antes':<24}  {'Req':>3}  {'Costo':>5}  Config despues")
        rule()

    for req in requests:
        before = list(lst)
        pos = lst.index(req) + 1
        total += pos
        lst.remove(req)
        lst.insert(0, req)

        if verbose:
            print(f"  {str(before):<24}  {req:>3}  {pos:>5}  {lst}")

    if verbose:
        rule()
        print(f"  Costo total de acceso: {total}\n")

    return total


# ── IMTF -- Improved Move-to-Front (Mohanty & Tripathy) ──────────────────────

def run_imtf(config: list, requests: list,
             label: str = "IMTF", verbose: bool = True) -> int:
    """
    Ejecuta IMTF sobre *requests* partiendo de *config*.

    Despues de acceder al elemento en posicion i, se mueve al frente
    SOLO SI aparece en los proximos i-1 elementos de la secuencia
    (ventana de look-ahead).

    Retorna el costo total de accesos.
    """
    lst = list(config)
    total = 0

    if verbose:
        print(f"\n  [ {label} ]")
        print(f"  Config inicial : {lst}")
        print(f"  Solicitudes    : {requests}")
        rule(wide=True)
        print(f"  {'Config antes':<24}  {'Req':>3}  {'Costo':>5}  {'Mueve?':>7}  Config despues")
        rule(wide=True)

    for idx, req in enumerate(requests):
        before = list(lst)
        pos = lst.index(req) + 1
        total += pos

        window = requests[idx + 1 : idx + pos]
        move = req in window

        if move:
            lst.remove(req)
            lst.insert(0, req)

        if verbose:
            flag = "Si" if move else "No"
            print(f"  {str(before):<24}  {req:>3}  {pos:>5}  {flag:>7}  {lst}")

    if verbose:
        rule(wide=True)
        print(f"  Costo total de acceso: {total}\n")

    return total
