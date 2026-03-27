import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="AI Recommendation Prompt Lab",
    page_icon="🎯",
    layout="centered"
)

# ----------------------------
# Helper functions
# ----------------------------
def generate_prompt(user_input: str, strategy: str, use_case: str) -> str:
    """
    Generate a prompt based on the selected strategy and use case.
    """
    if use_case == "Entertainment":
        if strategy == "Basic":
            return f"Recommend 5 movies, shows, or media titles based on this request: {user_input}"
        elif strategy == "Structured":
            return (
                f"You are a recommendation system. Based on the user's request, recommend exactly 5 titles.\n"
                f"User request: {user_input}\n"
                f"For each recommendation, include:\n"
                f"1. Title\n"
                f"2. Genre\n"
                f"3. One-sentence explanation\n"
            )
        elif strategy == "Persona-based":
            return (
                f"You are an expert film and television critic. Recommend 5 titles based on this request: {user_input}.\n"
                f"Explain why each recommendation is a strong match in a thoughtful but concise way."
            )

    elif use_case == "Security":
        if strategy == "Basic":
            return f"Recommend 5 relevant threat intelligence topics, techniques, or resources based on: {user_input}"
        elif strategy == "Structured":
            return (
                f"You are a cybersecurity analyst. Based on the user's request, recommend exactly 5 relevant items.\n"
                f"User request: {user_input}\n"
                f"For each recommendation, include:\n"
                f"1. Topic or threat\n"
                f"2. Why it is relevant\n"
                f"3. A short analyst note\n"
            )
        elif strategy == "Persona-based":
            return (
                f"You are a senior threat intelligence analyst. Recommend 5 relevant threats, attack patterns, "
                f"or intelligence areas based on this request: {user_input}.\n"
                f"Provide concise analyst commentary for each recommendation."
            )

    return f"Recommend 5 items based on: {user_input}"


