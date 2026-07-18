# source C: repeated daily vitals measurements (XML)

import random
from datetime import date, datetime, time, timedelta

# ranges wide enough for abnormal but plausible readings, gives the
# Silver layer range checks (spec section 7) something to reject
SYSTOLIC_BP_RANGE = (90, 180)
DIASTOLIC_BP_RANGE = (55, 110)
PULSE_RANGE = (45, 115)
TEMPERATURE_RANGE_C = (35.5, 39.5)


def _random_timestamp_between(rng: random.Random, start: date, end: date) -> datetime:
    span_days = max((end - start).days, 0)
    offset_days = rng.randint(0, span_days)
    capture_date = start + timedelta(days=offset_days)
    return datetime.combine(capture_date, time(hour=rng.randint(0, 23), minute=rng.randint(0, 59)))


def generate_vitals(
    rng: random.Random, patients: list[dict], n_readings: int, reference_date: date
) -> list[dict]:
    readings = []
    for i in range(1, n_readings + 1):
        patient = rng.choice(patients)
        enrollment_date = date.fromisoformat(patient["enrollment_date"])

        readings.append(
            {
                "reading_id": f"VIT-{i:06d}",
                "source_patient_id": patient["source_patient_id"],
                "trial_id": patient["trial_id"],
                "site_id": patient["site_id"],
                "capture_timestamp": _random_timestamp_between(
                    rng, enrollment_date, reference_date
                ).isoformat(),
                "systolic_bp": rng.randint(*SYSTOLIC_BP_RANGE),
                "diastolic_bp": rng.randint(*DIASTOLIC_BP_RANGE),
                "pulse": rng.randint(*PULSE_RANGE),
                "temperature": round(rng.uniform(*TEMPERATURE_RANGE_C), 1),
            }
        )
    return readings
