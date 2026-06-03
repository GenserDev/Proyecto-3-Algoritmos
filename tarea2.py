from algorithms import section, run_mtf

CONFIG   = [0, 1, 2, 3, 4]
SEQUENCE = [4,3,2,1,0, 1,2,3,4,3, 2,1,0,1,2, 3,4]


def tarea2() -> int:
    section("TAREA 2 -- MTF | secuencia 4 3 2 1 0 1 2 3 4 3 2 1 0 1 2 3 4 (17 elem)")
    return run_mtf(CONFIG, SEQUENCE, label="TAREA 2")


if __name__ == "__main__":
    tarea2()
