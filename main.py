import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit app title and description
st.title("JustiBot")
st.write("Where your needs meet AI.")

# Input for user's prompt
user_prompt = st.text_area("Enter your prompt:", value="Hello, I am JusticeBot how can I help you?")

# Generate text with GPT-3
if st.button("Generate"):
    if user_prompt:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can use different engines like "text-davinci-003" for different use cases
                prompt=user_prompt,
                max_tokens=150,  # Adjust the max_tokens based on your desired text length
                n = 1,  # Number of completions to generate
                stop=None,  # You can specify stopping criteria
                temperature=0.5,  # Adjust the temperature for randomness
            )
            generated_text = response.choices[0].text.strip()
            st.subheader("Generated Text:")
            st.write(generated_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")

# Display information about GPT-3
st.subheader("About Justibot:")
st.write(
    "It is an AI-Powered generative chatbot which provides legal knowledge and advice "
)

# Add a link to OpenAI's GPT-3 documentation
st.subheader("Created by ")
st.markdown("[Shreya Roy](https://github.com/royshreyaa)")
st.markdown("[Sarang Zanwar](https://github.com/Sarang-Zanwar)")


