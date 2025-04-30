<script setup>
//get specific user profile

import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";

const route = useRoute();
const profileID = route.params.profile_id;

const Profile = ref({});
const user = ref({});

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
}

onMounted(() => {
  fetchProfile();
});
</script>



<template>
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
        <button>Add to Favourites</button>
    </div>
    

</template>