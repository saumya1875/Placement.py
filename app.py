import streamlit as st
import joblib

model = joblib.load("placement_dataset.pkl")

def main():
    st.title("Welcome to Placement Predictor")
    
    cgpa = st.slider("Choose your CGPA", min_value=0.0, max_value=10.0, step=0.1)
    st.write('Entered CGPA:', cgpa)
    
    if st.button("Predict"):
        result = model.predict([[cgpa]]) 
        st.success(f"Your predicted package would be: {result} LPA")  

if __name__ == "__main__":
    main()
