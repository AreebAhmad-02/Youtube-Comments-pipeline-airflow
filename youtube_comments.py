# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import csv
import os
import googleapiclient.discovery
import pandas as pd


def run_yt_comments_pipeline():
    def process_comments(response_items):
            comments = []
            for comment in response_items:
                    author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                    comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
                    publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
                    comment_info = {'author': author, 
                            'comment': comment_text, 'published_at': publish_time}
                    comments.append(comment_info)
            # print(f'Finished processing {len(comments)} comments.')
            return comments



    def seek_data(videoId):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "" # secure the id from the gcp console
        comments_list = []

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        
        request = youtube.commentThreads().list(
            part="snippet, replies",
            videoId=videoId,
            
        )
        response = request.execute()
        comments_list.extend(process_comments(response['items']))

        while response.get('nextPageToken', None):
            request = youtube.commentThreads().list(
                part='id,replies,snippet',
                # youtube video id from which comments are to be extracted 
                videoId="q8q3OFFfY6c",
                pageToken=response['nextPageToken']
            )
            response = request.execute()

            comments_list.extend(process_comments(response['items']))

        

        print(comments_list)
        return comments_list


    # Save the results in a CSV file
    def save_to_csv(comments, filename="comments.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['author', 'comment', 'published_at']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for comment in comments:
                writer.writerow(comment)

    response = seek_data(videoId="q8q3OFFfY6c")
    df = pd.DataFrame(response)
    df.to_csv("s3://airflowyt/yt_comments.csv")

    # processed_comments = process_comments(response["items"])
run_yt_comments_pipeline()

