<script setup>
//Part2 #1
import { useRoute } from 'vue-router';
import {ref, onMounted } from 'vue';
const route = useRoute();
const userID = route.params.user_id;
const userProfile = ref('');

onMounted(()=>{

  fetch (`/api/users/${user_id}`)
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('Profile(s) found', data)
      userProfile.value = data

  })
  .catch ((error)=>{
      console.log(error)
  });
})

</script>