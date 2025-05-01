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
<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #fff7f0; /* Soft peach background */
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(253, 186, 140, 0.4); /* Peachy soft shadow */
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  color: #7c2d12; /* Deep warm brown */
  margin-bottom: 1rem;
  font-weight: bold;
}

h3 {
  font-size: 1.75rem;
  color: #9a3412; /* Rich warm tone */
  margin-bottom: 1.25rem;
  font-weight: 600;
}

p {
  font-size: 1.1rem;
  color: #78350f; /* Slightly softer brown */
  margin-bottom: 1rem;
  line-height: 1.6;
}

strong {
  color: #a16207; /* Golden warm accent */
  font-weight: 700;
}


.text-center {
  padding-top: 1rem;
  padding-bottom: 1rem;
}
</style>
