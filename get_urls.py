import random
from googleapiclient.discovery import build

# Replace with your API key
API_KEY = "AIzaSyAy6S5giXu0G0VL-tpUaATpzrrIccYEoIk"


# Function to get random YouTube Shorts URLs based on topic and country
def get_random_shorts(topic, country, num_results=200):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for YouTube Shorts with the given topic and country
    search_response = youtube.search().list(
        q=topic,
        type='video',
        part='id',
        videoDuration='short',
        regionCode=country,
        maxResults=200  # Increase this number if you want more search results
    ).execute()

    # Extract video IDs from search results
    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

    # Shuffle the video IDs
    random.shuffle(video_ids)

    # Get the first num_results video IDs
    selected_video_ids = video_ids[:num_results]

    # Generate the YouTube Shorts URLs from the video IDs
    shorts_urls = [f"https://www.youtube.com/shorts/{video_id}" for video_id in selected_video_ids]

    return shorts_urls


if __name__ == "__main__":
    # Replace with your desired topic and country code
    topic = "comedy"
    country = "PK"  # Example: "US" for United States

    # Get random YouTube Shorts URLs
    random_shorts_urls = get_random_shorts(topic, country)

    # Print the result
    # Save the URLs to input.txt
    with open("input.txt", "w") as file:
        for url in random_shorts_urls:
            file.write(url + "\n")

    print("URLs saved to input.txt file.")
