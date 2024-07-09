# Fluence: Idea Generating Machine

Fluence is your copilot for helping you generate ideas for your Instagram as per your niche and industry. It is not your regular Chatgpt response which give general plan instead it create plan customized for your account.

## Tech Stack:
- Streamlit(for building web app)
- instaloader(for scraping IG profile and posts)
- OpenAI API

## Working:
- First, it takes the creator industry, niche and Instagram username
- Then, it scrape their instagram profile and extract their bio and latest 10 posts
- All this data along with the prompt is paas to the OpenAI API and return the output
- The output is in JSON format and user can download the content plan generated in text file

### You can access the app here - https://fluence.streamlit.app/