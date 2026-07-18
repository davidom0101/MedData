# single Random(seed) threaded through generators in fixed order
# (demographics -> events -> vitals). reference_date is a param, not
# date.today(), so output depends only on the seed

import random
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from data_generator.adverse_events import generate_adverse_events
from data_generator.demographics import generate_demographics
from data_generator.vitals import generate_vitals
from data_generator.writers import (
    write_adverse_events_json,
    write_demographics_csv,
    write_vitals_xml,
)

# simulated "today", not date.today() (see top of file)
DEFAULT_REFERENCE_DATE = date(2026, 1, 1)

DEFAULT_N_PATIENTS = 200
DEFAULT_EVENTS_PER_PATIENT = 3
DEFAULT_VITALS_PER_PATIENT = 10


@dataclass(frozen=True)
class GenerationSummary:
    seed: int
    reference_date: date
    n_patients: int
    n_events: int
    n_vitals: int
    demographics_path: Path
    adverse_events_path: Path
    vitals_path: Path


def generate_all(
    seed: int,
    output_dir: Path,
    n_patients: int = DEFAULT_N_PATIENTS,
    n_events: int | None = None,
    n_vitals: int | None = None,
    reference_date: date = DEFAULT_REFERENCE_DATE,
) -> GenerationSummary:
    rng = random.Random(seed)

    n_events = n_events if n_events is not None else n_patients * DEFAULT_EVENTS_PER_PATIENT
    n_vitals = n_vitals if n_vitals is not None else n_patients * DEFAULT_VITALS_PER_PATIENT

    patients = generate_demographics(rng, n_patients, reference_date)
    events = generate_adverse_events(rng, patients, n_events, reference_date)
    vitals = generate_vitals(rng, patients, n_vitals, reference_date)

    demographics_path = output_dir / "demographics.csv"
    adverse_events_path = output_dir / "adverse_events.json"
    vitals_path = output_dir / "vitals.xml"

    write_demographics_csv(patients, demographics_path)
    write_adverse_events_json(events, adverse_events_path)
    write_vitals_xml(vitals, vitals_path)

    return GenerationSummary(
        seed=seed,
        reference_date=reference_date,
        n_patients=n_patients,
        n_events=n_events,
        n_vitals=n_vitals,
        demographics_path=demographics_path,
        adverse_events_path=adverse_events_path,
        vitals_path=vitals_path,
    )
