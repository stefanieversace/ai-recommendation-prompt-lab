import streamlit as st
import random

st.set_page_config(
    page_title="AI Recommendation Prompt Lab",
    page_icon="🎵",
    layout="centered"
)


def generate_prompt(user_input: str, strategy: str, use_case: str) -> str:
    """
    Generate a prompt based on the selected strategy and use case.
    """
    if use_case == "Entertainment":
        if strategy == "Basic":
            return f"Recommend 5 films or shows based on this request: {user_input}"
        elif strategy == "Structured":
            return (
                "You are a recommendation system.\n"
                f"User request: {user_input}\n"
                "Recommend exactly 5 films or shows.\n"
                "For each recommendation include:\n"
                "1. Title\n"
                "2. Genre\n"
                "3. One-sentence explanation\n"
            )
        elif strategy == "Persona-based":
            return (
                "You are an expert film and television critic.\n"
                f"Recommend 5 titles based on this request: {user_input}\n"
                "Explain briefly why each recommendation is a strong match."
            )

    elif use_case == "Security":
        if strategy == "Basic":
            return f"Recommend 5 relevant cybersecurity topics, techniques, or resources based on: {user_input}"
        elif strategy == "Structured":
            return (
                "You are a cybersecurity analyst.\n"
                f"User request: {user_input}\n"
                "Recommend exactly 5 relevant items.\n"
                "For each recommendation include:\n"
                "1. Topic or threat\n"
                "2. Why it is relevant\n"
                "3. A short analyst note\n"
            )
        elif strategy == "Persona-based":
            return (
                "You are a senior threat intelligence analyst.\n"
                f"Recommend 5 relevant threats, attack patterns, or intelligence areas based on this request: {user_input}\n"
                "Provide concise analyst commentary for each recommendation."
            )

    elif use_case == "Music":
        if strategy == "Basic":
            return f"Recommend 5 songs based on this request: {user_input}"
        elif strategy == "Structured":
            return (
                "You are a music recommendation system.\n"
                f"User request: {user_input}\n"
                "Recommend exactly 5 songs.\n"
                "For each recommendation include:\n"
                "1. Song title\n"
                "2. Artist\n"
                "3. Genre or vibe\n"
                "4. One-sentence explanation\n"
            )
        elif strategy == "Persona-based":
            return (
                "You are an expert music curator for a streaming platform.\n"
                f"Recommend 5 songs based on this request: {user_input}\n"
                "Focus on mood, sound, listener intent, and replay value."
            )

    return f"Recommend 5 items based on: {user_input}"


