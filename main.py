import os
from meta_ai_api import MetaAI
from IG_Scrapper import scrape_instagram_profile, download_latest_captions

def generate_response(ig_username, industry, niche, extra, week):
    print("Calling.....................................")
    ai = MetaAI()

    # to scrape instagram bio
    ig_bio = scrape_instagram_profile(ig_username) #official_vadapav_girl
    # to scrape latest cpations of posts from Instagram user
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

    resp = ai.prompt(message=chat_prompt)["message"]

    if os.path.exists("content_planner.txt"):
        os.remove("content_planner.txt")

    with open("content_planner.txt", "w", encoding="utf-8") as f:
        f.write(resp)

    print(resp)
    print("Content plan generated...............................................")
    return resp

if __name__ == "__main__":
    ig_username = "official_vadapav_girl"
    generate_response(ig_username, "industry", "niche", "extra", "1 week")