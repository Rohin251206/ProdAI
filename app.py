import streamlit as st
import google.generativeai as genai

# --------------------------
# CONFIGURE GEMINI
# --------------------------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# --------------------------
# STREAMLIT PAGE SETTINGS
# --------------------------
st.set_page_config(page_title="🧠 AI Productivity Coach", layout="centered")
st.title("🧠 ProdAI - AI Productivity Coach")
st.write("Get personalized productivity tips, time management help, and motivation — powered by Gemini AI.")

# --------------------------
# USER INPUT SECTION
# --------------------------
st.subheader("💬 Tell me about your day or goals")
user_input = st.text_area("What would you like help with today? (e.g., focus, planning, procrastination, motivation)", height=150)

# --------------------------
# AI COACH LOGIC
# --------------------------
if st.button("Get Productivity Advice"):
    if user_input.strip():
        with st.spinner("Analyzing and coaching..."):
            prompt = f"""
            You are an AI productivity coach. 
            The user says: "{user_input}"

            1. Understand the user's current mindset or problem.
            2. Give 3 actionable, personalized steps to improve productivity.
            3. End with a short motivational quote or message.
            Keep your tone friendly, positive, and human.
            """

            response = model.generate_content(prompt)
            advice = response.text

        st.subheader("✨ Your Personalized Coaching Advice")
        st.write(advice)

        # Save as downloadable text
        st.download_button(
            label="Download Coaching Plan",
            data=advice,
            file_name="AI_Productivity_Coach_Advice.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please describe what you’d like help with before clicking the button!")

# --------------------------
# OPTIONAL: WEEKLY PRODUCTIVITY CHALLENGE
# --------------------------
st.markdown("---")
st.subheader("🔥 Need a Challenge?")
if st.button("Generate a 7-Day Productivity Challenge"):
    with st.spinner("Creating your challenge..."):
        challenge_prompt = """
        Create a 7-day productivity challenge for someone who wants to improve focus,
        consistency, and time management. Make each day’s task simple but effective.
        """
        challenge_response = model.generate_content(challenge_prompt)
        challenge_text = challenge_response.text

    st.write(challenge_text)

    st.download_button("Download 7-Day Challenge", challenge_text, file_name="7_Day_Challenge.txt")
