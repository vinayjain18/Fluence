import instaloader

def scrape_instagram_profile(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        profile_data = f"Here's my Instagram details:\nName: {profile.full_name} \nBio: {profile.biography}"
        return profile_data

    except Exception as e:
        print(f"An error occurred: {e}")


def download_latest_captions(username, num_posts=10):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Counter for the number of posts processed
        count = 0
        captions = ""

        # Iterate over the posts and get the latest ones
        for post in profile.get_posts():
            if count < num_posts:
                # Add the caption to the string with a line break after each post
                captions += f"Post {count + 1}, Published Date: {post.date}:\n{post.caption}\n\n"
                count += 1
            else:
                break

        return captions.strip()  # Remove any trailing whitespace

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


if __name__ == "__main__":
    username = "official_vadapav_girl"
    scrape_instagram_profile(username)
    download_latest_captions(username, 10)