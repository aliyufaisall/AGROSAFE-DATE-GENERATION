import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate unique crop IDs
def generate_application_ids(num_applications):
    application_ids = []

    for i in range(1, num_applications + 1):
        application_id = f"A{i:05d}"
        application_ids.append(application_id)

    return application_ids

# Generate unique chemical IDs matching application IDs
def generate_chemical_ids(num_applications):
    chemical_ids = np.random.choice(
        [f"C{i:03d}" for i in range(1, 201)],
        size=num_applications
    )

    return chemical_ids.tolist()

# Generate unique crop IDs matching application IDs
def generate_crop_ids(num_applications):
    crop_ids = np.random.choice(
        [f"CR{i:03d}" for i in range(1, 51)],
        size=num_applications
    )

    return crop_ids.tolist()

# Generate a list of application methods based on predefined weights
def generate_application_rate(num_applications):
    application_rate = np.random.lognormal(
        mean=1.5,
        sigma=0.8,
        size=num_applications
    )

    application_rate = np.clip(
        application_rate,
        0.1,
        20.0
    )

    return application_rate.tolist()

# Generate a list of the number of applications based on predefined probabilities
def generate_number_of_applications(num_applications):
    number_of_applications = np.random.choice(
        [1, 2, 3, 4, 5],
        size=num_applications,
        p=[0.35, 0.30, 0.20, 0.10, 0.05]
    )

    return number_of_applications.tolist()

# Generate a list of phi values based on a normal distribution
def generate_phi(num_applications):
    phi = np.random.normal(
        loc=21,
        scale=10,
        size=num_applications
    )

    phi = np.clip(phi, 0, 60)

    return phi.round().astype(int).tolist()

# Generate a list of application methods based on predefined weights
def generate_application_method(num_applications):
    application_method = np.random.choice(
        [
            "Foliar Spray",
            "Soil Drench",
            "Seed Treatment",
            "Granular Application",
            "Fertigation"
        ],
        size=num_applications,
        p=[0.50, 0.20, 0.15, 0.10, 0.05]
    )

    return application_method.tolist()

# Generate a list of application timings based on predefined weights
def generate_application_dates(num_applications):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)

    days_between = (end_date - start_date).days

    application_dates = []

    for _ in range(num_applications):
        random_days = random.randint(0, days_between)
        application_date = start_date + timedelta(days=random_days)
        application_dates.append(application_date.strftime("%Y-%m-%d"))

    return application_dates

# Generate a list of days since last application based on a normal distribution
def generate_days_since_last_application(num_applications):
    days_since_last_application = np.random.normal(
        loc=15,
        scale=8,
        size=num_applications
    )

    days_since_last_application = np.clip(
        days_since_last_application,
        0,
        60
    )

    return days_since_last_application.round().astype(int).tolist()


def generate_application_data(num_applications):
    application_ids = generate_application_ids(num_applications)
    chemical_ids = generate_chemical_ids(num_applications)
    crop_ids = generate_crop_ids(num_applications)
    application_rate = generate_application_rate(num_applications)
    number_of_applications = generate_number_of_applications(num_applications)
    phi = generate_phi(num_applications)
    application_method = generate_application_method(num_applications)
    application_date = generate_application_dates(num_applications)
    days_since_last_application = generate_days_since_last_application(num_applications)

    return {
        "application_id": application_ids,
        "chemical_id": chemical_ids,
        "crop_id": crop_ids,
        "application_rate": application_rate,
        "number_of_applications": number_of_applications,
        "phi": phi,
        "application_method": application_method,
        "application_date": application_date,
        "days_since_last_application": days_since_last_application
    }
application_data = generate_application_data(25000)

def assemble_application_table(application_data):
    df = pd.DataFrame(application_data)
    return df
application_table = assemble_application_table(application_data)

def export_application_table(application_table):
    application_table.to_excel("application_features.xlsx", index=False)
export_application_table(application_table)