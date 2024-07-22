import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import instaloader

load_dotenv()

async def scrape_instagram_profile(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        return f"Here's my Instagram details:\nName: {profile.full_name} \nBio: {profile.biography}"
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

async def download_latest_captions(username, num_posts=10):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        captions = []
        for i, post in enumerate(profile.get_posts()):
            if i >= num_posts:
                break
            captions.append(f"Post {i + 1}, Published Date: {post.date}:\n{post.caption}\n")
        return "\n".join(captions)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

async def generate_response(ig_username, industry, niche, extra, week):
    try:
        print("Calling----------------------------------------------------------------------------")
        
        # Run Instagram scraping functions concurrently
        ig_bio, ig_captions = await asyncio.gather(
            scrape_instagram_profile(ig_username),
            download_latest_captions(ig_username)
        )

        chat_prompt = f"""Act as a social media marketer with 10 years of experience.
        I want you to generate a {week} content plan for Instagram that includes 1 reel and 1 post daily.
        Give me detailed content idea plan for each reel and post for the day and not just the heading. 
        Use their latest posts caption data to learn about what kind of content these user upload on its 
        Instagram page and based on it generate content ideas and plan.
        Here are some details of my Instagram account: {ig_bio}.The industry of the creator: {industry} 
        and niche is {niche} and some extra information - {extra}. Also here are the latest 10 post captions 
        of this instagram page. You can understand from these captions how and which type of content, 
        this instagram page mostly put on. Saying it again, To understand their Instagram page better, 
        understand the type of content from the latest posts. Latest 10 post(including reels) captions - {ig_captions}. Make 
        sure that the output is in HTML format only. Also dont mention the real world date and time, just put Day 1, Day2 and
        so on. And dont print anything else"""

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a social media marketer with expertise of creating content plan for Instagram users."},
                {"role": "user", "content": chat_prompt}
            ]
        )

        resp = completion.choices[0].message.content
        print("Content plan generated.....................................................................")
        return resp

    except Exception as e:
        return f"Couldn't generate response due to following error: {e}\nTry again after few minutes"


if __name__ == "__main__":
    ig_username = "narendramodi"
    result = asyncio.run(generate_response(ig_username, "industry", "niche", "extra", "1 week"))
    print(result)