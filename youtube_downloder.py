from pytube import YouTube
print("-----------------------------------")
print("    YOUTUBE MEDIA DOWNLOADER       ")
print("    code by: DennisGabriel-Dev     ")
print("-----------------------------------")

link = input("Enter the video link to download: ")

yt = YouTube(link)

print("Title : "+ yt.title)
print("Author : "+yt.author)



resolution_yt_max = yt.streams.get_highest_resolution()

resolution_yt_max.download()