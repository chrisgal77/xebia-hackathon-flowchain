<template>
  <div>
    <div class="mt-2">
    </div>
    <div class="mt-2">
      <b-container
        class="bv-example-row"
      >
      <b-card>
        <b-container class="bv-example-row">
          <b-row>
            <b-col><strong>Czas i data</strong></b-col>
            <b-col><strong>Zdjęcie z kamery</strong></b-col>
            <b-col><strong>Zdjęcie osoby</strong></b-col>
            <b-col><strong>Informacje</strong></b-col>
          </b-row>
        </b-container>
      </b-card>
      <div v-for="(item, index) in items" v-bind:key="index">
        <b-card>
          <b-container class="bv-example-row">
            <b-row>
              <b-col>{{ item.datetime }}</b-col>
              <b-col>
                <b-img :src="item.cctv_img" fluid alt="cctv_image" height="100"></b-img>
                <p><b-button v-b-modal.modal-2 class="btn btn-success" @click="setImage(item.cctv_img)">Powiększ</b-button></p>
              </b-col>
              <b-col>
                <b-img :src="item.person_photo" fluid alt="person_image" height="100"></b-img>
                <p><b-button v-b-modal.modal-2 class="btn btn-success" @click="setImage(item.person_photo)">Powiększ</b-button></p>
              </b-col>
              <b-col>{{ item.metadata }}</b-col>
            </b-row>
          </b-container>
        </b-card>
      </div>
      </b-container>
    </div>
    <b-modal id="modal-2" title="Powiększone zdjęcie" size="xl" :image="image" ok-only ok-title="Close me">
      <template>
        <div class="Popup">
          <b-img :src="image" fluid alt="Responsive image"></b-img>
        </div>
      </template>
    </b-modal>
  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return{
      image: '',
      url: 'http://localhost:5000/video',
      video: false,
      color: '#BA91FF',
      fields: [
          {
            key: 'datetime',
            label: 'Event Time'
          },
          {
            key: 'cctv_img',
            label: 'Surveilance Photo'
          },
          {
            key: 'person_photo',
            label: 'Person Found',
          },
          {
            key: 'metadata',
            label: 'Additional info'
          }
        ],
        items: [
          {'datetime': '21:52 26-05-2023', 'cctv_img': 'https://cdn.discordapp.com/attachments/1015019631548825671/1021077756479545375/among_trolls.png', 'person_photo': 'https://cdn.discordapp.com/attachments/1015019631548825671/1021077756479545375/among_trolls.png', 'metadata': 'Amogus Sus, 99%'},
          {'datetime': '21:52 26-05-2023', 'cctv_img': 'https://cdn.discordapp.com/attachments/1015019631548825671/1021077756479545375/among_trolls.png', 'person_photo': 'https://cdn.discordapp.com/attachments/1015019631548825671/1021077756479545375/among_trolls.png', 'metadata': 'Amogus Sus, 99%'}
        ]
    }
  },
  components: {
  },

  created() {
  document.body.style.backgroundColor = '#4006A0'
  },
  methods: {
    setImage (img) {
      this.image = img
    }
  }
}

</script>

<style lang="scss">

@import "../scss/main.scss";
@import "~bootstrap/scss/bootstrap.scss";
@import '~bootstrap-vue/dist/bootstrap-vue.css';

body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.card-outter {
  padding-bottom: 50px;
}
.card-actions {
  position: absolute;
  bottom: 0;
}
</style>

<!-- #AA81FA -->