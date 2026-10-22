
"""Parking lot management demonstration for static code analysis."""

import hashlib
import secrets

parking_slots = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

parking_state = {"total_collections": 0.0}


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle in an available slot and record the entry."""
    if entry_logs is None:
        entry_logs = []

    if slot_id not in parking_slots or parking_slots[slot_id]["is_occupied"]:
        return False

    parking_slots[slot_id]["plate"] = plate_no
    parking_slots[slot_id]["hours"] = hours_booked
    parking_slots[slot_id]["is_occupied"] = True
    parking_state["total_collections"] += (
        parking_slots[slot_id]["rate"] * hours_booked
    )

    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours with total charge calculated"
    )
    return True


def release_slot(slot_id):
    """Release an occupied parking slot."""
    if slot_id not in parking_slots:
        return False

    parking_slots[slot_id]["is_occupied"] = False
    parking_slots[slot_id]["plate"] = ""
    parking_slots[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a known parking slot is available."""
    slot = parking_slots.get(slot_id)
    if slot is None:
        return False
    return not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.50):
    """Calculate the parking fee using a surge multiplier."""
    if slot_id not in parking_slots:
        raise ValueError(f"Unknown parking slot: {slot_id}")

    if surge_multiplier < 0:
        raise ValueError("Surge multiplier cannot be negative")

    base_rate = parking_slots[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Generate a SHA-256 hash of a vehicle registration number."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a cryptographically secure four-digit ticket PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_parking_manifest(filename="parking_manifest.txt"):
    """Write the current parking slots to a manifest file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(parking_slots))

    print(f"Parking manifest exported to: {filename}")


def get_available_summary(slots):
    """Return the number of unoccupied parking slots."""
    return sum(
        1 for details in slots.values()
        if not details["is_occupied"]
    )


def main():
    """Demonstrate the parking lot system."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())

    export_parking_manifest()
    print("Vacant slots:", get_available_summary(parking_slots))


if __name__ == "__main__":
    main()
