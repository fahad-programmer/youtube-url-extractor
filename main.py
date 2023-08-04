import yt_dlp
from concurrent.futures import ThreadPoolExecutor


def get_stream_url(video_url):
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info['url']


def process_urls(input_file, output_file, num_threads):
    with open(input_file, 'r') as file:
        video_urls = file.read().splitlines()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use a list comprehension to create a list of futures for each URL
        futures = [executor.submit(get_stream_url, url) for url in video_urls]

        # Gather the results of each future
        stream_urls = [future.result() for future in futures]

    with open(output_file, 'w') as file:
        file.write(','.join(stream_urls))


if __name__ == "__main__":
    input_file = 'input.txt'  # Replace with the path to your input file
    output_file = 'output.txt'  # Replace with the path to your output file
    num_threads = 50  # Replace with the number of threads you want to use

    process_urls(input_file, output_file, num_threads)
