"""
Tarea 1 -- MTF sobre la secuencia 0 1 2 3 4 repetida cuatro veces.
"""

from algorithms import section, run_mtf

CONFIG   = [0, 1, 2, 3, 4]
SEQUENCE = [0,1,2,3,4, 0,1,2,3,4, 0,1,2,3,4, 0,1,2,3,4]


def tarea1() -> int:
    section("TAREA 1 -- MTF | secuencia 0->4 repetida cuatro veces (20 solicitudes)")
    return run_mtf(CONFIG, SEQUENCE, label="TAREA 1")


if __name__ == "__main__":
    tarea1()
