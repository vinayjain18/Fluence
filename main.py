import os
from IG_Scrapper import scrape_instagram_profile, download_latest_captions

def generate_response(openai_api_key,ig_username, industry, niche, extra, week):
    try:
        print("Calling----------------------------------------------------------------------------")

        # to scrape instagram bio
        ig_bio = scrape_instagram_profile(ig_username)
        # to scrape latest captions of posts from Instagram user
        ig_captions = download_latest_captions(ig_username)

        chat_prompt = (f"Act as a social media marketer with 10 years of experience.\
        I want you to generate a {week} content plan for Instagram that includes 1 reel and 1 post daily.\
        Give me detailed content idea plan for each reel and post for the day and not just the heading. \
        Use their latest posts caption data to learn about what kind of content these user upload on its Instagram page and based on it generate content ideas and plan.\
        Here are some details of my Instagram account: {ig_bio}.The industry of the creator: {industry} \
        and niche is {niche} and some extra information - {extra}. Also here are the latest 10 post captions \
        of this instagram page. You can understand from these captions how and which type of content, \
        this instagram page mostly put on. Saying it again, To understand their Instagram page better, \
        understand the type of content from the latest posts. Latest 10 post(including reels) captions - {ig_captions}. Make \
        sure that the output is in JSON format only with day as key and content idea as value. And dont print anything else")

        from openai import OpenAI
        from dotenv import load_dotenv
        import streamlit as st
        load_dotenv()

        # client = OpenAI(api_key=openai_api_key) # your openai api key
        client = OpenAI(api_key=openai_api_key)

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chat_prompt}
            ]
        )

        resp = completion.choices[0].message.content

        # if os.path.exists("content_planner.txt"):
        #     os.remove("content_planner.txt")
        #
        # with open("content_planner.txt", "w", encoding="utf-8") as f:
        #     f.write(resp)

        print(resp)
        print("Content plan generated..............................................................")
        return resp

    except Exception as e:
        return f"Couldn't generate response due to following error: {e}"

if __name__ == "__main__":
    ig_username = "narendramodi"
    generate_response(os.getenv("OPENAI_API_KEY"), ig_username, "industry", "niche", "extra", "1 week")