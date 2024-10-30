import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Monthly sales data for different products
data = {
    "Month": ["January", "February", "March", "April", "May"],
    "Product_A": [120, 150, 160, 130, 180],
    "Product_B": [90, 110, 95, 140, 130],
    "Product_C": [100, 105, 115, 125, 110]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Sample Data in DataFrame Format:")
print(df)


# Plotting the data
df.plot(x="Month", y=["Product_A", "Product_B", "Product_C"], kind="bar")

# Adding labels and title
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show the plot
plt.show()