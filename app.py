import streamlit as st
from google import genai
import os

# Page Configuration for a cleaner UI
st.set_page_config(page_title="VocalBridge AI", layout="centered")

st.title("🎙️ VocalBridge AI")
st.subheader("The Zero-Text Multimodal Literacy Platform")
st.write("An interactive learning environment bridging child speech and drawing data with advanced metrics.")

# Initialize Gemini Client (picks up key from environment secrets)
# We handle a fallback if the user is testing locally without the key set yet
api_key = os.environ.get("GEMINI_API_KEY", "")
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None
    st.warning("⚠️ GEMINI_API_KEY environment variable not found. Please set it in your app configuration.")

# Left and Right layout split for side-by-side interface metrics
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Step 1: Visual Canvas Prompt")
    # A public placeholder image displaying an illustrative story prompt
    st.image("https://images.unsplash.com/photo-1544717305-2782549b5136?q=80&w=600", 
             caption="Story Scene Prompt: What's happening here?")

with col2:
    st.markdown("### Step 2: Audio Recording")
    # Streamlit native audio recorder module 
    audio_file = st.audio_input("Record your narrative story aloud:")

# Processing Execution Execution Module Pipeline Trigger
if audio_file is not None and client is not None:
    if st.button("🚀 Execute AI Multi-modal Evaluation", type="primary"):
        with st.spinner("Analyzing audio tracking frequencies..."):
            
            prompt = """
            You are an expert cognitive development and childhood literacy AI evaluator. 
            Analyze the provided audio recording (the story spoken by the user).
            
            Provide your output in a clean, beautifully formatted layout with two distinct sections:
            1. **LEARNER SCORECARD**: Evaluate phoneme clarity, syntax structure, and narrative logic. Give constructive, uplifting coaching advice.
            2. **STAKEHOLDER DATA (JSON)**: End your response with a markdown code block containing a valid JSON object matching these specific keys:
               - phoneme_accuracy (float between 0.0 and 1.0)
               - vocabulary_level ("Early", "Intermediate", "Advanced")
               - syntax_milestone_met (true/false)
               - system_recommendation (string text)
            """
            
            try:
                # Read raw uploaded file bytes 
                audio_bytes = audio_file.read()
                
                # Ingest into Gemini using the native multimodal data wrapper
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=[
                        prompt,
                        {"mime_type": "audio/wav", "data": audio_bytes}
                    ]
                )
                
                st.success("Analysis Complete!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Operational Execution Fault: {str(e)}")
                