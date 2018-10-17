import os

for name in '''
    _modules
    examples
    api
'''.strip().split():
    try:
        os.makedirs(name)
    except OSError:
        pass

for name in '''
    index.html
    changelog.html
    about.html
    _modules/index.html
    _modules/av.html
    license.html
    py-modindex.html
    hacking.html
    contributors.html
    examples/_index.html
    examples/generating_from_numpy.html
    includes.html
    genindex.html
    api/toplevel.html
    api/audio.html
    api/_index.html
    api/frame.html
    api/video.html
    api/utils.html
    api/container.html
    api/stream.html
    api/packet.html
    api/buffer.html
    api/codec.html
    api/plane.html
    api/subtitles.html
    api/filter.html
    search.html
    installation.html
'''.strip().split():
    with open(name, 'w') as fh:
        fh.write('''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Redirecting...</title>
  <link rel="canonical" href="{url}"/>
  <meta http-equiv="refresh" content="0;url={url}" />
</head>
<body>
  <h1>Redirecting...</h1>
  <a href="{url}">Click here if you are not redirected.<a>
  <script>location='{url}'</script>
</body>
</html>
'''.format(url='https://docs.mikeboers.com/pyav/{}'.format(name)))
