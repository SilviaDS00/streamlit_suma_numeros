import streamlit as st

st.title("Suma de números!")
st.subheader("Esta app suma 3 números")

st.write("Ingrese 3 números para sumarlos usando `number_input()`:")

n1 = st.number_input("Primer número:", step=1)
n2 = st.number_input("Segundo número:", step=1)
n3 = st.number_input("Tercer número:", step=1)

if n1 and n2 and n3:
    sum = n1 + n2 + n3
    st.write(f"La suma de {n1}, {n2} y {n3} es {sum}")
    
st.divider()
    
st.write("Usando `st.slider()`:")

p1 = st.slider("Primer número:", min_value=0, max_value=10, step=1)
p2 = st.slider("Segundo número:", min_value=0, max_value=10, step=1)
p3 = st.slider("Tercer número:", min_value=0, max_value=10, step=1)

sum = p1 + p2 + p3
st.write(f"La suma de {p1}, {p2} y {p3} es {sum}")

