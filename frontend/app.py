import streamlit as st
from api_client import upload_document, ask_question
st.set_page_config(
    page_title="AegisFlow",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AegisFlow — Private AI Document Auditor")

# ---------- Sidebar Upload ----------
st.sidebar.header("Upload Document")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:
    with st.sidebar:
        with st.spinner("Processing document..."):
            result = upload_document(uploaded_file)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Document indexed successfully!")
            st.write(result)


# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------- Chat Input ----------
question = st.chat_input("Ask a question about your documents...")

if question:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Send question to backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            result = ask_question(question)

            if "error" in result:
                st.error(result["error"])
            else:
                answer = result["answer"]
                followups = result.get("followups", [])

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                # Follow-up suggestions
                if followups:
                    st.markdown("**Suggested follow-up questions:**")
                    for f in followups:
                        st.button(f)