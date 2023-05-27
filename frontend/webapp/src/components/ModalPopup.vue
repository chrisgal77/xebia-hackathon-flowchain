<template>
  <video ref="video" width="100%" height="640" controls></video>
</template>

<script>
import Hls from 'hls.js';

export default {
  mounted() {
    let hls = new Hls();
    let stream = "https://3bcc7697a17c.eu-central-1.playback.live-video.net/api/video/v1/eu-central-1.437790362083.channel.dnY029lLbZNG.m3u8";
    let video = this.$refs["video"];
    hls.loadSource(stream);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
      video.play();
    });
  },
};
</script>