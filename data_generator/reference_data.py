# static lookup data (sites, trials, event codes), kept separate from
# generation logic so the "world" can be edited on its own

SITES = [
    {
        "site_id": "SITE-001",
        "site_name": "Dublin City Hospital",
        "city": "Dublin",
        "county": "Dublin",
    },
    {
        "site_id": "SITE-002",
        "site_name": "Cork University Clinic",
        "city": "Cork",
        "county": "Cork",
    },
    {
        "site_id": "SITE-003",
        "site_name": "Galway Bay Medical Centre",
        "city": "Galway",
        "county": "Galway",
    },
    {
        "site_id": "SITE-004",
        "site_name": "Dublin North Research Unit",
        "city": "Dublin",
        "county": "Dublin",
    },
]

TRIALS = [
    {
        "trial_id": "TRIAL-001",
        "phase": "II",
        "therapeutic_area": "Oncology",
        "sponsor_type": "Pharma",
    },
    {
        "trial_id": "TRIAL-002",
        "phase": "III",
        "therapeutic_area": "Cardiology",
        "sponsor_type": "CRO",
    },
    {
        "trial_id": "TRIAL-003",
        "phase": "I",
        "therapeutic_area": "Immunology",
        "sponsor_type": "Pharma",
    },
]

# severity/seriousness sampled separately in adverse_events.py, these
# codes just give each event a plausible label
ADVERSE_EVENT_CODES = [
    "AE-001",  # headache
    "AE-002",  # nausea
    "AE-003",  # fatigue
    "AE-004",  # dizziness
    "AE-005",  # rash
    "AE-006",  # elevated liver enzymes
    "AE-007",  # neutropenia
    "AE-008",  # hypertension
    "AE-009",  # anaphylaxis
    "AE-010",  # cardiac arrhythmia
]

SEVERITY_LEVELS = ["mild", "moderate", "severe"]
SEX_VALUES = ["male", "female"]
CONSENT_STATUSES = ["consented", "withdrawn", "pending"]

# sites are Irish, weight country toward Ireland
COUNTRY_WEIGHTS = [("Ireland", 0.92), ("United Kingdom", 0.05), ("France", 0.03)]

INVESTIGATOR_IDS = [f"INV-{i:03d}" for i in range(1, 13)]
