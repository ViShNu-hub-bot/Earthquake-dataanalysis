import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# Function to load data
def load_data():
    file_path = "earthquake data.csv"  # Update the file path with your file's location
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to plot monthly earthquake distribution
def plot_monthly_distribution(data):
    data['Date & Time'] = pd.to_datetime(data['Date & Time'])
    data['Month'] = data['Date & Time'].dt.month
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Month', data=data, palette='viridis')
    plt.xlabel('Months')
    plt.ylabel('Number of earthquakes')
    plt.title('Monthly Earthquake distribution')
    st.pyplot()

# Function to plot weekly earthquake distribution
def plot_weekly_distribution(data):
    data['Date & Time'] = pd.to_datetime(data['Date & Time'])
    data['Weekday'] = data['Date & Time'].dt.weekday
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Weekday', data=data, palette='viridis')
    plt.xlabel('Weekdays')
    plt.ylabel('Number of earthquakes')
    plt.title('Weekdays Earthquake distribution')
    st.pyplot()

# Function to plot hourly earthquake distribution
def plot_hourly_distribution(data):
    data['Date & Time'] = pd.to_datetime(data['Date & Time'])
    data['Hour'] = data['Date & Time'].dt.hour
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Hour', data=data, palette='viridis')
    plt.xlabel('Hours')
    plt.ylabel('Number of earthquakes')
    plt.title('Hourly Earthquake distribution')
    st.pyplot()

# Function to plot geographical patterns
def plot_geographical_patterns(data):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Longitude', y='Latitude', data=data, hue='Magnitude', palette='viridis', size='Magnitude')
    plt.title('Geographical Patterns')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    st.pyplot()

# Function to plot depth & magnitude relationship
def plot_depth_magnitude_relationship(data):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Depth', y='Magnitude', data=data, palette='viridis')
    plt.title('Depth & Magnitude relationship')
    plt.xlabel('Depth')
    plt.ylabel('Magnitude')
    st.pyplot()

# Function to plot land types earthquakes distribution
def plot_land_types_earthquakes_distribution(data):
    plt.figure(figsize=(8, 6))
    top_lands = 20
    sns.countplot(x='Lands', data=data, order=data['Lands'].value_counts().index[:top_lands], palette='viridis')
    plt.title('Land types earthquakes distribution')
    plt.xlabel('Lands')
    plt.ylabel('Number of Earthquakes')
    plt.xticks(rotation=90)
    st.pyplot()

# Function to plot country specific analysis
def plot_country_specific_analysis(data):
    plt.figure(figsize=(8, 6))
    top_countries = 20
    sns.countplot(x='Country', data=data, order=data['Country'].value_counts().index[:top_countries], palette='viridis')
    plt.title('Country Specific Analysis')
    plt.xlabel('Country')
    plt.ylabel('Number of Earthquakes')
    plt.xticks(rotation=90)
    st.pyplot()

# Main function
def main():
    st.title("Earthquake Data Analysis")
    st.write("Developed by Vishnukanth K")
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/vishnukanth-k-a5552327b/)")
    
    # Load the data
    data = load_data()
    
    if data is not None:
        st.dataframe(data.head())
        
        if st.button("Show Monthly Earthquake Distribution"):
            plot_monthly_distribution(data)
        
        if st.button("Show Weekly Earthquake Distribution"):
            plot_weekly_distribution(data)
        
        if st.button("Show Hourly Earthquake Distribution"):
            plot_hourly_distribution(data)
        
        if st.button("Show Geographical Patterns"):
            plot_geographical_patterns(data)
        
        if st.button("Show Depth & Magnitude Relationship"):
            plot_depth_magnitude_relationship(data)
        
        if st.button("Show Land Types Earthquakes Distribution"):
            plot_land_types_earthquakes_distribution(data)
        
        if st.button("Show Country Specific Analysis"):
            plot_country_specific_analysis(data)

if __name__ == "__main__":
    main()
