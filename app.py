
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GenoHealth AI V2",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 GenoHealth AI")
st.subheader("Your Genes. Your Data. Our AI.")
st.info("Demo only — synthetic data, not for medical use.")

st.sidebar.title("GenoHealth AI")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Health Data", "About"]
)

if page == "Dashboard":
    st.header("Health Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Sample Glucose", "106 mg/dL")
    col2.metric("Sample HbA1c", "6.2%")
    col3.metric("Sample Records", "7 days")

    df = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu",
                "Fri", "Sat", "Sun"],
        "Glucose (mg/dL)": [105, 112, 101, 118,
                            109, 98, 106]
    })

    st.subheader("Sample Glucose Trend")
    st.line_chart(df.set_index("Day"))
    st.dataframe(df, use_container_width=True)

elif page == "Health Data":
    st.header("Health Data")
    st.write("Future module for validated data imports.")

else:
    st.header("About GenoHealth AI")
    st.write(
        "An early-stage AI health analytics "
        "and future genomics research platform."
    )
    st.caption("Prototype only. No medical predictions.")
