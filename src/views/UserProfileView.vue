<script setup>
    import { getUserIdFromToken } from "@/utils/authUtils.js";
    import { ref, onMounted } from 'vue';

    const token = localStorage.getItem('token');
    const userId = getUserIdFromToken();

    const userProfile = ref({});
    const favourites = ref([]);
    const profiles = ref([]);
    const matchedProfiles = ref([]);
    const userMap = ref({}); // Map user_id to user info


    console.log(userId);

    // Fetch user details
    function fetchUser() {
    fetch(`/api/users/${userId}`, {
        headers: {
        'Authorization': `Bearer ${token}`
        }
    })
        .then((response) => response.json())
        .then((data) => {
        console.log('User found:', data);
        userProfile.value = data;
        })
        .catch((error) => {
        console.error('Error fetching user:', error);
        });
    }

    // Fetch favourite users
    function fetchFavourites() {
    fetch(`/api/users/${userId}/favourites`, {
        method: 'GET',
        headers: {
        'Authorization': `Bearer ${token}`
        }
    })
        .then((response) => response.json())
        .then((data) => {
        favourites.value = data;
        matchFavouritesToProfiles();
        console.log('Favourites are:', data);
        })
        .catch((error) => {
        console.error('Error fetching favourites:', error);
        });
    }

    // Fetch all user profiles
    function fetchProfiles() {
    fetch("/api/profiles", { method: 'GET', headers:{'Authorization':`Bearer ${token}`} })
        .then((response) => response.json())
        .then((data) => {
        profiles.value = data;
        matchFavouritesToProfiles();
        })
        .catch((error) => {
        console.error("Error fetching profiles:", error);
        });
    }

    // Match favourites to full profiles
    // function matchFavouritesToProfiles() {
    //     if (!favourites.value.length || !profiles.value.length) return;

    //     matchedProfiles.value = profiles.value.filter(profile =>favourites.value.includes(profile.user_id_fk));
    //     console.log(matchedProfiles.value)
    // }

    async function fetchUserById(userId) {
        if (userMap.value[userId]) return; // already fetched

        try {
            const res = await fetch(`/api/users/${userId}`, {method:'GET', headers:{'Authorization':`Bearer ${token}`}});
            const data = await res.json();
            userMap.value[userId] = data;
        } catch (err) {
            console.error(`Error fetching user ${userId}`, err);
        }
    }

    async function matchFavouritesToProfiles() {
        if (!favourites.value.length || !profiles.value.length) return;

        matchedProfiles.value = profiles.value.filter(profile =>
            favourites.value.includes(profile.user_id_fk)
        );

        // Fetch usernames for each matched profile
        await Promise.all(
            matchedProfiles.value.map(p => fetchUserById(p.user_id_fk))
        );
    };


    onMounted(() => {
    fetchUser();
    fetchFavourites();
    fetchProfiles();
    });
</script>


<template>
    <div class="max-w-3xl mx-auto mt-10 p-6 bg-white shadow rounded-lg">
      <h2 class="text-2xl font-bold mb-4">My Profile</h2>
      <router-link to="/profiles/new">Create Profile</router-link>
  
      <div v-if="matchedProfiles.length" class="mt-6">
        <p><strong>Username:</strong> {{ userProfile.username }}</p>
        <p><strong>Email:</strong> {{ userProfile.email }}</p>
  
          <h3 class="text-xl font-semibold mb-2">Favourited Users</h3>
          <section v-for="fav in matchedProfiles" :key="fav.id" class="mb-4">
                <img src="/src/assets/image.png" alt="Profile photo" class="w-6 h-6 rounded-full mb-2" />
                <p class="font-semibold text-lg">
                    Name: {{ userMap[fav.user_id_fk]?.username || 'Unknown User' }}
                </p>
                <p>
                    Date joined: {{ userMap[fav.user_id_fk]?.date_joined }}
                </p>
                <p><strong>Biography:</strong> {{ fav.biography }}</p>
            </section>
        </div>
        <div v-else class="mt-6 text-gray-600">
          You haven't favourited any users yet.
        </div>
      </div>
    
</template>
  
  
<style scoped>
    div {
        background-color: #fff7f0; /* Creamy peach background */
        border-radius: 0.75rem;
        box-shadow: 0 4px 12px rgba(253, 186, 140, 0.4); /* Soft peachy shadow */
        padding: 1.75rem;
    }
    
    /* Main heading */
    h2 {
        font-size: 1.75rem; /* slightly bigger */
        font-weight: 700;
        margin-bottom: 1rem;
        color: #7c2d12; /* Warm deep brown */
    }
    
    /* Sub-heading */
    h3 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        color: #9a3412; /* Rich warm tone */
    }
    
    /* Paragraphs */
    p {
        margin-bottom: 0.75rem;
        font-size: 1rem;
        color: #78350f; /* Rich brown */
    }
    
    /* Lists */
    ul {
        list-style-type: disc;
        padding-left: 1.5rem;
        color: #78350f; /* Match paragraph text */
    }
    
    /* List items */
    li {
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    /* Lighter text (no favourites message) */
    .text-gray-600 {
        color: #a16207; /* Warm golden brown */
        font-size: 0.95rem;
        font-style: italic;
    }
</style>
  
