<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Your Favourites</h2>

    <div v-if="loading" class="text-gray-500">Loading favourites...</div>
    <div v-else-if="favourites.length === 0" class="text-gray-500">No favourites found.</div>
    <div v-else class="grid gap-4 sm:grid-cols-2 md:grid-cols-3">
      <div v-for="fav in favouriteProfiles" :key="fav.id" class="border rounded-xl p-4 shadow bg-white">
        <h3 class="font-semibold text-lg">{{ fav.name }}</h3>
        <p class="text-sm text-gray-600">Username: {{ fav.username }}</p>
        <router-link :to="`/profiles/${fav.id}`" class="text-blue-500 text-sm hover:underline mt-2 block">View Profile</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Favourites",
  data() {
    return {
      favourites: [],
      favouriteProfiles: [],
      loading: true,
    };
  },
  async mounted() {
    const token = localStorage.getItem("token");
    const userId = localStorage.getItem("user_id"); // or however you store it

    try {
      // 1. Fetch favourite user IDs
      const res = await fetch(`/api/users/${userId}/favourites`);
      const favIds = await res.json();
      this.favourites = favIds;

      // 2. Fetch user info for each favourite
      const profilePromises = favIds.map(async (id) => {
        const res = await fetch(`/api/users/${id}`);
        return await res.json();
      });

      this.favouriteProfiles = await Promise.all(profilePromises);
    } catch (error) {
      console.error("Failed to load favourites:", error);
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
.p-4 {
  background-color: #fff7f0; /* Soft peachy background */
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(253, 186, 140, 0.4); /* Peachy glow */
}

h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #7c2d12; /* Deep warm brown */
  margin-bottom: 1.5rem;
}

h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #9a3412; /* Warm cocoa brown */
  margin-bottom: 0.5rem;
}

.text-gray-500 {
  color: #a16207; /* Softer muted golden peach tone */
  font-style: italic;
}

.grid {
  gap: 1.5rem;
}

.border {
  background-color: #ffe7db; /* Light peach card background */
  border: 1px solid #fcd5b5;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 8px rgba(253, 186, 140, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.border:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(253, 186, 140, 0.5);
}

.text-sm {
  font-size: 0.95rem;
  color: #78350f;
}

.text-blue-500 {
  color: #fb923c; /* Peach instead of default blue */
}

.text-blue-500:hover {
  text-decoration: underline;
  color: #f97316;
}

a {
  margin-top: 0.5rem;
  display: inline-block;
}
</style>

