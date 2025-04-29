<script setup>
//Part2 #4
import { ref, onMounted } from "vue";
 //reactive variables
const searchInput = ref('');
let profiles = ref([]);
let clicked = ref(false);
let newProfiles =ref([]);

 

//method to search profiles
function searchProfiles(){
  //store searchinput to searchfilters - allowing the query to search by name, birth year, sex and race at a time.
  const params = new URLSearchParams({
    name: searchInput.value,
    birth_year: searchInput.value,
    sex: searchInput.value,
    race: searchInput.value
  });

  //ajax request to flask api /api/search GET request
  fetch(`/api/search?${params.toString()}`, {method: 'GET', headers:{'Accept':'application/json'}})
  .then ((response) => response.json())
  .then((data)=> {
    //display success
    console.log ('user found', data)
    profiles.value = data
    clicked = true;
  })
  .catch ((error)=>{
          console.log(error)
  });
};


//ajax request to fetch users but for the four latest profiles
function fetchNewProfiles(){
  fetch("/api/profiles", {method:'GET'})
  .then((response)=> response.json())
  .then((data)=>{
    //returns the list of new profiles
    newProfiles = data.slice(-4).reverse()
    console.log("Latest 4 profiles:", newProfiles);
  })
  .catch(error => {
      console.error("Error fetching profiles:", error);
    });
};

onMounted(()=>{ 
  fetchNewProfiles();
});


</script>

<template>
    <div class="container">
      <div class="text-center">
        <section>
          <RouterLink class="nav-link" to="/register">My Profile</RouterLink>
          
        </section>
        <section style="background-color: darkgray;"> <!--Display-->
          <h1>Search</h1>
          <input v-model="searchInput" @keyup.enter="searchProfiles" name="search" placeholder="Search by name, birth year, sex, or race" />
          <button @click="searchProfiles">Search</button>
        </section>
        <div v-if ="profiles?.length"> <!--Display search results-->
          <h3>Search Results for {{ searchInput }}</h3>
          <ul>
            <li v-for="profile in profiles" :key="profile.id">
              {{ profile.name }} ({{ profile.birth_year }} - {{ profile.sex }} - {{ profile.race }})
            </li>
          </ul>
        </div>
       <div v-if="profiles.length===0&& clicked"><!--Only shows when result is empty-->
          <p>No results yet.</p>
        </div>

        <div class="profiles-container" v-if="newProfiles?.length"> <!--Displays last four profiles-->
          <div class="profiles-card" v-for="new_prof in newProfiles" :key="new_prof.id">
            <img :src="new_prof.poster" alt="User profile image">
            <p> {{ new_prof.username }}</p>
          </div>
        </div>
      
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>