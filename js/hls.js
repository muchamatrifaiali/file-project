<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/hls.js/1.1.1/hls.min.js"></script>
    <script type="text/javascript" src="https://cdn.gumlytics.com/insights/1.1/gumlet-insights.min.js"></script>
  </head>
  <body>
    <h1>Gumlet Insights SDK</h1>
    <div id="player" style="width: 400px"></div>
    <video id="my-video" preload="true" width="640" height="264" controls></video>
    <script type="text/javascript">

      var video = document.getElementById('my-video');
      var time = new Date().getTime();
      var hls = new Hls({
        // disable preload
        autoStartLoad: false
      });

      hls.attachMedia(video);
      hls.loadSource('https://b1news.beritasatumedia.com/Beritasatu/B1News_manifest.m3u8');

      video.addEventListener('play', function() {
        // needed when preload is disabled
        hls.startLoad();
      });

      // Create the Gumlet Configuration JSON
      var config = {
        property_id: 'TEST_PROPERTY', // required:  please replace with correct property id.
      };

      var analytics = gumlet.insights(config);

      analytics.registerHLSJSPlayer(hls, {starttime: time});

    </script>
  </body>
</html>
