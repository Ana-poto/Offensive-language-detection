import io
import re
import praw


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\u0000-\uFFFF"  # emoticons
        u"\u021b"
        u"\u0103"
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.IGNORECASE)
    return regrex_pattern.sub(r'',text)

if __name__ == '__main__':
    my_client_id='bYYD6rUFvlYbXQ'
    my_client_secret='7Wm46fm-9wSfphKU0EJtPRcnB4Ce9w'
    my_user_agent='RedditColector'
    reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)
    # get 10 hot posts from the Romania subreddit
    hot_posts = reddit.subreddit('Romania').hot(limit=10)
    commentsRomania = reddit.subreddit('Romania').comments(limit=None)
    commentsIasi = reddit.subreddit('iasi').comments(limit=None)
    commentsBucuresti = reddit.subreddit('bucuresti').comments(limit=None)
    commentsTimisoara = reddit.subreddit('timisoara').comments(limit=None)
    with open("redditComments.txt", "w+", encoding="utf-8") as f:
        for comment in commentsRomania:
            #print(comment.body)
            comment.body = re.sub('http\S+', '', comment.body)
            comment.body = re.sub('www\S+', '', comment.body)
            comment.body = re.sub('Www\S+', '', comment.body)
            data = comment.body
            f.write(data)
            f.write("\n")
        for comment in commentsIasi:
            # print(comment.body)
            comment.body = re.sub('http\S+', '', comment.body)
            comment.body = re.sub('www\S+', '', comment.body)
            comment.body = re.sub('Www\S+', '', comment.body)
            data = comment.body
            f.write(data)
            f.write("\n")
        for comment in commentsIasi:
            # print(comment.body)
            comment.body = re.sub('http\S+', '', comment.body)
            comment.body = re.sub('www\S+', '', comment.body)
            comment.body = re.sub('Www\S+', '', comment.body)
            data = comment.body
            f.write(data)
            f.write("\n")
        for comment in commentsTimisoara:
            # print(comment.body)
            comment.body = re.sub('http\S+', '', comment.body)
            comment.body = re.sub('www\S+', '', comment.body)
            comment.body = re.sub('Www\S+', '', comment.body)
            data = comment.body
            f.write(data)
            f.write("\n")
    f.close()



