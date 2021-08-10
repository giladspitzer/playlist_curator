<template>
  <div class="mx-5">
    <div class="text-center" v-if="fetching">
      <b-spinner label="Spinning"></b-spinner>
      <b-spinner type="grow" label="Spinning"></b-spinner>
      <b-spinner variant="primary" label="Spinning"></b-spinner>
      <b-spinner variant="primary" type="grow" label="Spinning"></b-spinner>
      <b-spinner variant="success" label="Spinning"></b-spinner>
      <b-spinner variant="success" type="grow" label="Spinning"></b-spinner>
    </div>
    <div v-else>
      <b-row class="mb-2 p-0">
        <b-col md="9"/>
        <b-col md="3" class="p-0">
          <b-form-input placeholder="search for a playlist"  v-model="searchText" type="search" @input="filter_playlists"/>
        </b-col>
      </b-row>
      <div v-if="filtered_playlists.length > 0">
        <div v-for="playlists in groupedPlaylists(this.filtered_playlists)" class="row mb-2" :key="playlists[0].id">
        <b-card-group deck  columns="3">
          <b-card v-for="playlist in playlists" :key="playlist.id" @click="openPlaylist(playlist.id)">
            <b-row no-gutters>
              <b-col md="12">
                <b-card-img :src="playlist.img" alt="Image" class="rounded-0"></b-card-img>
              </b-col>
            </b-row>
            <b-row no-gutters>
              <b-col md="12">
                <b-card-body :title="playlist.name">
                  <b-card-sub-title>
                    <font-awesome-icon icon="user-astronaut"/>
                    {{playlist.owner.name}}
                  </b-card-sub-title>
    <!--              <b-card-text>-->
    <!--                {{playlist.description}}-->
    <!--              </b-card-text>-->
                </b-card-body>
              </b-col>
            </b-row>
            <b-row no-gutters>
              <b-col md="1"/>
              <b-col md="3">
                <font-awesome-icon icon="globe"/>
              </b-col>
              <b-col md="3">
                <font-awesome-icon icon="music"/>
                {{playlist.tracks_total}}
              </b-col>
              <b-col md="3">
                <font-awesome-icon icon="users"/>
              </b-col>
              <b-col md="1"/>
            </b-row>
          </b-card>
        </b-card-group>
        </div>
      </div>
      <div v-else>
        No Results
      </div>
    </div>
  </div>
</template>

<script>
import {getPlaylists} from '@/api/api'
import {chunk} from "@/utils/utils";
export default {
  name: 'Playlists',
  data() {
    return {
      searchText: '',
      fetching: true,
      playlists: [],
      filtered_playlists: [],
      fields: [
        'id', 'name'
      ]
    }
  },
  computed: {
  },
  mounted() {
    this.fetching = true
    getPlaylists()
    .then(results => {
      this.playlists = results.data
      this.filtered_playlists = results.data
      this.fetching = false
    })
    .then(() => console.warn(this.playlists))
  },
  methods: {
    groupedPlaylists(playlists) {
      return chunk(playlists, 5)
    },
    filter_playlists(){
      this.fetching = true
      this.filtered_playlists = this.playlists.filter((e) => {
          return e.name.toLowerCase().includes(this.searchText.toLowerCase()) || e.owner.name.toLowerCase().includes(this.searchText.toLowerCase())
      })
      this.fetching = false
    },
    openPlaylist(playlistId){
      console.warn(playlistId)
    }
  }
}
</script>

<style scoped>
.card:hover{
  cursor: auto;
}
</style>
