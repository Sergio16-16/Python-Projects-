from googleapiclient.discovery import build

def search_youtube_videos(api_key, query, max_results=11):
    # Constrói o serviço da API do YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Executa a busca na API do YouTube
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results
    ).execute()

    # Processa os resultados da busca
    videos = []
    for item in search_response.get('items', []):
        if item['id']['kind'] == 'youtube#video':
            video_data = {
                'title': item['snippet']['title'],
                'videoId': item['id']['videoId'],
            }
            videos.append(video_data)
    
    return videos

api_key = 'AIzaSyDEhAHFF9FgAC3WB4aeau0wJ9QXmqmCDfw'
query = 'Brino' 

videos = search_youtube_videos(api_key, query)
for idx, video in enumerate(videos):
    print(f"{idx + 1}. {video['title']}\n   https://www.youtube.com/watch?v={video['videoId']}\n   ")
