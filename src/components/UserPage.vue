<script setup>
  //Part2 #4
  import { ref, onMounted } from "vue";
  import { getUserIdFromToken } from "@/utils/authUtils.js";
  import { useToken } from "../composables/useToken.js";

  //get userID from token
  const userId = getUserIdFromToken();

  //reactive variables
  const searchInput = ref('');
  let profiles = ref([]);
  let clicked = ref(false);
  let newProfiles =ref([]);
  const { token } = useToken()
  

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
    fetch(`/api/search?${params.toString()}`, {method: 'GET', headers:{'Authorization':`Bearer ${token.value}`, 'Accept':'application/json'}})
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
    fetch("/api/profiles", {method:'GET', headers:{
    'Authorization': `Bearer ${token.value}`}})
    .then((response)=> response.json())
    .then((data)=>{
      //returns the list of new profiles
      newProfiles.value = data.slice(-4).reverse()
      console.log("Latest 4 profiles:", data.slice(-4).reverse());
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
          <RouterLink class="nav-link" :to="`/users/${userId}`">My Profile</RouterLink>
          
        </section>
        <section class="search-section"> <!--Display-->
          <h1>Search</h1>
          <input v-model="searchInput" @keyup.enter="searchProfiles" name="search" placeholder="Search by name, birth year, sex, or race" />
          <button @click="searchProfiles">Search</button>
        </section>
        <div v-if="profiles?.length" class="search-results"> 
          <h3>Search Results for "{{ searchInput }}"</h3>
          <div class="result-card" v-for="profile in profiles" :key="profile.id">
            <p><strong>Name:</strong> {{ profile.name }}</p>
            <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
            <p><strong>Sex:</strong> {{ profile.sex }}</p>
            <p><strong>Race:</strong> {{ profile.race }}</p>
          </div>
        </div>

       <div v-if="profiles.length===0&& clicked" class="no-results"><!--Only shows when result is empty-->
          <p>No results yet.</p>
        </div>

        <div class="profiles-container" v-if="newProfiles?.length"> <!--Displays last four profiles-->
          <div class="profiles-card" v-for="new_prof in newProfiles" :key="new_prof.id">
            <img src="/src/assets/image.png">
            <p> {{ new_prof.parish }}</p>
            <router-link  :to="`/profiles/${new_prof.id}`" tag="button">View more details</router-link>
          </div>
        </div>
      
      </div>
    </div>
</template>

<style>
body {
  background: linear-gradient(to right, #ffe0e9, #ffd6e0, #ffc2d1);
  min-height: 100vh;
  margin: 0;
  font-family: 'Poppins', sans-serif;
}

.text-center{
  background: rgba(255, 255, 255, 0.8); /* Soft white with transparency */
  border-radius: 15px; /* Rounded corners for a soft feel */
  padding: 2rem;
  max-width: 800px;
  margin: 2rem auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.text-center {
  text-align: center;
}

section {
  background-color: #ffccd5; /* lighter peach */
  padding: 20px;
  border-radius: 12px;
  margin: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

input[name="search"] {
  padding: 10px 15px;
  width: 60%;
  max-width: 400px;
  border: 1px solid #ffb3c1;
  border-radius: 20px;
  margin-right: 10px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  background-color: #ff8fa3;
  color: white;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #ff5c75;
}

.search-section {
  background: rgba(255, 229, 214, 0.9); /* Soft peach background */
  padding: 2rem;
  border-radius: 15px;
  margin: 2rem 0;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.search-section h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #d17a6d; /* soft coral color */
}

.search-section input {
  padding: 0.5rem 1rem;
  border: 1px solid #ffd8c2;
  border-radius: 25px;
  margin-right: 1rem;
  outline: none;
  width: 400px;
  background: #fff;
}

.search-section button {
  padding: 0.5rem 1.5rem;
  border: none;
  background-color: #ffb6a2;
  color: white;
  font-weight: bold;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-section button:hover {
  background-color: #ff987a;
}

.search-results {
  margin-top: 2rem;
}

.search-results h3 {
  color: #d17a6d;
  margin-bottom: 1rem;
}

.result-card {
  background: #ffe5d6;
  padding: 1rem 1.5rem;
  margin-bottom: 1rem;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  text-align: left;
}

.result-card p {
  margin: 0.5rem 0;
  color: #333;
}

.result-card strong {
  color: #d17a6d;
}

.no-results {
  background: #fff0e6;
  padding: 1.5rem;
  margin-top: 2rem;
  border-radius: 15px;
  text-align: center;
  color: #d17a6d;
  font-weight: bold;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.profiles-container {
  margin-top: 3rem;
  padding: 2rem;
  background: rgba(255, 240, 230, 0.8); /* soft peachy background */
  border-radius: 20px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.profiles-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  text-align: center;
  padding: 1rem;
  width: 200px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  transition: transform 0.2s ease;
}

.profiles-card:hover {
  transform: translateY(-5px);
}

.profiles-card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
}

.profiles-card p {
  margin-top: 0.75rem;
  font-weight: bold;
  color: #d17a6d;
}

</style>