import streamlit as st

st.set_page_config(page_title="AI Recommendation Lab", layout="centered")

st.title("🎬 AI Recommendation Prompt Lab")

st.write("Enter your preferences and get AI-generated recommendations.")

user_input = st.text_input("What are you looking for?")

def generate_prompt(user_input):
    return f"Recommend 5 items based on: {user_input}"

def get_recommendations(prompt):
    # Replace this with real API later
    return [
        "Interstellar",
        "Arrival",
        "Shutter Island",
        "Gone Girl",
        "Prisoners"
    ]

if st.button("Get Recommendations"):
    if user_input:
        prompt = generate_prompt(user_input)
        results = get_recommendations(prompt)

        st.subheader("Recommendations:")
        for item in results:
            st.write(f"- {item}")
    else:
        st.warning("Please enter something first.")
