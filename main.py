import os 
import streamlit as st
from groq import Groq

def groq_completion(user_content):
    client = Groq(api_key = os.environ.get('GROQ_API_KEY'))
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "Act like a doctor and provide answers accordingly dont pretend like a Large Language model"
            },
            {
                "role": "user",
                "content": user_content
            }
        ],
        temperature=0.5,
        max_tokens=56400,
        top_p=1,
        stream=True,
        stop=None,
    )


    result = ''
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""
    return result

def main():
    st.title("Groq Instant Chat Application")
    user_content = st.text_input("Enter the Query")
    if st.button("Submit"):
        if not user_content:
            st.warning("Please enter something")
            return 
        st.info("Please wait processing your query .............")
        generated_text = groq_completion(user_content)
        st.success("Your Answer for the Query")
        st.text_area("",value = generated_text,height = 200)

if __name__ == "__main__":
    main()