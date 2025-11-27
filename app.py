import streamlit as st

st.set_page_config(page_title="Void Texts", page_icon="🕳️")
st.title("🕳️ Void Texts – Stay No Contact")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "ex_number" not in st.session_state:
    st.session_state.ex_number = ""

with st.sidebar:
    st.header("Settings")
    number = st.text_input("Blocked ex number (never really sent)", st.session_state.ex_number)
    if st.button("Save & Block Forever"):
        st.session_state.ex_number = number
        st.success("Blocked. Texts go to the void.")

st.info("Type anything. It will NEVER reach your ex.")

user_input = st.chat_input(f"Sending to {st.session_state.ex_number or 'the void'}...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": "✅ Sent to the void. You stayed strong."})

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
