import streamlit as st
import sympy as sp

# Define symbolic variables
t, s = sp.symbols('t s')
b, b1, b2 = sp.symbols('b b1 b2')
tau, tau1, tau2 = sp.symbols('tau tau1 tau2')
n = sp.symbols('n')

# Simplified Laplace Transform Table
laplace_table = {
    "1. δ(t) (Unit impulse)": (sp.DiracDelta(t), 1),
    "2. S(t) (Unit step)": (sp.Heaviside(t), 1 / s),
    "3. r (Ramp)": (t, 1 / s**2),
    "4. t^(n-1)": (t**(n - 1), sp.factorial(n - 1) / s**n),
    "5. e^(-b*t)": (sp.exp(-b * t), 1 / (s + b)),
    "6. (1/τ)*e^(-t/τ)": (1 / tau * sp.exp(-t / tau), 1 / (tau * s + 1)),
    "7. t^(n-1)*e^(-b*t)": (t**(n - 1) * sp.exp(-b * t), 1 / (s + b)**n),
    "8. t^(n-1)*e^(-t/τ)": (t**(n - 1) * sp.exp(-t / tau), 1 / (tau * s + 1)**n),
    "9. (1/(b1 - b2))*(e^(-b1*t) - e^(-b2*t))": (
        (sp.exp(-b1 * t) - sp.exp(-b2 * t)) / (b1 - b2),
        1 / ((s + b1) * (s + b2)),
    ),
    "10. (1/(τ1 - τ2))*(e^(-t/τ1) - e^(-t/τ2))": (
        1 / (tau1 - tau2) * (sp.exp(-t / tau1) - sp.exp(-t / tau2)),
        1 / ((tau1 * s + 1) * (tau2 * s + 1)),
    ),
    "11. 1 - e^(-t/τ)": (1 - sp.exp(-t / tau), tau * s / (tau * s + 1)),
}

# Streamlit app
st.title("Simplified Laplace Transform Table Viewer")
st.write("Explore Laplace transformations between the time and Laplace domains for simplified functions.")

# User input: Direction and function selection
direction = st.radio("Select conversion direction:", ["Time Domain → Laplace Domain", "Laplace Domain → Time Domain"])
selected_function = st.selectbox("Choose a function:", list(laplace_table.keys()))

# Fetch the corresponding time and Laplace forms
time_form, laplace_form = laplace_table[selected_function]

# Display results based on direction
if direction == "Time Domain → Laplace Domain":
    st.subheader("Time Domain to Laplace Domain:")
    st.latex(f"f(t) = {sp.latex(time_form)}")
    st.latex(f"F(s) = {sp.latex(laplace_form)}")
else:
    st.subheader("Laplace Domain to Time Domain:")
    st.latex(f"F(s) = {sp.latex(laplace_form)}")
    st.latex(f"f(t) = {sp.latex(time_form)}")

# Notes
st.write("Note: Parameters like `b`, `τ`, `n`, etc., are symbolic placeholders. Replace them with specific values as needed.")
