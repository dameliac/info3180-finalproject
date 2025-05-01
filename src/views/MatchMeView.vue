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
div {
  background-color: #fff7f0; 
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(253, 186, 140, 0.4); 
}

.mb-4 {
  background-color: #ffe7db; 
  border: 1px solid #fcd5b5;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 6px rgba(253, 186, 140, 0.3);
}

.text-lg {
  color: #7c2d12; 
}

button {
  background-color: #fb923c;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.75rem;
  margin-top: 1rem;
  font-weight: bold;
  transition: background-color 0.3s ease;
  cursor: pointer;
}

button:hover {
  background-color: #f97316; 
}

.text-xl {
  color: #9a3412;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.bg-gray-100 {
  background-color: #ffe7db; 
}

img {
  width: 6rem;
  height: 6rem;
  object-fit: cover;
  border-radius: 9999px;
  margin-bottom: 0.75rem;
  border: 2px solid #fdba74;
}

p {
  color: #78350f;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}
</style>

