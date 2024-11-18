import google.generativeai as genai
import streamlit as st
from streamlit_lottie import st_lottie 
import json


def load_lottie_url(url: str):
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Set up Google Generative AI (GenAI) API key
f = open("keys/Gemini_Api.txt")
key = f.read()
genai.configure(api_key=key)

# Set up the main title and theme
st.set_page_config(page_title="GenAI Code Reviewer", page_icon="💡")

# Sidebar: Welcome dashboard with description and icons
st.sidebar.title("Welcome to GenAI Reviewer! 💻")
st.sidebar.markdown("""
**GenAI Code Reviewer** helps you analyze your Python code for errors and potential improvements.
Submit your code to get real-time, expert-level feedback powered by Google's Generative AI.
""")
st.sidebar.markdown("📝 **How It Works:**\n1. Enter your Python code.\n2. Click 'Generate Review'.\n3. Receive AI-powered feedback!")
st.sidebar.markdown("🌟 **Benefits:**\n- Real-time feedback\n- Error detection\n- Improvement suggestions")

# Lottie animation for the main interface (using a public URL for demonstration)
lottie_animation_url = "https://assets7.lottiefiles.com/packages/lf20_hz6jzprc.json"  # Replace with a suitable Lottie URL
lottie_animation = load_lottie_url(lottie_animation_url)
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="animation")

# Main title and subtitle
st.title("GenAI App - AI Code Reviewer 🤖")
st.subheader("Submit your Python code for review and get helpful feedback instantly!")

# Input area for Python code
user_prompt = st.text_area("Enter your Python code here:", placeholder="Paste your code here...", height=150)

# Button to generate review
if st.button("Generate Review"):
    if user_prompt:
        try:
            # Initialize the GenAI model
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            ai_assistant = model.start_chat(history=[])

            # Generate a response from the AI model
            response = ai_assistant.send_message(
                f"Please review the following Python code for errors or improvements:\n\n{user_prompt}\n\nProvide feedback and suggest fixes if necessary."
            )

            # Subheader for the corrected code and review
            st.markdown("<h2 style='color: green;'>Corrected Code and Review:</h2>", unsafe_allow_html=True)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter your Python code.")

# Footer or additional information
st.markdown("---")
st.markdown("🔍 **Powered by Google's Generative AI** | Made with ❤️ using Streamlit")
