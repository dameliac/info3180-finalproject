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
/* Container card for each profile */
.mb-4 {
  background-color: #fff7f0;
  border: 1px solid #fcd5ce;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 12px rgba(255, 183, 155, 0.2);
}

/* Title for each user profile */
h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #7f5539;
}

/* Match Me button styling */
button {
  background-color: #ff9770;
  color: white;
  padding: 0.5rem 1.25rem;
  border: none;
  border-radius: 0.75rem;
  margin-top: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #ff6f61;
}

/* Matching Profiles Section */
h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #6d4c41;
}

/* Match card */
.bg-gray-100 {
  background-color: #fff0e6;
  border: 1px solid #f9c5bd;
  padding: 1.25rem;
  border-radius: 1rem;
  box-shadow: 0 2px 6px rgba(255, 183, 155, 0.15);
}

/* Profile Image */
img {
  width: 6rem;
  height: 6rem;
  border-radius: 9999px;
  object-fit: cover;
  margin-bottom: 0.75rem;
  border: 2px solid #ffb4a2;
}

/* Paragraph text */
p {
  font-size: 0.95rem;
  color: #5e3c2c;
  margin-bottom: 0.4rem;
}

strong {
  color: #8c3f2c;
}
</style>

