<template>
    <!--Part 2 #1-->
    <form @submit.prevent="Profiles" id="ProfileForm">
        <!-- Success Message -->
        <div v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
        </div>
        <!-- Error Messages -->
        <div v-if="errorMessages.length" class="alert alert-danger">
        <ul>
            <li v-for="(error, index) in errorMessages" :key="index">{{ error }}</li>
        </ul>
        </div>

      <div>
        <label for="description" class="form-label">Description:</label>
        <textarea type="text" name="description" class="form-control"></textarea>
      </div>
      <div>
        <label for="parish" class="form-label">Parish:</label>
        <input type="text" name="parish" class="form-control"  />
      </div>
      <div>
        <label for="biography" class="form-label">Biography:</label>
        <textarea type="text" name="biography" class="form-control"> </textarea>
      </div>
      <div>
        <label for="sex" class="form-label">Sex:</label>
        <input type="text" name="sex" class="form-control" />
      </div>
      <div>
        <label for=" race" class="form-label"> Race:</label>
        <input type="text" name=" race" class="form-control" />
      </div>
      <div>
        <label for="birth_year" class="form-label">Birth Year:</label>
        <input type="text" name="birth_year" class="form-control"  maxlength="4" pattern="\d{4}" inputmode="numeric"/>
      </div>
      <div>
        <label for="height" class="form-label">Height:</label>
        <input type="number" name="height" class="form-control"  />
      </div>
      <div>
        <label for="fav_cuisine" class="form-label">Favourite Cuisine:</label>
        <input type="text" name="fav_cuisine" class="form-control" />
      </div>
      <div>
        <label for="fav_colour" class="form-label">Favourite Colour:</label>
        <input type="text" name="fav_colour" class="form-control" />
      </div>
      <div>
        <label for="fav_school_subject" class="form-label">Favourite School Subject:</label>
        <input type="text" name="fav_school_subject" class="form-control" />
      </div>
      <div>
        <input type="checkbox" name="political"   />
        <label for="political" class="form-label">Political:</label>
        <input type="checkbox" name="religious"  />
        <label for="religious" class="form-label">Religious:</label>
        <input type="checkbox" name="family_oriented" />
        <label for="family_oriented" class="form-label">Family Oriented:</label>
      </div>
    
    

      <button type="submit">Create Profile</button>
    </form>
</template>

<script setup>
import {ref, onMounted} from "vue";
const successMessage = ref('');
const errorMessages = ref([]);
let csrf_token = ref("");

function Profiles(){
  const profileForm = document.getElementById('ProfileForm');
  let form_data = new FormData(profileForm);

  const token=localStorage.getItem('token');

  fetch ('/api/profiles', {method: 'POST', body: form_data, headers:{
    'Authorization': `Bearer ${token}`,
    'X-CSRFToken': csrf_token.value
  }})
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ( data)
      //check if the response has a success message
      if(data.message){
          successMessage.value = data.message;
      }
      if (data.errors){
          errorMessages.value = data.errors;
      }
  })
  .catch ((error)=>{
      errorMessages.value = ["An unexpected error occurred. Please try again."];
      console.log(error)
  });
};


function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      });
  }
  
  onMounted(() => {
    getCsrfToken();
  });
</script>

<style scoped>
/* Profile Form Container */
#ProfileForm {
  background: rgba(255, 235, 220, 0.95); /* Peachy semi-transparent background */
  padding: 2rem;
  border-radius: 20px;
  max-width: 900px;
  margin: 3rem auto;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

/* Success and Error Messages */
.alert {
  padding: 1rem 1.5rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  font-size: 1.1rem;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Form Label */
label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #cc6e5c;
}

/* Form Inputs and Textareas */
input[type="text"],
input[type="number"],
textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #f5b7a1;
  border-radius: 10px;
  background-color: white;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus,
input[type="number"]:focus,
textarea:focus {
  border-color: #f1948a;
  outline: none;
}

/* Textareas larger */
textarea {
  min-height: 120px;
}

/* Checkboxes */
input[type="checkbox"] {
  margin-right: 10px;
  accent-color: #f1948a;
}

div > input[type="checkbox"] + label {
  display: inline-block;
  margin-right: 1.5rem;
  font-weight: normal;
  color: #aa5d50;
}

/* Submit Button */
button[type="submit"] {
  background-color: #f5b7a1;
  color: white;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%;
  margin-top: 1rem;
}

button[type="submit"]:hover {
  background-color: #f1948a;
}

/* Form Div Spacing */
#ProfileForm > div {
  margin-bottom: 1.5rem;
}

/* Bullet Points for Error List */
ul {
  padding-left: 1.5rem;
}

li {
  font-size: 1rem;
}

/* General Typography */
body {
  font-family: 'Poppins', sans-serif;
}
</style>