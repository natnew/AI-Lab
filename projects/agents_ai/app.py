import streamlit as st
from projects.agents_ai.utils import create_role_playing_conversation

def run():
    st.title("AI Agents")
    st.write("""
    AI agents are autonomous systems powered by large language models (LLMs) that can plan, use tools, 
    execute tasks, and collaborate to achieve goals. You can also create role-playing agents for 
    engaging and entertaining exchanges.
    """)

    # Input section
    agent_1 = st.text_input("Enter Role for Agent 1 (e.g., Ali Wong)", value="Ali Wong")
    agent_2 = st.text_input("Enter Role for Agent 2 (e.g., Jimmy Yang)", value="Jimmy Yang")

    scenario = st.text_area("Enter the scenario or starting point for the conversation", 
                            placeholder="e.g., A humorous debate on the best takeout food.")

    if st.button("Generate Conversation"):
        if agent_1.strip() and agent_2.strip() and scenario.strip():
            with st.spinner("Generating conversation..."):
                try:
                    conversation = create_role_playing_conversation(agent_1, agent_2, scenario)
                    st.subheader("Generated Conversation")
                    st.write(conversation)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill out all fields.")
