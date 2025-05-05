import streamlit as st
import dashscope
from dashscope import Generation

# Set API key and base URL
DASHSCOPE_API_KEY = 'Your API KEY'
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

# Model lists by category
text_models = [
    "qwen", "qwen-max", "qwen-plus", "qwen-lite", "qwen-turbo", "qwen-long",
    "qwen2", "qwen2.5", "qwen2-max", "qwen2-plus", "qwen2-lite", "qwen2-turbo",
    "qwen2.5-max", "qwen2.5-plus", "qwen2.5-lite", "qwen2.5-turbo"
]
audio_models = ["qwen-audio", "qwen-audio-max"]
vision_models = ["qwen-vision", "qwen-vision-max"]
multimodal_models = ["qwen-multimodal", "qwen-multimodal-max"]

all_models = text_models + audio_models + vision_models + multimodal_models

# Streamlit UI
st.title("🤖 Qwen AI Interface")
st.write("Select a model and interact with Qwen via text, audio, or image!")

selected_model = st.selectbox("🧠 Select AI Model:", all_models, index=all_models.index("qwen-plus"))

# Determine model type
if selected_model in text_models:
    input_type = "text"
elif selected_model in audio_models:
    input_type = "audio"
elif selected_model in vision_models:
    input_type = "image"
elif selected_model in multimodal_models:
    input_type = "multimodal"
else:
    input_type = "unknown"

# Input section
user_text = None
uploaded_file = None

if input_type == "text":
    user_text = st.text_input("💬 Enter your question:")
elif input_type == "audio":
    uploaded_file = st.file_uploader("🔊 Upload an audio file", type=["mp3", "wav", "m4a"])
elif input_type == "image":
    uploaded_file = st.file_uploader("🖼 Upload an image", type=["jpg", "jpeg", "png"])
elif input_type == "multimodal":
    st.info("📦 Multimodal models not yet supported in this demo.")
else:
    st.error("Unknown model type.")

# Submit button
if st.button("🚀 Get Answer"):
    if input_type == "text":
        if not user_text or not user_text.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    messages = [
                        {'role': 'system', 'content': 'you are a helpful assistant'},
                        {'role': 'user', 'content': user_text}
                    ]
                    response = Generation.call(
                        api_key=DASHSCOPE_API_KEY,
                        model=selected_model,
                        messages=messages,
                        result_format='message'
                    )
                    answer = response.output.choices[0].message.content
                    st.markdown("### 🧠 Response:")
                    st.success(answer)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    elif input_type in ["audio", "image"]:
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            st.warning(f"Model '{selected_model}' support is not implemented in this demo yet.")
    elif input_type == "multimodal":
        st.warning("Multimodal models will require combined input (text + image/audio). Not supported yet.")
