<template>
    <!--Part 2 #2-->
    <form @submit.prevent="register" id="registerForm">
      <div>
          <input type="text" name="username" class="form-control" placeholder="Username:" />
      </div>
      <div>
          <input type="text" name="password" class="form-control" placeholder="Password:" />
      </div>
      <div>
          <input type="text" name="name" class="form-control" placeholder="Full Name:" />
      </div>
      <div>
          <input type="email" name="email" class="form-control" placeholder="Email Address:" />
      </div>
      <div>
            <label for="photo" class="form-label">Please upload a profile image.</label>
            <input type="file" name="photo" class="form-control" accept="image/*"/>
        </div>


      <div v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
      </div>
      <!-- Error Messages -->
      <div v-if="errorMessages.length" class="alert alert-danger">
      <ul>
          <li v-for="(error, index) in errorMessages" :key="index">{{ error }}</li>
      </ul>
      </div>

      <button type="submit">Sign Up</button>
    </form>
</template>

<script setup>
import {ref, onMounted} from 'vue';
let csrf_token = ref("");
const successMessage = ref('');
const errorMessages = ref([]);

function register(){
  const registerForm = document.getElementById('registerForm');
  let form_data = new FormData(registerForm);

  fetch ("/api/register", {method: 'POST', body: form_data, headers: {
    'X-CSRFToken': csrf_token.value}})
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('User is registered', data)
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
      console.log(error);
  });
};

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
}

onMounted(()=>{
    getCsrfToken();
});

</script>

<style scoped>
/* Form container */
form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    background: rgba(255, 255, 255, 0.8); /* slightly transparent white */
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
    width: 400px;
    margin: 20px auto;
}

input.form-control {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
    background: #fff;
}

label.form-label {
    font-weight: bold;
    margin-bottom: 5px;
    text-align: left;
    display: block;
    font-size: 14px;
    color: #333;
}

button[type="submit"] {
    padding: 12px;
    background: linear-gradient(135deg, #ff7eb3, #ff758c);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
}

button[type="submit"]:hover {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    transform: scale(1.05);
}

.alert-success {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
}

.alert-danger {
    background-color: #f8d7da;
    color: #842029;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
}

input[type="file"] {
    padding: 8px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
}
</style>
