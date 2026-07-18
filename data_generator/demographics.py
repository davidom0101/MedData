# source A: patient demographics and enrollment records (CSV)

import random
from datetime import date, timedelta

from data_generator.reference_data import (
    CONSENT_STATUSES,
    COUNTRY_WEIGHTS,
    SEX_VALUES,
    SITES,
    TRIALS,
)
from data_generator.sampling import weighted_choice

# mostly consented, some withdrawn or pending, mirrors real attrition
CONSENT_WEIGHTS = [
    (CONSENT_STATUSES[0], 0.85),  # consented
    (CONSENT_STATUSES[1], 0.10),  # withdrawn
    (CONSENT_STATUSES[2], 0.05),  # pending
]

MAX_ENROLLMENT_LOOKBACK_DAYS = 540


def generate_demographics(rng: random.Random, n_patients: int, reference_date: date) -> list[dict]:
    patients = []
    for i in range(1, n_patients + 1):
        site = rng.choice(SITES)
        trial = rng.choice(TRIALS)
        enrollment_date = reference_date - timedelta(
            days=rng.randint(1, MAX_ENROLLMENT_LOOKBACK_DAYS)
        )

        patients.append(
            {
                "source_patient_id": f"PT-{i:05d}",
                "trial_id": trial["trial_id"],
                "site_id": site["site_id"],
                "sex": rng.choice(SEX_VALUES),
                "age": rng.randint(18, 85),
                "enrollment_date": enrollment_date.isoformat(),
                "country": weighted_choice(rng, COUNTRY_WEIGHTS),
                "consent_status": weighted_choice(rng, CONSENT_WEIGHTS),
            }
        )
    return patients
