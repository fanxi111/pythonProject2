from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = '523532'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        client_ip = request.remote_addr
        print(f"Client IP: {client_ip}")
        artist_name = request.form['artist']
        albums = search_albums(artist_name)
        return render_template('results.html', artist=artist_name, albums=albums)
    return render_template('index.html')


def search_albums(artist_name):
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    data = response.json()
    if 'album' in data:
        albums = data['album']
    else:
        albums = []
    return albums


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
