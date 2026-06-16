import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#This imports all of the relevant libraries for the code to run.

df = pd.read_csv('telemetry_data(in).csv')
#This reads in the telemetry data from a CSV file and stores it in a pandas DataFrame called df.

df = df[1:] # Remove the first row of the DataFrame

df['timestamp'] = pd.to_datetime(df['timestamp'])
#This converts the 'timestamp' column in the DataFrame to a datetime format.

df['temperature_c'] = pd.to_numeric(df['temperature_c'], errors='coerce')
#This converts the 'temperature_c' column in the DataFrame to a numeric format, coercing any errors (e.g., non-numeric values) to NaN.

df['vibration_mm_s'] = pd.to_numeric(df['vibration_mm_s'], errors='coerce')
#This converts the 'vibration_mm_s' column in the DataFrame to a numeric format, coercing any errors to NaN.

df['rpm'] = pd.to_numeric(df['rpm'], errors='coerce')
#This converts the 'rpm' column in the DataFrame to a numeric format, coercing any errors to NaN.

av_temp_max = 85
vib_max = 15

boolean_T01 = df['turbine_id']== 'T-01'
boolean_T02 = df['turbine_id']== 'T-02'
boolean_T03 = df['turbine_id']== 'T-03'
boolean_T04 = df['turbine_id']== 'T-04'
boolean_T05 = df['turbine_id']== 'T-05'
boolean_T06 = df['turbine_id']== 'T-06'
boolean_T07 = df['turbine_id']== 'T-07'
boolean_T08 = df['turbine_id']== 'T-08'
boolean_T09 = df['turbine_id']== 'T-09'
#This creates boolean masks for each turbine ID, allowing for filtering the DataFrame based on the turbine ID.

data_T01 = df[boolean_T01]
data_T02 = df[boolean_T02]
data_T03 = df[boolean_T03]
data_T04 = df[boolean_T04]
data_T05 = df[boolean_T05]
data_T06 = df[boolean_T06]
data_T07 = df[boolean_T07]
data_T08 = df[boolean_T08]
data_T09 = df[boolean_T09]
#This creates separate DataFrames for each turbine by applying the boolean masks to the original DataFrame. Each new DataFrame contains only the data for the corresponding turbine ID.
data_list = [data_T01, data_T02, data_T03, data_T04, data_T05, data_T06, data_T07, data_T08, data_T09]

av_temp_list = []
for data in data_list:
    avg_temp = data['temperature_c'].mean()
    av_temp_list.append(avg_temp)

#This loop iterates over the list of turbine DataFrames, calculates the average temperature for each turbine, and appends it to the av_temp_list.


max_vib_list = []
for data in data_list:
    max_vib = data['vibration_mm_s'].max()
    max_vib_list.append(max_vib)
#This loop iterates over the list of turbine DataFrames, calculates the maximum vibration for each turbine, and appends it to the max_vib_list.

turbine_ids = ['T-01', 'T-02', 'T-03', 'T-04', 'T-05', 'T-06', 'T-07', 'T-08', 'T-09']
#This creates a list of turbine IDs corresponding to the DataFrames created earlier.

report_temp = []
report_vib = []


for temp in av_temp_list:
    if temp > av_temp_max:
        report_temp.append('Yes')
    else:
        report_temp.append('No')

#This loop iterates over the average temperature list and checks if each average temperature exceeds the maximum allowed temperature (av_temp_max). If it does, it appends 'Yes' to the report_temp list; otherwise, it appends 'No'.


for vib in max_vib_list:
    if vib > vib_max:
        report_vib.append('Yes')
    else:
        report_vib.append('No')

#This loop iterates over the maximum vibration list and checks if each maximum vibration exceeds the maximum allowed vibration (vib_max). If it does, it appends 'Yes' to the report_vib list; otherwise, it appends 'No'.

data_report = pd.DataFrame({
    'Turbine ID': turbine_ids,
    'Average Temperature (°C)': av_temp_list,
    'Maximum Vibration (mm/s)': max_vib_list,
    'Temperature Alert': report_temp,
    'Vibration Alert': report_vib
})

data_report.to_csv('telemetry_report.csv', index=False)

#This creates a new DataFrame called data_report that contains the turbine IDs, average temperatures, maximum vibrations, and alert statuses for temperature and vibration. It then saves this DataFrame to a CSV file named 'telemetry_report.csv' without including the index column.


def Temp_Time_Plot(data,i):
    avg_temp = data['temperature_c'].mean()
    max_temp = data['temperature_c'].max()
    #This defines a function called Temp_Time_Plot that takes a DataFrame (data) as input. It calculates the average and maximum temperatures from the 'temperature_c' column of the input DataFrame.

    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['temperature_c'], label='Temperature (°C)', color='blue')
    plt.axhline(y=avg_temp, color='orange', linestyle='--', label=f'Average Temp: {avg_temp:.2f} °C')
    plt.axhline(y=max_temp, color='red', linestyle='--', label=f'Max Temp: {max_temp:.2f} °C')
    plt.axhline(y=av_temp_max, color='black', linestyle='--', label=f'Max Allowed Temp: {av_temp_max} °C')
    plt.title(f'Temperature vs Time, Turbine ID: {i}  ')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.savefig(f'Temperature_Time_Plot_{i}.png')
    plt.close()
    #This part of the function creates a line plot of temperature over time, adds horizontal lines for average and maximum temperatures, and saves the plot as a PNG file named 'Temperature_Time_Plot_{i}.png', where {i} is the index of the turbine.

def Vib_Time_Plot(data,i):
    max_vib = data['vibration_mm_s'].max()
    #This defines a function called Vib_Time_Plot that takes a DataFrame (data) as input. It calculates the maximum vibration from the 'vibration_mm_s' column of the input DataFrame.

    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['vibration_mm_s'], label='Vibration (mm/s)', color='green')
    plt.axhline(y=max_vib, color='red', linestyle='--', label=f'Max Vibration: {max_vib:.2f} mm/s')
    plt.axhline(y=vib_max, color='black', linestyle='--', label=f'Max Allowed Vibration: {vib_max} mm/s')
    plt.title(f'Vibration vs Time, Turbine ID: {i}')
    plt.xlabel('Timestamp')
    plt.ylabel('Vibration (mm/s)')
    plt.legend()
    plt.grid()
    plt.savefig(f'Vibration_Time_Plot_{i}.png')
    plt.close()
    #This part of the function creates a line plot of vibration over time, adds a horizontal line for maximum vibration, and saves the plot as a PNG file named 'Vibration_Time_Plot_{i+1}.png', where {i} is the index of the turbine.

for data, turbine_id in zip(data_list, turbine_ids):
    Temp_Time_Plot(data, turbine_id)
    Vib_Time_Plot(data, turbine_id)

#This loop iterates over the list of turbine DataFrames, calling the Temp_Time_Plot and Vib_Time_Plot functions for each turbine's data. It generates and saves the temperature and vibration plots for each turbine, with the index i indicating the turbine number in the filenames.









