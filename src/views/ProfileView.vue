<script setup>


import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";

const route = useRoute();
const profileID = route.params.profile_id;
const Profile = ref({});
const user = ref({});
const successMessage = ref('');
const errorMessages = ref([]);
const token = localStorage.getItem('token');
let csrf_token = ref("");

console.log(token);

//get specific user profile
function fetchProfile() {
  fetch(`/api/profiles/${profileID}`, { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      Profile.value = data;

      // Fetch the user info using the foreign key
      fetchUser(data.user_id_fk);
    })
    .catch(error => {
      console.error("Error fetching profile:", error);
    });
}
 
//to display the user profile's name/owner
function fetchUser(userID) {
  fetch(`/api/users/${userID}`, { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      user.value = data;
      console.log(data);
    })
    .catch(error => {
      console.error("Error fetching user:", error);
    });
};

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
};

//add profile to favourites
function addFavourites(userid){
    
    fetch(`/api/profiles/${userid}/favourite`, {method:'POST', headers:{
        'Authorization' : `Bearer ${token}`,
        'X-CSRFToken': csrf_token.value,
        'Content-Type': 'application/json'
    }})
    .then(response => response.json())
    .then(data=>{
        if (data.message){
            successMessage.value = data.message;
            console.log ("Profile added to favourites", data);
        }
        if(data.errors){
            errorMessages.value =data.errors;
        }
    })
    .catch((error)=>{
    errorMessages.value = ['An unexpected error occurred. Please try again.'];
    console.log(error)
  });
};


onMounted(() => {
  fetchProfile();
  getCsrfToken();
});
</script>



<template>
    <div v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
    </div>
    <div v-if="errorMessages" class="alert alert-danger">
        {{ errorMessages }}
    </div>
    <section>
        <img src="../assets/image.png" />
        <h1>{{ user.name }}</h1>
    </section>

    <div>
        <p>Description: {{ Profile.description }}</p>
        <p>Biography: {{ Profile.biography }}</p>
        <p>Parish: {{ Profile.parish }}</p>
        <p>Race: {{ Profile.race }}</p>
        <p>Height: {{ Profile.height  }}</p>
        <p>Sex: {{ Profile.sex }}</p>
        <p>Birth Year: {{ Profile.birth_year }}</p>
        <p>Favourite Colour: {{ Profile.fav_color }}</p>
        <p>Favourite Cuisine: {{ Profile.fav_cuisine }}</p>
        <p>Favourite School Subject: {{ Profile.fav_school_subject }}</p>
        <p>Political: {{ Profile.political ? 'Yes' : 'No' }}</p>
        <p>Religious: {{ Profile.religious ? 'Yes' :'No'  }}</p>
        <p>Family Oriented: {{ Profile.family_oriented ? 'Yes' :'No' }}</p>
    
        <button>Email User</button>
        <button @click="addFavourites(Profile.user_id_fk)">Add to Favourites</button>
    </div>

    

</template>

<style scoped>
.alert-success {
  background-color: #ffe4e1; 
  color: #9c4221; 
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  margin-bottom: 1rem;
  font-weight: 500;
}

.alert-danger {
  background-color: #ffe0e0; 
  color: #b91c1c; 
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  margin-bottom: 1rem;
  font-weight: 500;
}

section {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 2rem;
}

section img {
  width: 90px;
  height: 90px;
  object-fit: cover;
  border-radius: 9999px; 
  border: 3px solid #fcd5ce; 
}

section h1 {
  font-size: 1.75rem; 
  font-weight: 700;
  color: #7c2d12; 
}

div {
  background-color: #fff7f0; 
  padding: 1.75rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(253, 186, 140, 0.4); 
}

div p {
  font-size: 1rem;
  color: #78350f; /* Rich brown */
  margin-bottom: 0.75rem;
}

button {
  margin-top: 1rem;
  margin-right: 0.75rem;
  padding: 0.5rem 1.25rem;
  background-color: #fca5a5; /* Soft coral-pink */
  color: white;
  font-weight: 600;
  border-radius: 0.5rem;
  transition: background-color 0.3s, transform 0.2s;
  cursor: pointer;
  border: none;
}

button:hover {
  background-color: #fb7185; 
  transform: translateY(-2px);
}
</style>
