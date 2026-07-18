# draws only from the passed Random instance, never global random or
# wall clock, so a given seed always produces the same output

import random


def weighted_choice(rng: random.Random, weights: list[tuple[str, float]]) -> str:
    values = [v for v, _ in weights]
    cumulative = [w for _, w in weights]
    return rng.choices(values, weights=cumulative, k=1)[0]
