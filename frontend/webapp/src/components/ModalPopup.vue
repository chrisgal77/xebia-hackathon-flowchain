<template>
  <div>
    <div class="container">
      <video
        ref="videoElement"
        class="video-js"
        preload="auto"
        data-setup='{}'
      ></video>
    </div>
  </div>
</template>

<script>
import videojs from 'video.js';
import '@videojs/http-streaming';

export default {
  mounted() {
    this.$nextTick(() => {
      const videoElement = this.$refs.videoElement;

      const player = videojs(videoElement, {
        controlBar: {
          playToggle: false,
        },
        userActions: {
          hotkeys: false,
          doubleClick: false,
          fullscreenToggle: false,
          contextMenu: false,
          externalTracks: false,
          keyboard: false,
          pictureInPicture: false,
          subtitlesButton: false,
        },
      });

      // Dodaj zdarzenie click do odtwarzacza wideo
      player.on('click', () => {
        player.play();
      });

      player.src({
        src: 'https://3bcc7697a17c.eu-central-1.playback.live-video.net/api/video/v1/eu-central-1.437790362083.channel.dnY029lLbZNG.m3u8',
        type: 'application/x-mpegURL',
      });

      player.play();
    });
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
}
</style>