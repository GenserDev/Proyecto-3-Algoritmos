"""
Tarea 4 -- Secuencia de 20 solicitudes con MAXIMO costo total en MTF (peor caso).

Estrategia: en cada paso acceder al elemento en la ultima posicion de la lista
actual.  Con n=5 elementos, ese acceso siempre cuesta 5.
El ciclo resultante es [4,3,2,1,0] repetido.
Cota superior absoluta: 20 x 5 = 100.
"""

from algorithms import section, run_mtf

CONFIG = [0, 1, 2, 3, 4]
LENGTH = 20


def build_sequence(config: list = CONFIG, length: int = LENGTH) -> list:
    """Devuelve la secuencia de maximo costo accediendo siempre al ultimo elemento."""
    lst = list(config)
    seq = []
    for _ in range(length):
        last = lst[-1]
        seq.append(last)
        lst.remove(last)
        lst.insert(0, last)
    return seq


def tarea4() -> tuple:
    """Retorna (secuencia, costo_total)."""
    section("TAREA 4 -- Secuencia de 20 solicitudes con MAXIMO costo en MTF (peor caso)")
    seq = build_sequence()
    cost = run_mtf(CONFIG, seq,
                   label="TAREA 4 -- Peor caso (siempre acceder al ultimo elemento)")
    print(f"  Secuencia de peor caso : {seq}")
    print(f"  Costo maximo total     : {cost}")
    print()
    print("  Justificacion:")
    print("  Con 5 elementos el maximo costo por acceso es 5.")
    print("  El ciclo [4,3,2,1,0] mantiene el elemento buscado siempre en pos 5.")
    print("  Cota superior absoluta = 20 x 5 = 100 -> alcanzada.")
    return seq, cost


if __name__ == "__main__":
    tarea4()
