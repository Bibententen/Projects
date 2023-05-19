import time

def merge_sort(tweets):
    if len(tweets) <= 1:
        return tweets

    # Divide the list in half
    mid = len(tweets) // 2
    left_half = tweets[:mid]
    right_half = tweets[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i]['id'] < right_half[j]['id']:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged += left_half[i:]
    merged += right_half[j:]

    return merged


# Read tweets from file
with open('task4.txt', 'r') as f:
    tweets = []
    for line in f:
        id, text = line.strip().split(',')
        tweets.append({'id': int(id), 'text': text})

# Sort tweets by ID using Merge Sort
start_time = time.time()
sorted_tweets = merge_sort(tweets)
end_time = time.time()
running_time = end_time - start_time
# Write sorted tweets to file

with open('result4_2.txt', 'w') as f:
    running_time_str = 'Running time: ' + str(running_time) + ' seconds\n'
    f.write(running_time_str)
    for tweet in sorted_tweets:
        f.write(str(tweet) + '\n')
    