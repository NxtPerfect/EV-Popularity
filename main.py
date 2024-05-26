import polars as pl
import streamlit as st
import matplotlib.pyplot as plt

CSV_PATH = "./data/Electric_Vehicle_Population_Data.csv"

def main():
    df = pl.read_csv(CSV_PATH, dtypes={
        "VIN (1-10)": pl.Utf8,
        "County": pl.Utf8,
        "City": pl.Utf8,
        "State": pl.Utf8,
        "Postal Code": pl.Utf8,
        "Model Year": pl.UInt16,
        "Make": pl.Utf8,
        "Model": pl.Utf8,
        "Electric Vehicle Type": pl.Utf8,
        "Clean Alternative Fuel Vehicle (CVAF) Eligibility": pl.UInt8,
        "Electric Range": pl.UInt16,
        "Base MSRP": pl.UInt32,
        "Legislative District": pl.Utf8,
        "Vehicle Location": pl.Utf8,
        "Electric Utility": pl.Utf8,
        "2020 Census Tract": pl.UInt64,
        })
    st.markdown("# EV Population Data")
    st.markdown("## Data")
    st.dataframe(df)


    st.markdown("## Make piechart")
    make_counts = df["Make"].value_counts()
    st.write(make_counts, make_counts["count"])
    make_percentage = df.with_columns((pl.col('count') / make_counts['count'].sum() * 100).alias('percentage'))
    plt.figure(figsize=(10, 6))
    plt.pie(make_percentage["percentage"].to_list(), labels=make_percentage["Make"].to_list(), autopct="%1.1f%%", startangle=140)
    plt.title("Make distribution")
    plt.axis('equal')
    st.pyplot(plt)
    plt.close()

if __name__ == "__main__":
    main()
