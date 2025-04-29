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