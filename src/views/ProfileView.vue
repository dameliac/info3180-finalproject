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