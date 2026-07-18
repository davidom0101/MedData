# reproducibility is the point, same seed -> same
# output, different seed -> different output

import subprocess
import sys
from pathlib import Path

from data_generator.generate import generate_all


def test_same_seed_produces_identical_files(tmp_path):
    out_a = tmp_path / "run_a"
    out_b = tmp_path / "run_b"

    generate_all(seed=42, output_dir=out_a, n_patients=50)
    generate_all(seed=42, output_dir=out_b, n_patients=50)

    for filename in ["demographics.csv", "adverse_events.json", "vitals.xml"]:
        assert (out_a / filename).read_bytes() == (out_b / filename).read_bytes()


def test_different_seed_produces_different_output(tmp_path):
    out_a = tmp_path / "seed_1"
    out_b = tmp_path / "seed_2"

    generate_all(seed=1, output_dir=out_a, n_patients=50)
    generate_all(seed=2, output_dir=out_b, n_patients=50)

    assert (out_a / "demographics.csv").read_bytes() != (out_b / "demographics.csv").read_bytes()


def test_output_record_counts_match_request(tmp_path):
    summary = generate_all(seed=7, output_dir=tmp_path, n_patients=20, n_events=15, n_vitals=30)

    demographics_rows = summary.demographics_path.read_text().strip().splitlines()
    assert len(demographics_rows) - 1 == 20  # minus header

    assert summary.n_events == 15
    assert summary.n_vitals == 30


def test_cli_entrypoint_is_reproducible(tmp_path):
    # CLI check: two process runs, same seed, identical bytes
    out_a = tmp_path / "cli_a"
    out_b = tmp_path / "cli_b"
    repo_root = Path(__file__).resolve().parent.parent

    for out_dir in (out_a, out_b):
        subprocess.run(
            [
                sys.executable,
                "-m",
                "data_generator",
                "--seed",
                "123",
                "--patients",
                "10",
                "--output-dir",
                str(out_dir),
            ],
            cwd=repo_root,
            check=True,
            capture_output=True,
        )

    for filename in ["demographics.csv", "adverse_events.json", "vitals.xml"]:
        assert (out_a / filename).read_bytes() == (out_b / filename).read_bytes()
