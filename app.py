import streamlit as st

st.set_page_config("Fluence",
                   menu_items={
                       'Get Help': 'https://www.extremelycoolapp.com/help',
                       'Report a bug': "https://www.extremelycoolapp.com/bug",
                       'About': "### Fluence: It is your copilot for helping you generate ideas and\
                                    refine it as per your niche and industry."
                   })

st.header('_Fluence_: Idea Generating Machine', divider="rainbow")
st.write("Fluence is your copilot for helping you generate ideas and\
            refine it as per your niche and industry. Currently, I have only \
            built the UI for this app. I'm working on the backend logic \
            and will update you soon. Thank you☺️")
st.write()

with st.form("my_form"):
    industry = st.text_input('Industry Name', placeholder='Eg: Fashion', key='industry')
    niche = st.text_input('Niche Name', placeholder='Eg: Beauty & Makeup', key='niche')
    account = st.text_input('Your Social Media handle URL', placeholder='Eg: https://www.instagram.com/username', key='account')
    submit = st.form_submit_button('Submit')


if submit:
    st.markdown("**Submitted**🎉, here are the details:")
    st.write("Your Industry:", industry)
    st.write("Your Niche:", niche)
    st.write("Your Social Media Handle URL:", account)
