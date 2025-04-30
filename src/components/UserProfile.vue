<script setup>
//Part2 #1
import { useRoute } from 'vue-router';
import {ref, onMounted } from 'vue';
const route = useRoute();
const userID = route.params.user_id;
const userProfile = ref('');

function fetchUser(){

  fetch (`/api/users/${user_id}`)
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('user found', data)
      userProfile.value = data;

  })
  .catch ((error)=>{
      console.log(error)
  });
};

</script>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: 50px auto;
  background: rgba(255, 255, 255, 0.85); /*Soft transparent white */
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(8px);
}

.profile-container h1 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #333;
}

.profile-details {
  font-size: 1.2rem;
  color: #444;
  line-height: 1.6;
}

.profile-details p {
  margin-bottom: 12px;
}

.profile-details strong {
  color: #222;
}

.alert {
  margin-top: 20px;
  padding: 15px;
  border-radius: 10px;
  font-weight: bold;
  text-align: center;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
}
</style>