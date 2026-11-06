
"""
PYTHON GARBAGE COLLECTION
Experiments with the gc module

"""

import gc
import sys
import time
import weakref
import tracemalloc


def section(title):
    print(f"\n{'=' * 8} {title} {'=' * 8}")


class Node:
    """A simple object used for garbage collection experiments."""

    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"   [__del__] {self.name} destroyed")


# EXPERIMENT 1: Reference Counting

def exp1_reference_counting():
    section("1. Reference counting: instant cleanup")

    a = Node("A")
    print("refcount of A:", sys.getrefcount(a))

    b = a
    print("after b = a, refcount:", sys.getrefcount(a))

    del a
    print("after del a, refcount:", sys.getrefcount(b))

    print("deleting the last name...")
    del b
    print("(destroyed immediately, no gc needed)")


# EXPERIMENT 2: Reference Cycles

def exp2_cycle_and_manual_collect():
    section("2. Reference cycle and manual collection")

    gc.collect()
    gc.disable()

    print("gc enabled?", gc.isenabled())

    x = Node("X")
    y = Node("Y")

    x.other = y
    y.other = x

    del x, y

    print("deleted both names. Objects are still in memory.")

    found = gc.collect()

    print("gc.collect() returned", found)

    gc.enable()


# EXPERIMENT 3: Thresholds and Statistics

def exp3_thresholds_counts_stats():
    section("3. Thresholds, counts and statistics")

    print("get_threshold():", gc.get_threshold())
    print("get_count():", gc.get_count())

    stats = gc.get_stats()

    print("get_stats():")
    for i, s in enumerate(stats):
        print(
            "Generation", i,
            "collections =", s["collections"],
            "collected =", s["collected"],
            "uncollectable =", s["uncollectable"]
        )


# EXPERIMENT 4: Automatic Garbage Collection

def exp4_automatic_trigger():
    section("4. Automatic garbage collection")

    events = []

    def watcher(phase, info):
        if phase == "stop":
            events.append(
                (info["generation"], info["collected"])
            )

    gc.callbacks.append(watcher)

    old = gc.get_threshold()

    try:
        gc.collect()
        gc.set_threshold(50, 5, 5)

        events.clear()

        for _ in range(300):
            a, b = [], []
            a.append(b)
            b.append(a)

        gc.collect()

        print("Automatic collections:", len(events))
        print("First few runs:", events[:5])

    finally:
        gc.set_threshold(*old)
        gc.callbacks.remove(watcher)


# EXPERIMENT 5: Generations

def exp5_generations():
    section("5. Generations of garbage collection")

    gc.collect()

    keeper = [Node("K")]
    keeper[0].other = keeper

    print(
        "Before collect(0):",
        [len(gc.get_objects(g)) for g in range(3)]
    )

    gc.collect(0)

    print(
        "After collect(0):",
        [len(gc.get_objects(g)) for g in range(3)]
    )

    gc.collect(1)

    print(
        "After collect(1):",
        [len(gc.get_objects(g)) for g in range(3)]
    )

    print("Surviving objects move to older generations.")

    keeper[0].other = None
    del keeper


# EXPERIMENT 6: Memory Measurement

def exp6_memory_effect():
    section("6. Memory effect of garbage collection")

    gc.collect()
    gc.disable()

    tracemalloc.start()

    try:
        base = tracemalloc.get_traced_memory()[0]

        for _ in range(20000):
            a, b = {}, {}
            a["b"] = b
            b["a"] = a

        del a, b

        leaked = tracemalloc.get_traced_memory()[0] - base

        n = gc.collect()

        after = tracemalloc.get_traced_memory()[0] - base

        print(
            "Memory held by cycles:",
            round(leaked / 1024, 1), "KiB"
        )

        print("Objects collected:", n)

        print(
            "Memory after collection:",
            round(after / 1024, 1), "KiB"
        )

    finally:
        tracemalloc.stop()
        gc.enable()


# EXPERIMENT 7: DEBUG_SAVEALL

def exp7_debug_saveall():
    section("7. DEBUG_SAVEALL")

    gc.collect()

    gc.set_debug(gc.DEBUG_SAVEALL)

    try:
        p, q = [1], [2]

        p.append(q)
        q.append(p)

        del p, q

        gc.collect()

        print("Objects stored in gc.garbage:")
        print(gc.garbage)

    finally:
        gc.set_debug(0)
        gc.garbage.clear()
        gc.collect()


# EXPERIMENT 8: Object Tracking and Weak References

def exp8_tracking_and_weakref():
    section("8. Object tracking and weak references")

    samples = [
        ("Integer", 5),
        ("String", "hi"),
        ("List", [1]),
        ("Empty dictionary", {}),
        ("Dictionary with list", {"k": [1]}),
        ("Tuple of integers", (1, 2)),
        ("Node object", Node("T"))
    ]

    for label, obj in samples:
        print(
            label,
            "tracked by gc?",
            gc.is_tracked(obj)
        )

    n = Node("W")
    ref = weakref.ref(n)

    print("Weak reference alive?", ref() is not None)

    del n

    print("After deletion, weak reference alive?", ref() is not None)


# EXPERIMENT 9: Freeze

def exp9_freeze():
    section("9. Garbage collection freeze")

    gc.collect()

    print("Frozen before:", gc.get_freeze_count())

    gc.freeze()

    print("Frozen after:", gc.get_freeze_count())

    gc.unfreeze()

    print("After unfreeze:", gc.get_freeze_count())


# EXPERIMENT 10: Performance Comparison

def exp10_timing():
    section("10. Garbage collection performance")

    def work():
        data = []

        for i in range(400000):
            data.append([i])

        return len(data)

    results = {}

    for label, enabled in [
        ("GC enabled", True),
        ("GC disabled", False)
    ]:
        gc.collect()

        if enabled:
            gc.enable()
        else:
            gc.disable()

        start = time.perf_counter()

        work()

        end = time.perf_counter()

        results[label] = (end - start) * 1000

        gc.enable()

        print(label, ":", round(results[label], 1), "ms")


# MAIN PROGRAM

if __name__ == "__main__":

    print("Python Version:", sys.version.split()[0])

    exp1_reference_counting()
    exp2_cycle_and_manual_collect()
    exp3_thresholds_counts_stats()
    exp4_automatic_trigger()
    exp5_generations()
    exp6_memory_effect()
    exp7_debug_saveall()
    exp8_tracking_and_weakref()
    exp9_freeze()
    exp10_timing()

    print("\nAll 10 experiments completed successfully.")
