import os 
from flask import Flask, render_template_string, request

app = Flask(__name__)
posts = []

HTML = """
        <!DOCTYPE html>
<html>
<body style="font-family: sans-serif; max-width: 600px; margin: 2rem auto; padding: 1rem;">
    <h1>Auditory MVP</h1>
    <form method="POST">
        <input name="song" placeholder="Song" required style="width: 100%; margin-bottom: 10px; padding: 5px;">
        <input name="artist" placeholder="Artist" required style="width: 100%; margin-bottom: 10px; padding: 5px;">
        <button type="submit">Post Song</button>
    </form>
    <hr>
    <h3>Feed</h3>
    {% for post in posts %}
        <div style="border: 1px solid #ddd; padding: 10px; margin-top: 10px;">
            <strong>{{ post.song }}</strong> by {{ post.artist }}
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        posts.insert(0, {'song': request.form.get('song'),'artist': request.form.get('artist')})
    return render_template_string(HTML, posts=posts)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)