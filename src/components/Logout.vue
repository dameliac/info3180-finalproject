<script setup>
//Part 2 #1
import {ref} from 'vue';

function Logout(){


  fetch ('/api/auth/logout', {method: 'POST'})
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('User logged out successfully', data)
  })
  .catch ((error)=>{
      
      console.log(error)
  });
};
</script>