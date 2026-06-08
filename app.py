import streamlit as st

from src.generate_answer import answer_question


st.set_page_config(
    page_title="Financial AI Assistant",
    page_icon="📊"
)

st.title("Financial AI Assistant")

st.write(
    "Ask questions about Microsoft and NVIDIA annual reports. "
    "The assistant uses stored report data to answer."
)

company = st.selectbox("Company", ["all", "microsoft", "nvidia"])
year = st.selectbox("Year", ["all", "2024", "2025"])

question = st.text_area(
    "Your question",
    placeholder="Example: What does Microsoft say about AI?"
)

if st.button("Ask"):
    if question.strip():
        with st.spinner("Searching reports..."):
            answer = answer_question(
                question=question,
                company=company,
                year=year
            )

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

st.markdown("---")

st.markdown(
    """
    **Try asking:**

    - What does Microsoft say about AI?
    - What are Microsoft's main business risks?
    - What does NVIDIA say about data center growth?
    - What are NVIDIA's main business risks?
    - What are the main AI-related themes in the reports?
    """
)