import numpy as np
import pandas as pd
import random

# Generate unique crop IDs
def generate_crop_ids(num_crops):
    crop_ids = []

    for i in range(1, num_crops + 1):
        crop_id = f"CR{i:03d}"
        crop_ids.append(crop_id)

    return crop_ids
# Generate unique crop names
def generate_crop_names(num_crops):
    crop_names = []

    for i in range(1, num_crops + 1):
        crop_name = f"CROP-{i:06d}"
        crop_names.append(crop_name)

    return crop_names

# Generate a list of crop types based on predefined weights
def generate_plant_organs(num_crops):
    plant_organs = np.random.choice(
        [
            "Leaf",
            "Fruit",
            "Root",
            "Grain",
            "Seed",
            "Stem",
            "Tuber",
            "Bulb"
        ],
        size=num_crops,
        p=[0.20, 0.20, 0.15, 0.15, 0.10, 0.08, 0.07, 0.05]
    )

    return plant_organs.tolist()

# Generate a list of cuticle thickness values based on a normal distribution
def generate_cuticle_thickness(num_crops):
    cuticle_thickness = np.random.normal(
        loc=25,
        scale=10,
        size=num_crops
    )

    cuticle_thickness = np.clip(
        cuticle_thickness,
        5,
        60
    )

    return cuticle_thickness.tolist()

#Generate a list of surface roughness values based on predefined probabilities
def generate_surface_roughness(num_crops):
    surface_roughness = np.random.choice(
        ["Low", "Medium", "High"],
        size=num_crops,
        p=[0.30, 0.50, 0.20]
    )

    return surface_roughness.tolist()

# Generate a list of crop growth rate values based on a normal distribution
def generate_crop_growth_rate(num_crops):
    crop_growth_rate = np.random.normal(
        loc=2.5,
        scale=1.0,
        size=num_crops
    )

    crop_growth_rate = np.clip(
        crop_growth_rate,
        0.2,
        6.0
    )

    return crop_growth_rate.tolist()

#Generate a dictionary containing all crop data
def generate_crop_data(num_crops):
    crop_ids = generate_crop_ids(num_crops)
    crop_names = generate_crop_names(num_crops)
    plant_organs = generate_plant_organs(num_crops)
    cuticle_thickness = generate_cuticle_thickness(num_crops)
    surface_roughness = generate_surface_roughness(num_crops)
    crop_growth_rate = generate_crop_growth_rate(num_crops)

    return {
        "crop_id": crop_ids,
        "crop_name": crop_names,
        "plant_organ_harvested": plant_organs,
        "cuticle_thickness": cuticle_thickness,
        "surface_roughness": surface_roughness,
        "crop_growth_rate": crop_growth_rate
    }
crop_data = generate_crop_data(50)

# Assemble the crop data into a pandas DataFrame
def assemble_crop_table(crop_data):
    df = pd.DataFrame(crop_data)
    return df
crop_table = assemble_crop_table(crop_data)

def export_to_excel(crop_table):
    crop_table.to_excel("crop_features.xlsx", index=False)
export_to_excel(crop_table)