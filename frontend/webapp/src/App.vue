<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <img src="./assets/logo.png" fluid/>
      <b-navbar-brand href="#">EyeCity</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-button right v-b-toggle.sidebar-1 variant="danger" class="mx-1">Press me!</b-button>
          <b-button right v-b-toggle.sidebar-2 variant="info" class="mx-1">Poznaj nas</b-button>
          <b-button v-b-modal.modal-stream variant="warning" class="mx-1">Stream</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <b-sidebar id="sidebar-1" title="Poszukiwany" shadow>
      <div class="px-3 py-2">
        <p>
          Żywy bądź martwy (choć lepiej żywy) Krzysiek. Zaginął po poznaniu pewnej damy.
          Teraz już nie ma czasu na swoich kolegów. Krzysiek wróć, tęsknimy!
          Dla znalazcy 5zł i paczka Cheetosów serowych.
        </p>
        <img src="./assets/Gal_wanted.png" fluid thumbnail />
      </div>
    </b-sidebar>
    <b-sidebar id="sidebar-2" title="Poznaj nas" shadow>
      <div class="px-3 py-2">
        <p> Cześć, jesteśmy FlowChain. Jeżeli chcesz nawiązać z nami kontakt, możesz skorzystać z linków poniżej</p>
        <p><b-button href="https://www.linkedin.com/in/patryk-wypych/" class="btn btn-primary" target="_blank">Patryk Wypych</b-button></p>
        <p><b-button href="https://www.linkedin.com/in/krzysztof-galus/" class="btn btn-primary" target="_blank">Krzysztof Galus</b-button></p>
        <p><b-button href="https://www.linkedin.com/in/jakub-olszewski-300616211/" class="btn btn-primary" target="_blank">Jakub Olszewski</b-button></p>
        <p><b-button href="https://www.linkedin.com/in/jakub-miara/" class="btn btn-primary" target="_blank">Jakub Miara</b-button></p>
        <p><b-button href="https://www.linkedin.com/in/micha%C5%82-nawarecki-718402227/" class="btn btn-primary" target="_blank">Michał Nawarecki</b-button></p>
      </div>
    </b-sidebar>
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
      <b-card v-if="items.length === 0">
        <b-container class="bv-example-row">
          <b-row>
            <b-col><b-spinner></b-spinner></b-col>
            <b-col><b-spinner></b-spinner></b-col>
            <b-col><b-spinner></b-spinner></b-col>
            <b-col><b-spinner></b-spinner></b-col>
          </b-row>
        </b-container>
      </b-card>
      <div v-for="(item, index) in items" v-bind:key="index">
        <b-card v-if="item.image !== undefined">
          <b-container class="bv-example-row">
            <b-row>
              <b-col>{{ item.timestamp }}</b-col>
              <b-col>
                <b-img :src="getbaseimage(item.image)" fluid alt="cctv_image" height="100"></b-img>
                <p><b-button v-b-modal.modal-image class="btn btn-success" @click="setImage(getbaseimage(item.image))">Powiększ</b-button></p>
              </b-col>
              <b-col>
                <b-img :src="getbaseimage(item.face_image)" fluid alt="person_image" height="100"></b-img>
                <p><b-button v-b-modal.modal-image class="btn btn-success" @click="setImage(getbaseimage(item.face_image))">Powiększ</b-button></p>
              </b-col>
              <b-col>{{ item.name }}</b-col>
            </b-row>
          </b-container>
        </b-card>
      </div>
      </b-container>
    </div>
    <b-modal id="modal-image" title="Powiększone zdjęcie" size="xl" :image="image" ok-only ok-title="Close me">
      <template>
        <div class="Popup">
          <b-img :src="image" fluid alt="Responsive image"></b-img>
        </div>
      </template>
    </b-modal>
    <b-modal id="modal-stream" title="Stream na żywo z kamery" size="xl" ok-only ok-title="Close me">
      <p class="my-4"><Stream/></p>
    </b-modal>
  </div>
</template>

<script>

import Stream from './components/ModalPopup.vue'

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
        items: []
    }
  },
  components: {
    Stream
  },

  created() {
  document.body.style.backgroundColor = '#4006A0'
  },
  methods: {
    setImage (img) {
      this.image = img
    },
    async getImagesData() {
      try {
        const response = await fetch("http://localhost:8000/get_images");
        const data = await response.json();
        console.log(data)
        this.items = data;
      } catch (error) {
        console.error(error);
      }
    },
    getbaseimage (base) {
      return "data:image/png;base64, " + base
    }
  },
  mounted() {
    this.getImagesData()
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