def get_recommendations(user_input: str, use_case: str) -> list[dict]:
    """
    Mock recommendations for demo purposes.
    Replace later with a real API if needed.
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

    music_data = {
        "sad_pop": [
            ("drivers license", "Olivia Rodrigo", "Melancholic pop ballad with emotional intensity."),
            ("Liability", "Lorde", "Minimal, vulnerable, and emotionally raw."),
            ("Skinny Love", "Bon Iver", "Fragile indie-folk with a haunting tone."),
            ("When the Party's Over", "Billie Eilish", "Quiet, intimate, and deeply reflective."),
            ("Ghostin", "Ariana Grande", "Soft and aching with layered emotional themes.")
        ],
        "indie_rainy": [
            ("Cherry Wine", "Hozier", "Gentle acoustic melancholy perfect for a reflective mood."),
            ("Moon Song", "Phoebe Bridgers", "Soft, intimate, and late-night feeling."),
            ("Holocene", "Bon Iver", "Atmospheric and expansive with introspective warmth."),
            ("Bloom", "The Paper Kites", "Dreamy indie texture for a rainy-day soundtrack."),
            ("Youth", "Daughter", "Delicate and cinematic with emotional depth.")
        ],
        "gym": [
            ("Paint The Town Red", "Doja Cat", "Confident, rhythmic, and high-energy."),
            ("Boss Bitch", "Doja Cat", "Aggressive pop-rap energy for workouts."),
            ("Physical", "Dua Lipa", "Fast-paced, polished, and upbeat."),
            ("Run the World (Girls)", "Beyoncé", "Powerful and motivating with strong momentum."),
            ("Titanium", "David Guetta ft. Sia", "Big-energy anthem built for intensity.")
        ],
        "dreamy_pop": [
            ("Supercut", "Lorde", "Glossy, emotional pop with a nostalgic edge."),
            ("Space Song", "Beach House", "Floating and dreamy with a hypnotic atmosphere."),
            ("After The Storm", "Kali Uchis", "Smooth, soft, and hazy in tone."),
            ("Sofia", "Clairo", "Warm indie-pop with an airy feel."),
            ("West Coast", "Lana Del Rey", "Slow, cinematic, and mood-driven.")
        ],
        "spotify_style": [
            ("Sunflower", "Post Malone, Swae Lee", "A highly replayable cross-genre streaming favourite."),
            ("As It Was", "Harry Styles", "Clean pop production with broad listener appeal."),
            ("Blinding Lights", "The Weeknd", "Strong repeat value, immediate hook, and mainstream appeal."),
            ("Good Days", "SZA", "Smooth, mood-based listening with playlist versatility."),
            ("505", "Arctic Monkeys", "Beloved catalogue track with strong emotional resonance.")
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

        recommendations = []
        for title, category, explanation in chosen:
            recommendations.append(
                {
                    "title": title,
                    "subtitle": category,
                    "explanation": explanation,
                    "confidence": random.randint(84, 97)
                }
            )
        return recommendations

    if use_case == "Security":
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
                    "subtitle": category,
                    "explanation": explanation,
                    "confidence": random.randint(84, 97)
                }
            )
        return recommendations

    if use_case == "Music":
        if any(word in text for word in ["sad", "heartbreak", "cry", "breakup", "emotional"]):
            chosen = music_data["sad_pop"]
        elif any(word in text for word in ["rain", "rainy", "indie", "walk", "moody"]):
            chosen = music_data["indie_rainy"]
        elif any(word in text for word in ["gym", "workout", "run", "energy", "female vocals"]):
            chosen = music_data["gym"]
        elif any(word in text for word in ["dreamy", "late night", "night", "soft pop", "ethereal"]):
            chosen = music_data["dreamy_pop"]
        elif any(word in text for word in ["spotify", "playlist", "replay", "popular", "streaming"]):
            chosen = music_data["spotify_style"]
        else:
            chosen = random.choice(list(music_data.values()))

        recommendations = []
        for song, artist, explanation in chosen:
            recommendations.append(
                {
                    "title": song,
                    "subtitle": artist,
                    "explanation": explanation,
                    "confidence": random.randint(84, 97)
                }
            )
        return recommendations

    return []


def fill_example(example_text: str):
    st.session_state.user_input = example_text


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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">AI Recommendation Prompt Lab</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">An interactive demo exploring prompt engineering for film, security, and music recommendation systems.</div>',
    unsafe_allow_html=True
)

st.divider()

with st.sidebar:
    st.header("Demo Settings")

    use_case = st.selectbox(
        "Use case",
        ["Entertainment", "Security", "Music"]
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

    elif use_case == "Security":
        if st.button("Threat intelligence topics relevant to phishing", use_container_width=True):
            fill_example("Threat intelligence topics relevant to phishing")
        if st.button("SOC topics related to alert triage and Sentinel", use_container_width=True):
            fill_example("SOC topics related to alert triage and Sentinel")
        if st.button("Key areas to study for ransomware analysis", use_container_width=True):
            fill_example("Key areas to study for ransomware analysis")

    elif use_case == "Music":
        if st.button("Songs like Night Changes but sadder", use_container_width=True):
            fill_example("Songs like Night Changes but sadder")
        if st.button("Indie songs for a rainy walk in London", use_container_width=True):
            fill_example("Indie songs for a rainy walk in London")
        if st.button("Gym songs with female vocals", use_container_width=True):
            fill_example("Gym songs with female vocals")

    st.markdown("---")
    st.markdown(
        "This is a **portfolio demo** showing how prompt engineering can support recommendation systems "
        "across multiple domains."
    )

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

user_input = st.text_input(
    "What would you like recommendations for?",
    value=st.session_state.user_input,
    placeholder="Example: Dreamy late-night pop songs"
)

col1, col2 = st.columns(2)

with col1:
    generate_clicked = st.button("Generate Recommendations", use_container_width=True)

with col2:
    clear_clicked = st.button("Clear", use_container_width=True)

if clear_clicked:
    st.session_state.user_input = ""
    st.rerun()

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
            if use_case == "Music":
                title_label = "Song"
                subtitle_label = "Artist"
            elif use_case == "Entertainment":
                title_label = "Title"
                subtitle_label = "Genre"
            else:
                title_label = "Topic"
                subtitle_label = "Category"

            st.markdown(
                f"""
                <div class="card">
                    <p style="margin: 0.2rem 0;"><strong>{title_label}:</strong> {rec['title']}</p>
                    <p style="margin: 0.2rem 0;"><strong>{subtitle_label}:</strong> {rec['subtitle']}</p>
                    <p style="margin: 0.2rem 0;"><strong>Why it fits:</strong> {rec['explanation']}</p>
                    <p style="margin: 0.2rem 0;"><strong>Confidence:</strong> {rec['confidence']}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.subheader("Analyst Insight")

        if use_case == "Music":
            st.write(
                "Music recommendation is especially useful for demonstrating user-intent modelling because listeners "
                "often describe what they want in emotional or contextual language rather than technical genre terms. "
                "This makes prompt design, mood interpretation, and output consistency especially important."
            )
        elif use_case == "Entertainment":
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
            "This project demonstrates how prompt engineering can be used not just to generate outputs, "
            "but to simulate recommendation logic, compare prompting strategies, and evaluate the quality of results."
        )

st.divider()
st.caption(
    "Built as a prompt engineering portfolio project. "
    "Next step: connect to a live model API for fully dynamic recommendations."
)
def analyse_preferences(user_input: str, use_case: str) -> dict:
    text = user_input.lower()

    if use_case == "Music":
        return {
            "primary_interests": ["indie", "emotional", "soft vocals"],
            "style_preferences": ["intimate", "warm", "lyric-driven"],
            "disliked": ["overly mainstream", "highly commercial"],
            "themes": ["late-night listening", "rainy mood", "reflective"]
        }

    elif use_case == "Entertainment":
        return {
            "primary_interests": ["thriller", "emotional depth"],
            "style_preferences": ["plot-driven", "character-focused"],
            "disliked": ["slow pacing"],
            "themes": ["psychological tension", "twists"]
        }

    elif use_case == "Security":
        return {
            "primary_interests": ["threat detection", "analysis"],
            "style_preferences": ["practical", "real-world"],
            "disliked": ["theoretical only"],
            "themes": ["SOC workflows", "incident response"]
        }

    return {}
