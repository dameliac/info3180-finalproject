<template>
    <!-- Part 2 #2 -->
    <form @submit.prevent="Login" id="loginForm">
      <div>
        <label for="username">Username</label>
        <input type="text" name="username" class="form-control" placeholder="Username:" />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" name="password" class="form-control" placeholder="Password:" />
      </div>
  
      <!-- Error Messages -->
      <div v-if="errorMessages.length" class="alert alert-danger">
        <ul>
          <li v-for="(error, index) in errorMessages" :key="index">{{ error }}</li>
        </ul>
      </div>
  

  
      <button type="submit">Login</button>
    </form>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  
  //const successMessage = ref('');
  const errorMessages = ref([]);
  let csrf_token = ref("");
  const router = useRouter();
  
  function Login() {
    const loginForm = document.getElementById('loginForm');
    let form_data = new FormData(loginForm);
  
    fetch('/api/auth/login', { 
      method: 'POST', 
      body: form_data, 
      headers: { 'X-CSRFToken': csrf_token.value }
    })
    .then((response) => response.json())
    .then((data) => {
      console.log('Login successful', data);
      if (data.message) {
       // successMessage.value = data.message;
        localStorage.setItem('token', data.token)
        router.push('/');// << REDIRECT after login
      }
      if (data.errors) {
        errorMessages.value = data.errors;
      }
    })
    .catch((error) => {
      errorMessages.value = ["An unexpected error occurred. Please try again."];
      console.log(error);
    });
  }
  
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
  /* Styling the whole form */
  form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    background: rgba(255, 255, 255, 0.75); 
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
    width: 400px;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px); 
}
 
  input.form-control {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button[type="submit"] {
    padding: 10px;
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
  
  .alert {
    background-color: #f8d7da;
    color: #842029;
    padding: 10px;
    border-radius: 4px;
    font-size: 14px;
  }
  
  .alert-success {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 4px;
    font-size: 14px;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 8px;
    display: block;
    text-align: left;
    color: #333;
    font-size: 14px;
  }
  </style>
  