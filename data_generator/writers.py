# writers never touch the clock, records in = same bytes out

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def write_demographics_csv(patients: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(patients[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)


def write_adverse_events_json(events: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)
        f.write("\n")


def write_vitals_xml(readings: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    root = ET.Element("vitals_readings")
    for reading in readings:
        record = ET.SubElement(root, "reading")
        for field, value in reading.items():
            element = ET.SubElement(record, field)
            element.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)
