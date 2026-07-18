import argparse
from datetime import date
from pathlib import Path

from data_generator.generate import (
    DEFAULT_N_PATIENTS,
    DEFAULT_REFERENCE_DATE,
    generate_all,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="data_generator",
        description="Generate seeded synthetic clinical trial source files",
    )
    parser.add_argument(
        "--seed", type=int, required=True, help="RNG seed; same seed -> identical output"
    )
    parser.add_argument(
        "--patients", type=int, default=DEFAULT_N_PATIENTS, help="number of patients to generate"
    )
    parser.add_argument(
        "--events",
        type=int,
        default=None,
        help="number of adverse event records (default: patients * 3)",
    )
    parser.add_argument(
        "--vitals",
        type=int,
        default=None,
        help="number of vitals readings (default: patients * 10)",
    )
    parser.add_argument(
        "--reference-date",
        type=date.fromisoformat,
        default=DEFAULT_REFERENCE_DATE,
        help="simulated 'today' data is generated relative to, YYYY-MM-DD (default: %(default)s)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/landing"),
        help="directory to write demographics.csv / adverse_events.json / vitals.xml into",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    summary = generate_all(
        seed=args.seed,
        output_dir=args.output_dir,
        n_patients=args.patients,
        n_events=args.events,
        n_vitals=args.vitals,
        reference_date=args.reference_date,
    )
    print(f"seed={summary.seed} reference_date={summary.reference_date}")
    print(f"  demographics:   {summary.n_patients:>6} patients -> {summary.demographics_path}")
    print(f"  adverse_events: {summary.n_events:>6} events   -> {summary.adverse_events_path}")
    print(f"  vitals:         {summary.n_vitals:>6} readings -> {summary.vitals_path}")


if __name__ == "__main__":
    main()
