<script setup>
    import fetchUser from "@/components/UserProfile.vue";
    import { ref, onMounted } from 'vue';
    
    let favourites = ref([]);
    const userID = ref('');
    let profiles = ref([]);
    let matchedProfiles = ref([]);
    

    // Lifecycle hook equivalent to mounted
    onMounted(() => {
      // logic to fetch user data
      fetchUser();
      userID = user.user_id;
      fetchFavourites();
      fetchProfiles();
    });


    function fetchFavourites(){
        fetch(`/api/users/${userID}/favourites`, {method:'GET'})
        .then((response) => response.json())
        .then((data)=>{
            favourites.value = data;
            MatchFavouritesToProfiles();
            console.log('Favourites are: ',data);
        }) 
        .catch ((error)=>{
        console.log(error)
    });

    function fetchProfiles(){
        fetch("/api/profiles", {method:'GET'})
        .then((response)=> response.json())
        .then((data)=>{
            //returns the list of new profiles
            newProfiles.value = data.slice(-4).reverse()
            console.log("Favourite profile:", data.slice(-4).reverse());
            MatchFavouritesToProfiles();
        })
        .catch(error => {
            console.error("Error fetching profiles:", error);
            });
    };

}
function MatchFavouritesToProfiles() {
  if (!favourites.value.length || !profiles.value.length) return;

  matchedProfiles.value = profiles.value.filter(profile =>
    favourites.value.some(fav => fav.user_id === profile.user_id_fk)
  );
}
</script>

<template>
    <div class="max-w-3xl mx-auto mt-10 p-6 bg-white shadow rounded-lg">
      <h2 class="text-2xl font-bold mb-4">My Profile</h2>
      
        <div>
            <p><strong>Username:</strong> {{ user.username }}</p>
            <p><strong>Email:</strong> {{ user.email }}</p>
  
            <div v-if="favourites.length" class="mt-6">
                <h3 class="text-xl font-semibold mb-2">Favourited Users</h3>
                <ul class="list-disc pl-5 space-y-1">
                    <li v-for="fav in favourites" :key="id">
                    {{ fav.username }} ({{ fav.email }})
                    </li>
                </ul>
            </div>
        <div v-else class="mt-6 text-gray-600">You haven't favourited any users yet.</div>
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
  