def get_recommendations(user_input: str, use_case: str) -> list[dict]:
    """
    Mock recommendations for demo purposes.
    You can later replace this with a real API call.
    """
    entertainment_data = {
        "thriller": [
            ("Gone Girl", "Psychological Thriller", "A tense and twist-filled story with strong suspense."),
            ("Shutter Island", "Mystery Thriller", "A dark, atmospheric thriller with a psychological edge."),
            ("Prisoners", "Crime Thriller", "A gripping and emotionally intense investigation story."),
            ("Nightcrawler", "Neo-Noir Thriller", "Sharp, unsettling, and fast-paced with strong tension."),
            ("The Girl with the Dragon Tattoo", "Mystery Thriller", "A dark and compelling mystery with layered characters.")
        ],
        "romcom": [
            ("Definitely, Maybe", "Romantic Comedy", "A charming and underrated rom-com with emotional depth."),
            ("The Holiday", "Romantic Comedy", "A cosy and well-loved pick with warmth and humour."),
            ("13 Going on 30", "Romantic Comedy", "Fun, nostalgic, and light-hearted with broad appeal."),
            ("Music and Lyrics", "Romantic Comedy", "A sweet and witty film with an easy-going tone."),
            ("How to Lose a Guy in 10 Days", "Romantic Comedy", "A classic fast-paced rom-com with great chemistry.")
        ],
        "scifi": [
            ("Interstellar", "Science Fiction", "Emotional, visually ambitious, and intellectually engaging."),
            ("Arrival", "Science Fiction", "Thoughtful, emotional, and built around language and perception."),
            ("Ex Machina", "Science Fiction", "A smart and contained story about AI and power."),
            ("Blade Runner 2049", "Science Fiction", "Atmospheric and visually striking with philosophical depth."),
            ("Annihilation", "Science Fiction", "Unsettling and imaginative with strong conceptual themes.")
        ],
        "comfort": [
            ("Julie & Julia", "Drama/Comedy", "Warm, comforting, and perfect for a cosy mood."),
            ("Notting Hill", "Romantic Comedy", "Gentle, charming, and easy to rewatch."),
            ("The Parent Trap", "Family Comedy", "Light and nostalgic with feel-good energy."),
            ("Chef", "Comedy/Drama", "Relaxed, uplifting, and centred around food and family."),
            ("Mamma Mia!", "Musical Comedy", "Bright, fun, and pure escapism.")
        ]
    }

    security_data = {
        "phishing": [
            ("Email Phishing", "Threat Type", "Still one of the most common initial access methods."),
            ("Spear Phishing", "Threat Type", "Highly targeted and often more convincing than generic phishing."),
            ("Credential Harvesting", "Attack Technique", "Used to steal usernames and passwords for follow-on access."),
            ("Business Email Compromise", "Fraud Technique", "A major financial and operational risk for organisations."),
            ("Attachment-Based Malware", "Delivery Method", "Malicious documents remain a frequent attack vector.")
        ],
        "ransomware": [
            ("Initial Access Brokers", "Threat Ecosystem", "Often enable ransomware groups by selling access."),
            ("Privilege Escalation", "Attack Technique", "A common step before widespread ransomware deployment."),
            ("Lateral Movement", "Attack Technique", "Used to spread across systems before encryption."),
            ("Data Exfiltration", "Attack Technique", "Now frequently paired with encryption for double extortion."),
            ("Incident Response Planning", "Defensive Focus", "Critical for reducing ransomware impact.")
        ],
        "threat intel": [
            ("MITRE ATT&CK Mapping", "Framework", "Helps organise and analyse adversary behaviour."),
            ("IOC Management", "Threat Intelligence Process", "Useful for tracking domains, hashes, and IPs."),
            ("OSINT Collection", "Intelligence Practice", "Supports enrichment and contextual analysis."),
            ("Threat Actor Profiling", "Analysis Area", "Builds understanding of motivation, capability, and patterns."),
            ("Detection Engineering", "Defensive Practice", "Turns intelligence into practical monitoring rules.")
        ],
        "soc": [
            ("Alert Triage", "SOC Workflow", "A core task for assessing severity and next steps."),
            ("Log Analysis", "SOC Workflow", "Essential for identifying suspicious activity patterns."),
            ("KQL Detection Queries", "Detection Engineering", "Useful for building practical SIEM detections."),
            ("Incident Escalation", "SOC Workflow", "Important for routing serious issues appropriately."),
            ("False Positive Reduction", "Operational Focus", "Improves analyst efficiency and detection quality.")
        ]
    }

    text = user_input.lower()

    if use_case == "Entertainment":
        if any(word in text for word in ["thriller", "twist", "suspense", "crime", "dark"]):
            chosen = entertainment_data["thriller"]
        elif any(word in text for word in ["romcom", "rom-com", "romantic comedy", "love", "dating"]):
            chosen = entertainment_data["romcom"]
        elif any(word in text for word in ["sci-fi", "science fiction", "space", "future", "alien", "ai"]):
            chosen = entertainment_data["scifi"]
        elif any(word in text for word in ["comfort", "cosy", "cozy", "feel good", "rainy"]):
            chosen = entertainment_data["comfort"]
        else:
            chosen = random.choice(list(entertainment_data.values()))
    else:
        if any(word in text for word in ["phishing", "email", "credential"]):
            chosen = security_data["phishing"]
        elif any(word in text for word in ["ransomware", "extortion", "encrypt"]):
            chosen = security_data["ransomware"]
        elif any(word in text for word in ["intel", "intelligence", "ioc", "threat actor", "osint"]):
            chosen = security_data["threat intel"]
        elif any(word in text for word in ["soc", "siem", "alert", "triage", "kql", "sentinel", "log"]):
            chosen = security_data["soc"]
        else:
            chosen = random.choice(list(security_data.values()))

    recommendations = []
    for title, category, explanation in chosen:
        recommendations.append(
            {
                "title": title,
                "category": category,
                "explanation": explanation,
                "confidence": random.randint(84, 97)
            }
        )
    return recommendations


def fill_example(example_text: str):
    st.session_state.user_input = example_text


