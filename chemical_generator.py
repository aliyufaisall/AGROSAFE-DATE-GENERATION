import random
import numpy as np
import pandas as pd

# Generate a list of active ingredients with unique identifiers
def generate_active_ingredients(num_chemicals):
    active_ingredients = []

    for i in range(1, num_chemicals + 1):
        active_ingredients.append(f"CHEM-{i:06}")

    return active_ingredients

CHEMICAL_CLASSES = [
    ("Herbicide", 35),
    ("Insecticide", 35),
    ("Fungicide", 20),
    ("Nematicide", 5),
    ("Acaricide", 3),
    ("Rodenticide", 2)
]
# Generate a list of chemical classes based on predefined weights
def generate_chemical_classes(num_chemicals):
    classes = random.choices(
        population=[c[0] for c in CHEMICAL_CLASSES],
        weights=[c[1] for c in CHEMICAL_CLASSES],
        k=num_chemicals
    )

    return classes
# Generate a list of logP values based on a normal distribution
def generate_logp(num_chemicals):
    logp_values = np.random.normal(
        loc=3,
        scale=1.5,
        size=num_chemicals
    )

    logp_values = np.clip(logp_values, -2, 8)

    return logp_values.tolist()
# Generate a list of water solubility values based on a log-normal distribution
def generate_water_solubility(num_chemicals):
    water_solubility = np.random.lognormal(
        mean=6,
        sigma=2,
        size=num_chemicals
    )

    water_solubility = np.clip(
        water_solubility,
        0.001,
        1_000_000
    )

    return water_solubility.tolist()
# Generate a list of vapor pressure values based on a log-normal distribution
def generate_vapor_pressure(num_chemicals):
    vapor_pressure = np.random.lognormal(
        mean=-2,
        sigma=3,
        size=num_chemicals
    )

    vapor_pressure = np.clip(
        vapor_pressure,
        0.000001,
        1000
    )

    return vapor_pressure.tolist()
# Generate a list of Henry's constant values based on a log-normal distribution
def generate_henrys_constant(num_chemicals):
    henrys_constant = np.random.lognormal(
        mean=-5,
        sigma=3,
        size=num_chemicals
    )

    henrys_constant = np.clip(
        henrys_constant,
        0.000000001,
        100
    )

    return henrys_constant.tolist()
# Generate a list of Koc values based on a log-normal distribution
def generate_koc(num_chemicals):
    koc = np.random.lognormal(
        mean=5,
        sigma=2,
        size=num_chemicals
    )

    koc = np.clip(
        koc,
        1,
        1_000_000
    )

    return koc.tolist()
# Generate a list of molecular weight values based on a normal distribution
def generate_molecular_weight(num_chemicals):
    molecular_weight = np.random.normal(
        loc=300,
        scale=100,
        size=num_chemicals
    )

    molecular_weight = np.clip(
        molecular_weight,
        50,
        1000
    )

    return molecular_weight.tolist()
# Generate a list of pKa values based on a normal distribution
def generate_pka(num_chemicals):
    pka = np.random.normal(
        loc=6,
        scale=2,
        size=num_chemicals
    )

    pka = np.clip(
        pka,
        0,
        14
    )

    return pka.tolist()
# Generate a list of hydrolysis half-life values based on a log-normal distribution
def generate_hydrolysis_half_life(num_chemicals):
    hydrolysis_half_life = np.random.lognormal(
        mean=3,
        sigma=2,
        size=num_chemicals
    )

    hydrolysis_half_life = np.clip(
        hydrolysis_half_life,
        0.01,
        10000
    )

    return hydrolysis_half_life.tolist()
# Generate a list of photolysis half-life values based on a log-normal distribution
def generate_photolysis_half_life(num_chemicals):
    photolysis_half_life = np.random.lognormal(
        mean=2,
        sigma=2,
        size=num_chemicals
    )

    photolysis_half_life = np.clip(
        photolysis_half_life,
        0.01,
        10000
    )

    return photolysis_half_life.tolist()

# Generate a list of soil half-life values based on a log-normal distribution
def generate_soil_half_life(num_chemicals):
    soil_half_life = np.random.lognormal(
        mean=4,
        sigma=2,
        size=num_chemicals
    )

    soil_half_life = np.clip(
        soil_half_life,
        0.1,
        10000
    )

    return soil_half_life.tolist()

#Generate a list of systemic status values based on a random choice
def generate_systemic_status(num_chemicals):
    systemic_status = np.random.choice(
        ["systemic", "non_systemic"],
        size=num_chemicals
    )

    return systemic_status.tolist()

#Generate a dictionary containing all the generated chemical data
def generate_chemical_data(num_chemicals):
    active_ingredients = generate_active_ingredients(num_chemicals)
    chemical_classes = generate_chemical_classes(num_chemicals)
    logp = generate_logp(num_chemicals)
    water_solubility = generate_water_solubility(num_chemicals)
    vapor_pressure = generate_vapor_pressure(num_chemicals)
    henrys_constant = generate_henrys_constant(num_chemicals)
    koc = generate_koc(num_chemicals)
    molecular_weight = generate_molecular_weight(num_chemicals)
    pka = generate_pka(num_chemicals)
    hydrolysis_half_life = generate_hydrolysis_half_life(num_chemicals)
    photolysis_half_life = generate_photolysis_half_life(num_chemicals)
    soil_half_life = generate_soil_half_life(num_chemicals)
    systemic_status = generate_systemic_status(num_chemicals)

    return {
        "active_ingredients": active_ingredients,
        "chemical_classes": chemical_classes,
        "logp": logp,
        "water_solubility": water_solubility,
        "vapor_pressure": vapor_pressure,
        "henrys_constant": henrys_constant,
        "koc": koc,
        "molecular_weight": molecular_weight,
        "pka": pka,
        "hydrolysis_half_life": hydrolysis_half_life,
        "photolysis_half_life": photolysis_half_life,
        "soil_half_life": soil_half_life,
        "systemic_status": systemic_status
    }
chemical_data = generate_chemical_data(200)

#Generate a pandas DataFrame from the chemical data dictionary
def assemble_chemical_table(chemical_data):
    df = pd.DataFrame(chemical_data)
    return df
chemical_table = assemble_chemical_table(chemical_data)

#Save the chemical table to an Excel file
def export_to_excel(chemical_table):
    chemical_table.to_excel("chemical_features.xlsx", index=False)
export_to_excel(chemical_table)






