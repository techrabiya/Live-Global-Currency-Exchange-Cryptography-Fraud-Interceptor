import streamlit as st
import random
import string

st.title("🔐 Rabia's Elite Password Security Tool")
st.write("Welcome! Evaluate your password strength and generate secure keys instantly.")

user_pwd = st.text_input("Enter a password to test strength:", type="password")

if user_pwd:
    length = len(user_pwd) >= 8
    digit = any(char.isdigit() for char in user_pwd)
    upper = any(char.isupper() for char in user_pwd)
    special = any(char in string.punctuation for char in user_pwd)
    
    score = sum([length, digit, upper, special])
    
    st.markdown("---")
    st.write(f"**Password Evaluated:** {user_pwd}")
    
    if score == 4:
        st.success("Strength Rating: 🛡️ STRONG (Elite Security)")
    elif score >= 2:
        st.warning("Strength Rating: ⚠️ MODERATE (Needs Improvement)")
    else:
        st.error("Strength Rating: ❌ WEAK (Vulnerable)")
    st.markdown("---")

st.subheader("Generate a Secure Password")
if st.button("Generate Secure Password"):
    chars = string.ascii_letters + string.digits + string.punctuation
    secure_pwd = "".join(random.choice(chars) for _ in range(12))
    st.info(f"Generated Secure PWD: `{secure_pwd}`")
