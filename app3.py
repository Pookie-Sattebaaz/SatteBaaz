import streamlit as st
import json
from streamlit_lottie import st_lottie

crypto_per_dollar = 0.0000114575479
usd_to_inr = 85  # USD to INR conversion rate

# CSS for centering the title
st.markdown("""
    <style>
        .title {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>Satta Lagane Wale Ladke</h1>", unsafe_allow_html=True)

#################
# Function to load Lottie animation from JSON file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the Lottie animation
lottie_scanner = load_lottiefile("Lottie/cool-rabbit.json")

# CSS to center the Lottie animation
st.markdown("""
    <style>
        .center-lottie {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

# Apply the centering style using a div wrapper
st.markdown('<div class="center-lottie">', unsafe_allow_html=True)

# Display the centered Lottie animation
st_lottie(
    lottie_scanner,
    key="None",
)

st.markdown('</div>', unsafe_allow_html=True)

#################

st.markdown("**NOTE : Use two stake amounts and bet the amount after filling the multiplier to get the results in 'Additional Details.'**")

# Input for total pool amount (user-defined)
pool = st.number_input("Enter Your Total Betting Pool Amount in Dollar ( NOTE: To have max profit and less risk use 25$ )", value=25.0)

# List of IPL teams
ipl_teams = [
    "Chennai Super Kings",
    "Mumbai Indians",
    "Kolkata Knight Riders",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad",
    "Lucknow Super Giants",
    "Gujarat Titans",
    "Delhi Capitals",
    "Punjab Kings"
]

# Dropdowns for selecting teams
team1 = st.selectbox("Select Team 1", ipl_teams)
team2 = st.selectbox("Select Team 2", ipl_teams)

# Input fields for multipliers (no constraints)
multiplier1 = st.number_input(f"Enter Multiplier for {team1}", value=1.5)
multiplier2 = st.number_input(f"Enter Multiplier for {team2}", value=2.0)

# Buttons to calculate bet amount
col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate Crypto Bet Amount"):
        crypto_bet1 = (pool / multiplier1) * crypto_per_dollar
        crypto_bet2 = (pool / multiplier2) * crypto_per_dollar

        st.subheader("Crypto Betting Amounts")
        st.write(f"**Bet amount on {team1}:** {crypto_bet1:.5f} BTC")
        st.write(f"**Bet amount on {team2}:** {crypto_bet2:.5f} BTC")


with col2:
    if st.button("Calculate INR Bet Amount"):
        inr_bet1 = (pool / multiplier1) * usd_to_inr
        inr_bet2 = (pool / multiplier2) * usd_to_inr

        st.subheader("INR Betting Amounts")
        st.write(f"**Bet amount on {team1}:** ₹{inr_bet1:.3f}")
        st.write(f"**Bet amount on {team2}:** ₹{inr_bet2:.3f}")

# Additional Details Button
if st.button("Additional Details"):
    max_profit = (pool*usd_to_inr - (pool / multiplier1) * usd_to_inr) + (pool*usd_to_inr - (pool / multiplier2) * usd_to_inr)
    loss_team1 = ((pool / multiplier2) * usd_to_inr) - (pool*usd_to_inr - (pool / multiplier1) * usd_to_inr)
    loss_team2 = ((pool / multiplier1) * usd_to_inr) - (pool*usd_to_inr - (pool / multiplier2) * usd_to_inr)

    st.subheader("Additional Details")

    st.write(f"**Maximum Profit (Both ID):** ₹{max_profit:.3f}")
    st.write(f"**Maximum Loss (BOTH ID):** ₹{loss_team1:.3f}")
    st.write(f"**Maximum Profit (Single ID):** ₹{max_profit/2:.3f}")
    st.write(f"**Maximum Loss (Single ID):** ₹{loss_team1/2:.3f}")







# Footer with creator credit
st.markdown("<p class='footer'>Yeah website Famous Sattebaaz <b>Sattori Baba</b> ne banayi hai</p>", unsafe_allow_html=True)