# ----------------------------
# Styling
# ----------------------------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            color: #666666;
            margin-bottom: 1.2rem;
        }
        .card {
            padding: 1rem;
            border: 1px solid #e6e6e6;
            border-radius: 16px;
            margin-bottom: 1rem;
            background-color: #fafafa;
        }
        .small-note {
            color: #666666;
            font-size: 0.95rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">AI Recommendation Prompt Lab</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">An interactive demo exploring prompt engineering for recommendation systems.</div>',
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.header("Demo Settings")

    use_case = st.selectbox(
        "Use case",
        ["Entertainment", "Security"]
    )

    strategy = st.selectbox(
        "Prompt strategy",
        ["Basic", "Structured", "Persona-based"]
    )

    st.markdown("### Example Inputs")

    if use_case == "Entertainment":
        if st.button("Underrated thrillers with plot twists", use_container_width=True):
            fill_example("Underrated thrillers with plot twists")
        if st.button("Comfort movies for a rainy day", use_container_width=True):
            fill_example("Comfort movies for a rainy day")
        if st.button("Movies like Interstellar but more emotional", use_container_width=True):
            fill_example("Movies like Interstellar but more emotional")
    else:
        if st.button("Threat intelligence topics relevant to phishing", use_container_width=True):
            fill_example("Threat intelligence topics relevant to phishing")
        if st.button("SOC topics related to alert triage and Sentinel", use_container_width=True):
            fill_example("SOC topics related to alert triage and Sentinel")
        if st.button("Key areas to study for ransomware analysis", use_container_width=True):
            fill_example("Key areas to study for ransomware analysis")

    st.markdown("---")
    st.markdown(
        "This is a **portfolio demo**. It uses mock recommendation logic now, "
        "but can later be connected to a live LLM API."
    )

# ----------------------------
# Main input
# ----------------------------
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

user_input = st.text_input(
    "What would you like recommendations for?",
    value=st.session_state.user_input,
    placeholder="Example: Fast-paced thrillers with plot twists"
)

col1, col2 = st.columns([1, 1])
with col1:
    generate_clicked = st.button("Generate Recommendations", use_container_width=True)
with col2:
    clear_clicked = st.button("Clear", use_container_width=True)

if clear_clicked:
    st.session_state.user_input = ""
    st.rerun()

# ----------------------------
# Output
# ----------------------------
if generate_clicked:
    if not user_input.strip():
        st.warning("Please enter a request first.")
    else:
        prompt = generate_prompt(user_input, strategy, use_case)

        with st.spinner("Generating recommendations..."):
            recommendations = get_recommendations(user_input, use_case)

        st.divider()

        st.subheader("Generated Prompt")
        st.code(prompt, language="text")

        st.subheader("Recommendations")

        for rec in recommendations:
            st.markdown(
                f"""
                <div class="card">
                    <h4 style="margin-bottom: 0.4rem;">{rec['title']}</h4>
                    <p style="margin: 0.2rem 0;"><strong>Category:</strong> {rec['category']}</p>
                    <p style="margin: 0.2rem 0;"><strong>Why it fits:</strong> {rec['explanation']}</p>
                    <p style="margin: 0.2rem 0;"><strong>Confidence:</strong> {rec['confidence']}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.subheader("Analyst Insight")
        if use_case == "Entertainment":
            st.write(
                "This output shows how recommendation quality changes based on prompt design. "
                "More structured prompts typically produce more consistent and explainable results."
            )
        else:
            st.write(
                "This output demonstrates how prompt engineering can be adapted for intelligence-style tasks, "
                "including topic recommendation, analytical framing, and relevance prioritisation."
            )

        st.subheader("Why this demo matters")
        st.write(
            "This project is designed to show how prompt engineering can be used not just to generate outputs, "
            "but to simulate recommendation logic, compare prompting approaches, and evaluate response quality."
        )

# ----------------------------
# Footer
# ----------------------------
st.divider()
st.caption(
    "Built as a prompt engineering portfolio project. "
    "Next step: connect to a live LLM API for real-time generated outputs."
)
