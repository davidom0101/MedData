# source B: adverse event records (JSON)

import random
from datetime import date, datetime, time, timedelta

from data_generator.reference_data import (
    ADVERSE_EVENT_CODES,
    INVESTIGATOR_IDS,
    SEVERITY_LEVELS,
)

# seriousness correlates with severity, not sampled independently
SERIOUSNESS_PROBABILITY_BY_SEVERITY = {
    "mild": 0.05,
    "moderate": 0.20,
    "severe": 0.70,
}


def _random_timestamp_between(rng: random.Random, start: date, end: date) -> datetime:
    span_days = max((end - start).days, 0)
    offset_days = rng.randint(0, span_days)
    event_date = start + timedelta(days=offset_days)
    return datetime.combine(event_date, time(hour=rng.randint(0, 23), minute=rng.randint(0, 59)))


def generate_adverse_events(
    rng: random.Random, patients: list[dict], n_events: int, reference_date: date
) -> list[dict]:
    events = []
    for i in range(1, n_events + 1):
        patient = rng.choice(patients)
        enrollment_date = date.fromisoformat(patient["enrollment_date"])
        severity = rng.choice(SEVERITY_LEVELS)
        is_serious = rng.random() < SERIOUSNESS_PROBABILITY_BY_SEVERITY[severity]

        events.append(
            {
                "event_id": f"AE-EVT-{i:06d}",
                "source_patient_id": patient["source_patient_id"],
                "trial_id": patient["trial_id"],
                "event_timestamp": _random_timestamp_between(
                    rng, enrollment_date, reference_date
                ).isoformat(),
                "adverse_event_code": rng.choice(ADVERSE_EVENT_CODES),
                "severity": severity,
                "seriousness_flag": is_serious,
                "dosage": round(rng.uniform(5.0, 500.0), 1),
                "investigator_id": rng.choice(INVESTIGATOR_IDS),
            }
        )
    return events
