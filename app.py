import json
import streamlit as st
from main import generate_response

st.set_page_config("Fluence",
                   menu_items={
                       'About': "### Fluence: It is your copilot for helping you generate ideas and\
                                    refine it as per your niche and industry."
                   })

st.header('_Fluence_: Idea Generating Machine', divider="rainbow")
st.write("Fluence is your copilot for helping you generate ideas for your Instagram as per \
your niche and industry. Currently, it can help you generate 1 or 2 week of ideas at a time.")
st.write()


# Initialize session state variables
if 'is_generating' not in st.session_state:
    st.session_state.is_generating = False

def submit_callback():
    st.session_state.is_generating = True

with st.form("my_form"):
    industry = st.text_input('Industry Name', placeholder='Eg: Fashion', key='industry')
    niche = st.text_input('Niche Name', placeholder='Eg: Beauty & Makeup', key='niche')
    ig_username = st.text_input('Your Instagram Username', placeholder='Eg: narendramodi', key='account', help="Don't include '@' in username")
    extra = st.text_input('About yourself:', placeholder='Eg: I create content on beauty and fashion tips...', key='extra')
    week = st.selectbox(
        "How many week of content do you need to generate?",
        ("1 week", "2 week"))

    if st.session_state.is_generating:
        submit = st.form_submit_button('Submit', on_click=submit_callback, disabled=True)
    else:
        submit = st.form_submit_button('Submit', on_click=submit_callback)


if submit:
    st.markdown("**Submitted**, here are the details:")

    st.write("Your Instagram username:", ig_username)
    st.write()

    # Set the generating flag to True
    st.session_state.is_generating = True

    with st.spinner('Generating content(may take around 1 min)...'):
        response = generate_response(st.secrets["OPENAI_API_KEY"], ig_username, industry, niche, extra, week)

    if response.startswith("```json") and response.endswith("```"):
        response = response[7:-3]  # Remove the leading and trailing markdown code blocks

    # Set the generating flag to False
    st.session_state.is_generating = False

    try:
        # Display JSON response beautifully
        st.json(response)
    except Exception as e:
        st.error("Can't display the content, but you can simply download and see.")

    st.write("Content planner generated!🎉")

    # Provide a download button
    st.download_button(
        label="Download Content Planner",
        data=response,
        file_name='content_planer.txt',
        mime='text/plain'
    )
