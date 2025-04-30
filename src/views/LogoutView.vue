<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  fetch('/api/auth/logout', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`,
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      if (response.ok) {
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