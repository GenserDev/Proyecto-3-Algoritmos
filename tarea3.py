"""
Tarea 3 -- Secuencia de 20 solicitudes con MINIMO costo total en MTF.

Estrategia: solicitar siempre el elemento en la posicion 1 (config[0]).
Cada acceso cuesta 1; ningun acceso puede costar menos que 1.
Cota inferior absoluta: 20 x 1 = 20.
"""

from algorithms import section, run_mtf

CONFIG = [0, 1, 2, 3, 4]
LENGTH = 20


def build_sequence(config: list = CONFIG, length: int = LENGTH) -> list:
    """Devuelve la secuencia de minimo costo: el elemento del frente repetido."""
    return [config[0]] * length


def tarea3() -> tuple:
    """Retorna (secuencia, costo_total)."""
    section("TAREA 3 -- Secuencia de 20 solicitudes con MINIMO costo en MTF")
    seq = build_sequence()
    cost = run_mtf(CONFIG, seq,
                   label=f"TAREA 3 -- Minimo costo (siempre solicitar '{CONFIG[0]}')")
    print(f"  Secuencia de minimo costo : {seq}")
    print(f"  Costo minimo total        : {cost}")
    print()
    print("  Justificacion:")
    print(f"  '{CONFIG[0]}' ocupa la posicion 1 desde el inicio -> costo 1 en cada acceso.")
    print("  Ningun acceso puede costar < 1, luego 20 x 1 = 20 es la cota inferior.")
    return seq, cost


if __name__ == "__main__":
    tarea3()
