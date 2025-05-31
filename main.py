import streamlit as st
from deepface import DeepFace
import tempfile

st.set_page_config(page_title="SimpleFaceCheck", layout="centered")
st.title("🔍 SimpleFaceCheck - Face Verification")

st.markdown("""
Upload **two face images** to verify if they belong to the same person.
The system uses a deep learning model to compute a similarity score.
""")

img1 = st.file_uploader("📤 Upload Reference Image (e.g., ID photo)", type=["jpg", "jpeg", "png"])
img2 = st.file_uploader("📤 Upload Selfie Image", type=["jpg", "jpeg", "png"])

if img1 and img2:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as ref_file, \
         tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as selfie_file:

        ref_file.write(img1.read())
        selfie_file.write(img2.read())
        ref_path = ref_file.name
        selfie_path = selfie_file.name

    with st.spinner("Verifying..."):
        try:
            result = DeepFace.verify(img1_path=ref_path, img2_path=selfie_path)
            verified = result.get("verified")
            distance = result.get("distance")

            st.success("✅ Match Found!" if verified else "❌ No Match.")
            st.write(f"**Similarity Score:** `{distance:.4f}` (lower is more similar)")

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
# Commit 2 - UI edit
# Commit 1: Add header comment for tracking
# Commit 2: Improve code readability
# Commit 3: Placeholder for logging
# Commit 4: Preparation for error handling
