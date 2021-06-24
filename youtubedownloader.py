from __future__ import unicode_literals, with_statement
import io
import eel
import youtube_dl

eel.init('web')


@eel.expose
def ytdownload(data):
    link = data
    ytd_options = {}
    with youtube_dl.YoutubeDL(ytd_options) as ytd:
        ytd.download([link])


eel.start('index.html', size=(1000, 600))
