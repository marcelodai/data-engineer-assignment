from sqlalchemy import func
from db.models import SquirrelData, ParkData, OtherAnimalSightings, Activities

def run_queries(session):
    # 1.How many squirrels are there in each Park?

    squirrels_per_park = session.query(SquirrelData.park_id, ParkData.park_name, func.count(SquirrelData.squirrel_id)).join(ParkData).group_by(SquirrelData.park_id).all()

    print("\n\n1. How many squirrels are there in each Park?\n")
    for park_id, park_name, count in squirrels_per_park:
        print(f"Park: {park_name}, Park ID: {park_id}, Squirrels: {count}")

    # 2. How many squirrels are there in each Borough?

    squirrels_per_borough = session.query(ParkData.area_name, func.count(SquirrelData.squirrel_id)).join(SquirrelData, SquirrelData.park_id == ParkData.park_id).group_by(ParkData.area_name).all()

    print("\n\n2. How many squirrels are there in each Borough?\n")
    for borough, count in squirrels_per_borough:
        print(f"Borough: {borough}, Squirrels: {count}")

    # 3. A count of "Other Animal Sightings" by Park.

    animal_count_by_park = session.query(
        OtherAnimalSightings.park_id, ParkData.park_name,
        func.count(OtherAnimalSightings.animal).label("animal_count")
    ).join(ParkData, ParkData.park_id == OtherAnimalSightings.park_id).group_by(OtherAnimalSightings.park_id).all()

    print("\n\n3. A count of \"Other Animal Sightings\" by Park.\n")
    for _, park_name, animal_count in animal_count_by_park:
        print(f"Park: {park_name}, Animal Count: {animal_count}")



    # 4. What is the most common activity for Squirrels? (e.g. eating, running, etc..)
    most_common_activity = session.query(
        Activities.activity,
        func.count(Activities.activity).label("activity_count")
    ).group_by(Activities.activity).order_by(func.count(Activities.activity).desc()).first()

    print(f"\n\n4. What is the most common activity for Squirrels? (e.g. eating, running, etc..)\nThe most common activity for squirrels is {most_common_activity.activity}")

    # 5. A count of all Primary Fur Colors by Park.

    # Query to count all primary fur colors by park
    primary_fur_color_count_by_park = session.query(
        SquirrelData.park_id,
        ParkData.park_name,
        SquirrelData.primary_fur_color,
        func.count(SquirrelData.primary_fur_color).label("fur_color_count")
    ).join(ParkData, SquirrelData.park_id == ParkData.park_id).group_by(
        SquirrelData.park_id,
        ParkData.park_id,
        SquirrelData.primary_fur_color
    ).all()

    print("\n\n5. A count of all Primary Fur Colors by Park.\n")
    for _, park_name, fur_color, count in primary_fur_color_count_by_park:
        print(f"Park Name: {park_name}, Fur Color: {fur_color}, Count: {count}")
