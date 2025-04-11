import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.special import erf
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "K1.xlsx"  # Make sure the file is in the same directory
df = pd.read_excel(file_path, sheet_name="Foglio1")

# Clean and extract relevant columns (adjust these indices if needed)
df_cleaned = df.iloc[2:, 2:4]
df_cleaned.columns = ["Depth (um)", "K/Si Concentration"]
df_cleaned = df_cleaned.dropna().reset_index(drop=True)

# Convert data to numeric values
df_cleaned = df_cleaned.astype(float)

# Extract depth (x) and concentration (C) values
x_data = df_cleaned["Depth (um)"].values
C_data = df_cleaned["K/Si Concentration"].values

# Define the error function model: C(x) = A + (B - A) * (1 - erf(x / C))
def diffusion_model(x, A, B, C):
    return A + (B - A) * (1 - erf(x / C))

# Initial guess for parameters [A, B, C]
initial_guess = [min(C_data), max(C_data), 10]

# Fit the model to data
params, covariance = opt.curve_fit(diffusion_model, x_data, C_data, p0=initial_guess)
A_fit, B_fit, C_fit = params

# Given diffusion time (t = 8h = 28800s), calculate D using C = sqrt(4Dt) -> D = C^2 / (4t)
t_seconds = 8 * 3600
D = (C_fit**2) / (4 * t_seconds)

# Print diffusion coefficient
print(f"Estimated Diffusion Coefficient: D = {D:.2e} cm²/s")

# Plot original data and fitted curve
plt.scatter(x_data, C_data, label="Experimental Data", color="black", s=10)
x_fit = np.linspace(min(x_data), max(x_data), 300)
plt.plot(x_fit, diffusion_model(x_fit, *params), label="Fitted Curve", color="red")
plt.xlabel("Depth (µm)")
plt.ylabel("K/Si Concentration")
plt.legend()
plt.title("Diffusion Profile Fit")
plt.show()