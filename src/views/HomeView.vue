<script setup>
import { ref,computed } from "vue";
import searchProfiles from "@/components/UserPage.vue";
import fetchNewProfiles from "@/components/UserPage.vue";


  //check if the user is logged in
  const isLoggedIn= computed(()=>{
    return !!localStorage.getItem('token');
  })

</script>

<template> 
    <div class="container">
      <!--Content for logged-in users-->
      <div class="text-center" v-if="isLoggedIn" >
        <searchProfiles/>
      </div>

       <!-- Content for guests -->
      <div class="text-center" v-else>
        <h1>Jam-Date</h1>
        <h3>Welcome to Jam-Date — Your Match Starts Here!</h3>
        <p>Jam-Date is a vibrant and intelligent date-matching platform designed to help you find meaningful connections. 
          Create your personal profile, explore potential matches based on key compatibility traits, and discover people 
          who truly align with you.</p>
        <p>Search, connect, and express interest by adding profiles to your favourites with a simple click. 
          Dive deeper into matches to learn more about them, and enjoy insightful reports like the most 
          favourited users and who matches best with your own profile.</p>
        <p><strong>Jam-Date isn’t just about swiping — it’s about smart, thoughtful connections. Ready to meet your match?</strong></p>
        
      </div>
    </div>
</template>

<!--style sheet for the homepage-->
<style>
/* Add any component specific styles here */
</style>