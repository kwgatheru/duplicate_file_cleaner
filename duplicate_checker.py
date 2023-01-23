import collections

# Open the url_list.txt file and read the urls
with open("Tweet_URL.txt", "r") as f:
    urls = f.readlines()

# Use a dictionary to store the count of each url
url_counts = collections.Counter(urls)

# Open the duplicates.txt file to write the results
with open("duplicates.txt", "a") as f:
    # Write the duplicated urls and their count to the file
    for url, count in url_counts.items():
        if count > 1:
            f.write(f"{url}:{count}\n")
