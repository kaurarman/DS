import streamlit as st
import pandas as pd
import joblib

model = joblib.load("credit_risk_model.pkl")

st.title("Credit Risk Analysis System")

st.write(
    "Predict whether a loan applicant is likely to be approved or rejected."
)


no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

income_annum = st.number_input(
    "Annual Income"
)

loan_amount = st.number_input(
    "Loan Amount"
)

loan_term = st.number_input(
    "Loan Term"
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900
)

residential_assets_value = st.number_input(
    "Residential Assets Value"
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value"
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value"
)

bank_asset_value = st.number_input(
    "Bank Asset Value"
)
     

education = 0 if education == "Graduate" else 1

self_employed = 1 if self_employed == "Yes" else 0


if st.button("Predict Loan Status"):
  input_data = pd.DataFrame({
    'no_of_dependents':[no_of_dependents],
    'education':[education],
    'self_employed':[self_employed],
    'income_annum':[income_annum],
    'loan_amount':[loan_amount],
    'loan_term':[loan_term],
    'cibil_score':[cibil_score],
    'residential_assets_value':[residential_assets_value],
    'commercial_assets_value':[commercial_assets_value],
    'luxury_assets_value':[luxury_assets_value],
    'bank_asset_value':[bank_asset_value]
  })
  prediction = model.predict(input_data)
  probability = model.predict_proba(input_data)
  approval_prob = probability[0][0]
  if prediction[0] == 0:
    st.success("Loan Approved")
  else:
    st.error("Loan Rejected")
  risk_score = round(approval_prob * 100, 2)

  st.metric(
    "Approval Probability",
    f"{risk_score}%"
  )
  if approval_prob > 0.75:
    recommendation = "Approve Loan"

  elif approval_prob > 0.45:
    recommendation = "Review Manually"

  else:
    recommendation = "Reject Application"
  st.subheader("Recommendation")

  st.write(recommendation)
  
col1, col2 = st.columns(2)

with col1:
    st.header("Applicant Details")

with col2:
    st.header("Prediction Results")

st.sidebar.title("Credit Risk Dashboard")

st.sidebar.info(
    "Data Science Capstone Project"
)