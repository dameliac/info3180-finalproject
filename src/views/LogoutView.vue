<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToken } from "../composables/useToken.js"
const { token } = useToken()
const router = useRouter();
let csrf_token = ref("");
const token = localStorage.getItem('token');
if (!token) {
    console.error('No token found!');
    
}


async function getCsrfToken_Logout() {
    try {
        const response = await fetch('/api/v1/csrf-token');
        const data = await response.json();
        csrf_token.value = data.csrf_token;
        console.log(token);
        Logout();  // Only call Logout after CSRF token is set
    } catch (error) {
        console.error('Error fetching CSRF token:', error);
    }
}

function Logout(){
  
  fetch('/api/auth/logout', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Authorization': `Bearer ${token}`,
      'X-CSRFToken': csrf_token.value,
      'Content-Type': 'application/json'
    }
  
  })
    .then(response => {
      if (response.ok) {
        token.value = undefined
        localStorage.removeItem('token');
        router.push('/'); //Redirect to homepage
      } else {
        return response.json().then(err => {
          throw new Error(err.message || 'Logout failed');
        });
      }
    })
    .catch(error => {
      console.error('Logout error:', error);
      console.log(localStorage.getItem('token'));
      alert('Logout failed. Please try again.');
      router.push('/'); // Fallback redirect to homepage
    });
};



onMounted(() => {
  getCsrfToken_Logout();
  

});
</script>

<template>
  <p>Logging out...</p>
</template>



<style scoped>
/* Success Alert Styling for Logout*/
.alert-success {
  margin: 5rem auto;
  max-width: 600px;
  padding: 2rem;
  text-align: center;
  background: rgba(255, 235, 220, 0.95); 
  border: 2px solid #ffb6a1; 
  border-radius: 20px;
  color: #cc6e5c;
  font-size: 1.3rem;
  font-family: 'Poppins', sans-serif;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.alert-success a {
  display: inline-block;
  margin-top: 1.5rem;
  text-decoration: none;
  color: white;
  background-color: #ff9472; 
  padding: 0.8rem 1.5rem;
  border-radius: 30px;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.alert-success a:hover {
  background-color: #ff7a5c; 
}
</style>