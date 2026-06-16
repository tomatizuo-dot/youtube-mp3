from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    title = ""
    channel = ""
    duration = ""
    thumbnail = ""
    url = ""

    if request.method == "POST":
        url = request.form["url"]

        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        title = info["title"]
        channel = info["uploader"]
        duration = info["duration"]
        thumbnail = info["thumbnail"]

    return render_template(
        "index.html",
        title=title,
        channel=channel,
        duration=duration,
        thumbnail=thumbnail,
        url=url
    )

@app.route("/download", methods=["POST"])
def download():
    return 
