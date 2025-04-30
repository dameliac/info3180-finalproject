<script setup>
//Part 2
import {RouterLink} from 'vue-router';
import {ref, onMounted} from 'vue';
const successMessage = ref('');
let errorMessages = ref([]);

function Logout(){
    const token = localStorage.getItem('token'); //get JWT token

      // Check if token exists before making the logout request
    if (!token) {
        errorMessages.value = ['No token found, you are not logged in.'];
        return; // Prevent further actions if no token is found
    }
    console.log('Token:', localStorage.getItem('token'));

  fetch ('/api/auth/logout', {method: 'POST', headers:{
    'Authorization': `Bearer ${token}`, //send token
    'Content-Type': 'application/json'
  }})
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('User logged out successfully', data)
      if (data.message){
        successMessage.value = data.message;
        localStorage.removeItem('token');
      }
      if (data.errors){
        errorMessages.value =data.errors;
      }
  })
  .catch ((error)=>{
    errorMessages.value = ['An unexpected error occurred. Please try again.'];
    console.log(error)
  });
};

onMounted(()=>{
    Logout();
});


</script>


<!----><template>
    <div v-if="successMessage" class="alert alert-success">
    {{ successMessage }}
        <RouterLink to="/">Return to home</RouterLink>

    </div>

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