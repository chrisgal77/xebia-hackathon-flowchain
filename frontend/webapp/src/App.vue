<template>
  <div>
    <div class="mt-2">
      <b-img
        src="https://cdn.discordapp.com/attachments/1015019631548825671/1021077756479545375/among_trolls.png"
        v-bind="mainProps"
        fluid
      />
    </div>
    <div class="mt-2">
      <b-container
        class="bv-example-row"
      >
        <b-row>
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
        </b-row>
      </b-container>
    </div>

    <div class="position-absolute bottom-0 start-50 translate-middle">
      <b-button v-b-modal.modal-2 class="btn btn-success">POPAAAAAP</b-button>
    </div>
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
      color: '#BA91FF'
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