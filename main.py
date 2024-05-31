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

    st.markdown('## Make piechart')
    make_counts = df['Make'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(make_counts['count'], autopct='%1.1f%%', startangle=140)
    make_labels = [f'{l}, {(s/make_counts["count"].sum())*100:0.1f}%' for l, s in zip(make_counts['Make'], make_counts['count'])]
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=make_labels)
    plt.title('Make distribution')
    plt.axis('equal')
    st.pyplot(plt)
    plt.close()

    st.markdown('## Model piechart')
    model_counts = df['Model'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(model_counts['count'], autopct='%1.1f%%', startangle=140)
    model_labels = [f'{l}, {(s/model_counts["count"].sum())*100:0.1f}%' for l, s in zip(model_counts['Model'], model_counts['count'])]
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=model_labels)
    plt.title('Model distribution')
    plt.axis('equal')
    st.pyplot(plt)
    plt.close()

if __name__ == "__main__":
    main()
