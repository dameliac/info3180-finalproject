<template>
    <div class="p-6">
      <h1 class="text-2xl font-bold mb-4">Your Matches</h1>
  
      <div v-if="loading" class="text-gray-600">Loading matches...</div>
      <div v-else-if="error" class="text-red-600">{{ error }}</div>
      <div v-else-if="matches.length === 0" class="text-gray-600">No matches found.</div>
  
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <div
          v-for="match in matches"
          :key="match.profile_id"
          class="border p-4 rounded-xl shadow hover:shadow-md transition bg-white"
        >
          <img :src="match.photo" alt="Profile photo" class="w-full h-40 object-cover rounded-md mb-3" />
          <h2 class="text-lg font-semibold">{{ match.name }}</h2>
          <ul class="text-sm text-gray-700 mt-2 space-y-1">
            <li><strong>Birth Year:</strong> {{ match.birth_year }}</li>
            <li><strong>Height:</strong> {{ match.height }} cm</li>
            <li><strong>Cuisine:</strong> {{ match.fav_cuisine }}</li>
            <li><strong>Color:</strong> {{ match.fav_color }}</li>
            <li><strong>Subject:</strong> {{ match.fav_school_subject }}</li>
            <li><strong>Political:</strong> {{ match.political }}</li>
            <li><strong>Religious:</strong> {{ match.religious }}</li>
            <li><strong>Family-Oriented:</strong> {{ match.family_oriented }}</li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MatchMeView',
    props: {
      profileId: {
        type: Number,
        required: true,
      },
    },
    data() {
      return {
        matches: [],
        loading: true,
        error: null,
      };
    },
    mounted() {
      this.fetchMatches();
    },
    methods: {
      async fetchMatches() {
        this.loading = true;
        const token = localStorage.getItem('token'); // Or wherever your token is stored
  
        try {
          const response = await axios.get(`/api/profiles/matches/${this.profileId}`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
  
          this.matches = response.data.matching_profiles;
        } catch (error) {
          this.error = error.response?.data?.error || 'Something went wrong while fetching matches.';
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  