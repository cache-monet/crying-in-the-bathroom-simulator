import youtube_dl
from pysndfx import AudioEffectsChain

class MusicProcessor:
  def __init__(self, outdir):
    self.outdir =  outdir
    self.ydl = youtube_dl.YoutubeDL({
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '128',
      }],
      'outtmpl': '{}/%(id)s_source.%(ext)s'.format(self.outdir),
    })

    self.fx = (
      AudioEffectsChain()
      .lowshelf(gain=-8.0, frequency=512)
      .lowpass(frequency=1000)
      .highshelf(frequency=2000)
      .reverb()
    )

  def process(self, url: str):
    info_dict = self.ydl.extract_info(url, download=True)
    fid = info_dict.get('id')
    src = "{}/{}_source.mp3".format(self.outdir, fid)
    dst = "{}/{}.mp3".format(self.outdir, fid)
    self.fx(src, dst)
    return dst, "{}.mp3".format(fid)
