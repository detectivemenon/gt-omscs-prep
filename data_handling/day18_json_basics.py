# Day 18 – JSON Basics: load, validate, transform, save
# Save as: algorithmic-thinking/data_handling/day18_json_basics.py
# Run this file directly for tiny smoke tests.

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------
# Helpers: paths & tiny sample data
# ---------------------------------------------------------------------
DATA_DIR = Path(__file__).parent / "samples"
DATA_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_JSON_PATH = DATA_DIR / "users_sample.json"

SAMPLE_USERS = [
    {"id": 1, "name": "Alice",  "age": 31, "skills": ["python", "sql"], "active": True},
    {"id": 2, "name": "Bob",    "age": 27, "skills": ["excel"],         "active": False},
    {"id": 3, "name": "Cara",   "age": 35, "skills": ["python"],        "active": True},
    {"id": 4, "name": "Daniel", "age": 29, "skills": [],                "active": True},
]

# ---------------------------------------------------------------------
# Part A: File I/O utilities (pure JSON)
# ---------------------------------------------------------------------
import json

student = {
    "name": "Santosh",
    "age": 34,
    "courses": ["AI", "ML", "KBAI"],
    "active": True
}

json_string = json.dumps(student, indent = 4)
print("JSON output:\n", json_string)

python_obj = json.loads(json_string)
print("\nBack to Python:\n", python_obj)



with open("student_data.json", "w") as f:
    json.dump(student, f, indent=4)

print("✅ JSON written to student_data.json")

with open("student_data.json", "r") as f:
    loaded_data = json.load(f)

print("📄 JSON read from file:\n", loaded_data)
import os
print("CWD:", os.getcwd())

def save_json(data: Any, path: Path, *, pretty: bool = True) -> None:
    """
    Save Python data to a JSON file.
    pretty=True -> indent=2, sorted keys for readability.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        if pretty:
            json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)
        else:
            json.dump(data, f, separators=(",", ":"), ensure_ascii=False)

def load_json(path: Path) -> Any:
    """
    Load JSON file into Python data (dict/list/etc).
    """
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)




# ---------------------------------------------------------------------
# Part B: Validation & safe access patterns
# ---------------------------------------------------------------------
def validate_user(record: Dict[str, Any]) -> bool:
    """
    Minimal schema check for a 'user' record.
    Required: id(int), name(str), age(int), skills(list), active(bool).
    """
    return (
        isinstance(record, dict)
        and isinstance(record.get("id"), int)
        and isinstance(record.get("name"), str)
        and isinstance(record.get("age"), int)
        and isinstance(record.get("skills"), list)
        and isinstance(record.get("active"), bool)
    )

def filter_active_python_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Return users who are active and have 'python' in skills.
    """
    result = []
    for u in users:
        if not validate_user(u):
            # skip invalid records silently for now (we can log in Day 19)
            continue
        skills = u.get("skills", [])
        if u.get("active") and isinstance(skills, list) and "python" in skills:
            result.append(u)
    return result

def add_skill(users: List[Dict[str, Any]], name: str, skill: str) -> None:
    """
    In-place: add 'skill' to the user with matching name (case-insensitive),
    avoiding duplicates.
    """
    for u in users:
        if isinstance(u.get("name"), str) and u["name"].lower() == name.lower():
            if "skills" not in u or not isinstance(u["skills"], list):
                u["skills"] = []
            if skill not in u["skills"]:
                u["skills"].append(skill)

def safe_load_json(filepath: str) -> dict:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}

    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' contains invalid JSON.")
        return {}


# ---------------------------------------------------------------------
# Part C: Transform examples
# ---------------------------------------------------------------------
def to_id_name_map(users: List[Dict[str, Any]]) -> Dict[int, str]:
    """Convert list of users into {id: name} map."""
    return {u["id"]: u["name"] for u in users if "id" in u and "name" in u}


def extract_contacts(users: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Extract only names and emails for contact export."""
    return [{"name": u.get("name", "N/A"), "email": u.get("email", "N/A")} for u in users]

#--------------------------------------------------------------------
# Part D: Real-world example: Loading a JSON file and transforming it
# ---------------------------------------------------------------------
import json
from pathlib import Path
from typing import List, Dict, Any

def safe_load_json(filepath: Path):
    """Safely load JSON from file and return Python object."""
    try:
        with filepath.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file - {filepath}")
        return []

def to_id_name_map(users: List[Dict[str, Any]]) -> Dict[int, str]:
    """Convert list of users into {id: name} map."""
    return {u["id"]: u["name"] for u in users if "id" in u and "name" in u}

def extract_contacts(users: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Extract only names and emails for contact export."""
    return [{"name": u.get("name", "N/A"), "email": u.get("email", "N/A")} for u in users]




# ---------------------------------------------------------------------
# Smoke tests
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("[Day 18] JSON Basics — smoke tests")
    # Example data you can replace with safe_load_json("users.json")
    users = [
        {"id": 101, "name": "Santosh", "email": "santosh@example.com"},
        {"id": 102, "name": "Saritha", "email": "saritha@example.com"},
    ]

    id_map = to_id_name_map(users)
    contacts = extract_contacts(users)

    print("ID → Name map:", id_map)
    print("Contacts:", contacts)
    # 1) Save sample
    save_json(SAMPLE_USERS, SAMPLE_JSON_PATH)
    print(f"Saved sample to: {SAMPLE_JSON_PATH}")

    # 2) Load sample
    users = load_json(SAMPLE_JSON_PATH)
    print(f"Loaded {len(users)} users")

    # 3) Transform/validate
    # print("Average age:", average_age(users))
    # print("ID->Name map:", to_id_name_map(users))

    # 4) Filter & mutate
    py_actives = filter_active_python_users(users)
    print("Active Python users:", [u['name'] for u in py_actives])

    add_skill(users, "Bob", "python")      # teach Bob Python
    add_skill(users, "Daniel", "git")      # add a new skill to Daniel
    print("Bob skills after add:", next(u["skills"] for u in users if u["name"]=="Bob"))

    # 5) Save transformed
    out_path = DATA_DIR / "users_transformed.json"
    save_json(users, out_path)
    print(f"Wrote transformed users -> {out_path}")

    # 6) Real world example
    # 🔹 Absolute path to your JSON file
    path = Path("/Users/macmenongt/Documents/gt-omscs-prep/data_handling/users.json")

    users = safe_load_json(path)
    print("✅ JSON file loaded successfully:")
    print(users)
    path = Path("users.json")
    users = safe_load_json(path)  # Step 1: Read JSON from file → Python list

    print("Loaded users:", users)

    id_map = to_id_name_map(users)  # Step 2: Create {id: name} map
    contacts = extract_contacts(users)  # Step 3: Extract name-email pairs

    print("\nID → Name map:")
    print(id_map)

    print("\nContacts list:")
    print(contacts)