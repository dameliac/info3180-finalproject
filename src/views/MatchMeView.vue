<template>
  <div>
    <div v-for="profile in userProfiles" :key="profile.id" class="mb-4 border p-4 rounded-xl">
      <h2 class="text-lg font-bold">{{ profile.name }}</h2>
      <button
        class="bg-green-600 text-white px-4 py-2 rounded-lg mt-2 hover:bg-green-700"
        @click="fetchMatches(profile.id)"
      >
        Match Me
      </button>
    </div>

    <div v-if="matches.length">
      <h3 class="text-xl font-semibold mt-6 mb-2">Matching Profiles</h3>
      <div v-for="match in matches" :key="match.profile_id" class="border p-3 rounded-xl bg-gray-100 mb-2">
        <img :src="match.photo" alt="Profile Pic" class="w-24 h-24 rounded-full object-cover mb-2">
        <p><strong>Name:</strong> {{ match.name }}</p>
        <p><strong>Height:</strong> {{ match.height }}"</p>
        <p><strong>Favorite Cuisine:</strong> {{ match.fav_cuisine }}</p>
        <p><strong>Favorite Color:</strong> {{ match.fav_color }}</p>
        <p><strong>Favorite Subject:</strong> {{ match.fav_school_subject }}</p>
        <p><strong>Political:</strong> {{ match.political ? "Yes" : "No" }}</p>
        <p><strong>Religious:</strong> {{ match.religious ? "Yes" : "No" }}</p>
        <p><strong>Family Oriented:</strong> {{ match.family_oriented ? "Yes" : "No" }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProfileMatcher',
  props: {
    userProfiles: Array
  },
  data() {
    return {
      matches: []
    };
  },
  methods: {
    async fetchMatches(profileId) {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get(`/api/profiles/matches/${profileId}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.matches = response.data.matching_profiles;
      } catch (error) {
        console.error("Error fetching matches:", error.response?.data || error.message);
        alert("Failed to fetch matches.");
      }
    }
  }
};
</script>

<style scoped>
/* optional styling */
</style>
