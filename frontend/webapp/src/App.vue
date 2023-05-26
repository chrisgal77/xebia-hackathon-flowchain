<template>
  <div>
    <div class="mt-2">
    </div>
    <div class="mt-2">
      <b-container
        class="bv-example-row"
      >
      <!-- <b-table
        striped
        hover
        :items="items"
        :fields="fields"
      /> -->
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
        <b-card @click="v-b-modal.modal-2">
          <b-container class="bv-example-row">
            <b-row>
              <b-col>{{ item.datetime }}</b-col>
              <b-col><b-img :src="item.cctv_img" fluid alt="cctv_image" height="100"></b-img></b-col>
              <b-col><b-img :src="item.person_photo" fluid alt="person_image" height="100"></b-img></b-col>
              <b-col>{{ item.metadata }} <p><b-button v-b-modal.modal-2 class="btn btn-success">Więcej informacji</b-button></p></b-col>
            </b-row>
          </b-container>
        </b-card>
      </div>
        <!-- <b-row>
          <b-col cols="1"/>
          <b-col
            cols="10"
          >
            <b-card
              title="Podgląd"
              :img-src='url'
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mt-0"
            >
              <b-card-text>
                Wideo przedstawia działające detektory
              </b-card-text>

            </b-card>
          </b-col>
          <b-col cols="1"/>
        </b-row> -->
      </b-container>
    </div>

    <!-- <div class="position-absolute bottom-0 start-50 translate-middle">
      <b-button v-b-modal.modal-2 class="btn btn-success">POPAAAAAP</b-button>
    </div> -->
    <b-modal id="modal-2" title="Popup">
      <p class="my-4"><Popup/></p>
    </b-modal>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Popup from './components/ModalPopup.vue'


export default {
  name: 'App',
  data() {
    return{
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
    Popup
  },
  created() {
  document.body.style.backgroundColor = '#BA91FF'
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