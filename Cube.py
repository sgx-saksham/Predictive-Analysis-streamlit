import streamlit as st

st.title('Can you solve the Cube')
st.subheader('Want to try the Cube ? fill the form below 🙌')
st.image("https://img.etimg.com/thumb/width-1200,height-900,imgsize-53103,resizemode-75,msid-55348506/latentview-analytics-private-limited.jpg")

text_area = st.text_area('Tell Your Name and Proficiency')

options = ['Newbie', 'Intermediate', 'Expert']
dropdown = st.selectbox('Proficiency:', options)

if st.button('Submit'):
    st.write(f'Thanks {text_area} as you are an {dropdown} try this : https://saksham-with-cube.netlify.app/')
    st.image(f'https://saksham-gupta.netlify.app/static/media/theCube.b621d138.png')

if st.button('Clear'):
    st.experimental_rerun()

"""
2. In the Retail industry:
   - Customer Churn Prediction: Predicting whether a customer is likely to stop shopping with a particular retailer. This helps in implementing targeted retention strategies.
   - Demand Forecasting: Predicting the future demand for products based on historical data, aiding in inventory management and supply chain optimization.

3. Additional predictive applications in the Retail industry:
   - Fraud Detection: Identifying potentially fraudulent transactions, such as unauthorized credit card use or false returns, to protect the retail business from financial losses.
   - Price Optimization: Predicting optimal pricing for products based on various factors, maximizing revenue and ensuring competitiveness in the market.

4. More predictive applications in the Retail industry:
   - Inventory Management: Predicting the optimal amount of inventory to hold based on sales forecasts and historical trends.
   - Customer Lifetime Value Prediction: Predicting the net profit attributed to the entire future relationship with a customer.

5. In the Health industry:
   - Disease Diagnosis: Predicting whether a patient has a particular disease based on symptoms, medical history, and diagnostic tests, aiding in early intervention and treatment.
   - Patient Readmission Prediction: Predicting the likelihood of a patient being readmitted to the hospital after discharge, allowing healthcare providers to take preventive measures.

6. Additional predictive applications in the Health industry:
   - Drug Response Prediction: Predicting how patients will respond to a particular medication based on genetic and clinical data, enabling personalized medicine.
   - Length of Stay Prediction: Predicting the expected length of a patient's hospital stay, assisting in resource allocation and better patient care planning.

7. More predictive applications in the Health industry:
   - Epidemic Outbreak Prediction: Using data from various sources to predict the likelihood and spread of disease outbreaks.
   - Mental Health Prediction: Using patient data to predict mental health issues, helping in early detection and treatment.

8. In the Financial Services industry:
   - Credit Scoring: Predicting the creditworthiness of individuals or businesses based on financial history, helping in decision-making for loans and credit approvals.
   - Stock Price Prediction: Forecasting future stock prices based on historical market data and other relevant factors, aiding investors in making informed decisions.

9. Additional predictive applications in the Financial Services industry:
   - Customer Segmentation: Grouping customers based on similar characteristics and behaviors, allowing financial institutions to tailor products and services for different segments.
   - Default Risk Prediction: Predicting the likelihood of a borrower defaulting on a loan, assisting in risk management for lending institutions.

10. More predictive applications in the Financial Services industry:
   - Fraud Detection: Using machine learning algorithms to detect fraudulent transactions and protect against financial crime.
   - Market Basket Analysis: Using predictive analytics to understand the purchase behavior of customers and the relationships between the products that they buy.
"""