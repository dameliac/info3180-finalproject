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
/* Optional Tailwind or custom styling */
</style>
