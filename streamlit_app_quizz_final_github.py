# gpt3 quiz generator by Belghini - version July 2023


import os
import openai
import streamlit as st


# Connect to OpenAI GPT-3, fetch API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

#or enter the api key here
#openai.api_key = "........"

Model= "text-davinci-003"


def gen_Quiz(nb_questions, subject):

    response = openai.Completion.create(
        engine=Model,
        prompt=f"Write {nb_questions} question Multiple choice quiz for the subject: {subject}.",
        temperature=0.8,
        max_tokens=4000,
        top_p=0.8,
        best_of=2,
        frequency_penalty=0.0,
        presence_penalty=0.0)

    return response.get("choices")[0]['text']


def main_gpt_quiz_generator():

    st.markdown('Generate Quiz questionsrelated to a topic - powered by OpenAI using text-davinci-003 Model:sun_with_face:')
    st.write('\n')  # add spacing

    st.subheader('\nWhat is your Quiz is about?\n')

    quiz_text = ""  # initialize columns variables
    col1, space, col2, space, col3 = st.columns([10, 0.5, 5, 0.5, 5])
    with col1:
        input_topic = st.text_input('Tape a topic')
    with col2:
        input_number = st.text_input('number of questions')
    with col3:
        st.write("\n")
        st.write("\n")
        if st.button('Generate Quiz'):
            with st.spinner():
                quiz_text = gen_Quiz(input_number, input_topic)
    if quiz_text != "":
        st.write('\n')  # add spacing
        with st.expander("SECTION - Quiz Questions", expanded=True):
            st.markdown(quiz_text)  #output the results


if __name__ == '__main__':
    main_gpt_quiz_generator()
