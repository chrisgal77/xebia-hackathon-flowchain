<template>
    <div class="Popup">
      <b-table
        striped
        hover
        :items="items"
        :fields="fields"
      />
    </div>
  </template>
  
  <script>
  export default {
    name: 'PopupModal',
    props: {
      msg: String
    },
    data() {
      return {
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
        ]
      }
    },

  }
  </script>
  
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  