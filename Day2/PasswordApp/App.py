import streamlit as st
st.title("Password Analyser")
password=st.text_input("Enter the password",type='password')
# st.button("Validate")
if st.button("Validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and digit and special:
        st.success("Strong Password...Thank You!")
        
    else:
        st.error("Invalid Password!")
        if len(password)<8:
            st.write("Password must contain at least 8 characters")
        if not upper:
            st.write("Password must contain uppercase")
        if not lower:
            st.write("Password must contain lowercase")
        if not digit:
            st.write("Password must contain digits")
        if not special:
            st.write("Password must contain special characters")
    
    
