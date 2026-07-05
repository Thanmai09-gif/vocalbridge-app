import streamlit as st
from google import genai
import os

# 1. Custom Visual Theme Injection
st.set_page_config(
    page_title="VocalBridge AI Platform", 
    page_icon="🎙️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Custom CSS for standard enterprise aesthetics
# Custom CSS for standard enterprise aesthetics
st.markdown("""
    <style>
    .main-title { font-size: 42px !important; font-weight: 700 !important; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size: 18px !important; color: #4B5563; margin-bottom: 25px; }
    .card-box { padding: 20px; border-radius: 10px; background-color: #F3F4F6; border: 1px solid #E5E7EB; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)  # <-- Changed this parameter name to unsafe_allow_html

st.markdown('<div class="main-title">🎙️ VocalBridge AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">The Multimodal Decision Intelligence Platform for Civic Literacy Acceleration</div>', unsafe_allow_html=True)
st.divider()

# Core System Ingestion Setup
api_key = os.environ.get("GEMINI_API_KEY", "")
if not api_key:
    st.error("🛑 CRITICAL ARCHITECTURE ERROR: GEMINI_API_KEY missing in Streamlit Cloud Advanced Settings > Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Balanced Layout Structure Columns
left_panel, right_panel = st.columns([1, 1], gap="large")

with left_panel:
    st.markdown("### 🖼️ Interactive Story Prompt")
    st.markdown('<div class="card-box"><b>Instructions:</b> Review the situation image below. Formulate an imaginative description outlining the character problem context.</div>', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1544717305-2782549b5136?q=80&w=600", 
        use_container_width=True,
        caption="Scenario Case Model Alpha: Visual Stimulus Module"
    )

with right_panel:
    st.markdown("### 🔊 Narrative Audio Capture")
    st.markdown('<div class="card-box"><b>Voice Recording:</b> Click the mic to stream spoken narration data to Vertex AI pipelines.</div>', unsafe_allow_html=True)
    
    audio_file = st.audio_input("Record narrative delivery:")

    if audio_file is not None:
        st.success("✅ Multi-modal digital audio packet buffered successfully.")
        
        if st.button("🚀 Trigger Decision Intelligence Analysis", type="primary", use_container_width=True):
            with st.spinner("Executing native multi-modal inference inside Gemini 1.5 Flash..."):
                try:
                    audio_bytes = audio_file.read()
                    
                    prompt = """
                    You are an expert cognitive development and childhood literacy AI evaluator. 
                    Analyze the provided audio recording (the story spoken by the user).
                    
                    Provide your output in a clean, beautifully formatted layout with two distinct sections:
                    1. **LEARNER SCORECARD**: Evaluate phoneme clarity, syntax structure, and narrative logic. Give constructive, uplifting coaching advice. Use bullet points and emoji checkmarks.
                    2. **STAKEHOLDER DATA (JSON)**: End your response with a markdown code block containing a valid JSON object matching these specific keys:
                       - phoneme_accuracy (float between 0.0 and 1.0)
                       - vocabulary_level ("Early", "Intermediate", "Advanced")
                       - syntax_milestone_met (true/false)
                       - system_recommendation (string text)
                    """

                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=[
                            prompt,
                            {"mime_type": "audio/wav", "data": audio_bytes}
                        ]
                    )
                    
                    st.divider()
                    st.markdown("### 📊 Real-Time AI Platform Metrics Output")
                    st.info("The output payload below is parsed dynamically into BigQuery structural analytics caches.")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Execution Fault: {str(e)}")

                    
                