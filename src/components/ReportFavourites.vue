<script setup>
import { getUserIdFromToken } from "@/utils/authUtils.js";
import { ref, onMounted } from 'vue';

const token = localStorage.getItem('token');
const userId = getUserIdFromToken();

const userMap = ref({});
const profiles = ref([]);
const favourites = ref([]);
const topReports = ref([]);
const matchedFavourites = ref([]);
const topProfiles = ref([]);

async function fetchUserById(id) {
  if (userMap.value[id]) return; // Already fetched
  try {
    const res = await fetch(`/api/users/${id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    userMap.value[id] = data;
  } catch (error) {
    console.error(`Error fetching user ${id}:`, error);
  }
}

async function fetchProfiles() {
  try {
    const res = await fetch('/api/profiles', {
      headers: { Authorization: `Bearer ${token}` },
    });
    profiles.value = await res.json();
  } catch (error) {
    console.error('Error fetching profiles:', error);
  }
}

async function fetchFavourites() {
  try {
    const res = await fetch(`/api/users/${userId}/favourites`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    favourites.value = await res.json();
  } catch (error) {
    console.error('Error fetching favourites:', error);
    console.log(userId)
  }
}

async function fetchTopFavourites() {
  try {
    const res = await fetch('/api/users/favourites/20', {
      headers: { Authorization: `Bearer ${token}` },
    });
    topReports.value = await res.json();
  } catch (error) {
    console.error('Error fetching top 20 favourites:', error);
  }
}


async function processData() {
  // Match user's favourites
  matchedFavourites.value = profiles.value.filter(profile =>
    favourites.value.includes(profile.user_id_fk)
  );

  // Match top favourites
  const topUserIds = topReports.value.map(r => r.user_id);
  topProfiles.value = profiles.value.filter(profile =>
    topUserIds.includes(profile.user_id_fk)
  );

  const uniqueUserIds = [
    ...new Set([
      ...favourites.value,
      ...topReports.value.map(r => r.user_id),
    ]),
  ];
  await Promise.all(uniqueUserIds.map(fetchUserById));
}

onMounted(async () => {
  await Promise.all([
    fetchProfiles(),
    fetchFavourites(),
    fetchTopFavourites(),
  ]);
  await processData();
});
</script>

<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">Reports</h2>

    <!-- Favourited Users by Current User -->
    <section class="mb-10">
      <h3 class="text-xl font-semibold mb-4">Users You Have Favourited</h3>
      <div v-if="matchedFavourites.length">
        <section
          v-for="fav in matchedFavourites"
          :key="fav.id"
          class="mb-4 border-b pb-4"
        >
          <p><strong>Username:</strong> {{ userMap[fav.user_id_fk]?.username }}</p>
          <p><strong>Name:</strong> {{ userMap[fav.user_id_fk]?.name }}</p>
          <p><strong>Email:</strong> {{ userMap[fav.user_id_fk]?.email }}</p>

        </section>
      </div>
      <p v-else class="text-gray-600">You haven't favourited any users yet.</p>
    </section>

    <!-- Top 20 Most Favourited Users -->
    <section>
      <h3 class="text-xl font-semibold mb-4">Top 20 Most Favourited Users</h3>
      <div v-if="topProfiles.length">
        <section
          v-for="profile in topProfiles"
          :key="profile.id"
          class="mb-4 border-b pb-4"
        >
          <p><strong>Username:</strong> {{ userMap[profile.user_id_fk]?.username }}</p>
          <p><strong>Name:</strong> {{ userMap[profile.user_id_fk]?.name }}</p>
          <p><strong>Email:</strong> {{ userMap[profile.user_id_fk]?.email }}</p>
        
        </section>
      </div>
      <p v-else class="text-gray-600">No top users to display yet.</p>
    </section>
  </div>
</template>

<style scoped>
.report-container {
    max-width: 960px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.report-title {
    font-size: 2rem;
    font-weight: bold;
    color: #5a1a01;
    margin-bottom: 1.5rem;
    text-align: center;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #7c2d12;
    margin-bottom: 1rem;
    border-bottom: 2px solid #facc15;
    padding-bottom: 0.5rem;
}

.user-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    border-radius: 0.75rem;
    box-shadow: 0 4px 10px rgba(253, 186, 140, 0.2);
    margin-bottom: 1rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.user-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(253, 186, 140, 0.3);
}

.user-avatar {
    width: 48px;
    height: 48px;
    border-radius: 9999px;
    background-color: #fde68a;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.25rem;
    color: #78350f;
}

.user-info p {
    margin: 0.25rem 0;
    font-size: 1rem;
    color: #78350f;
}

.empty-message {
    font-style: italic;
    color: #a16207;
    text-align: center;
    margin-top: 2rem;
}

</style>
