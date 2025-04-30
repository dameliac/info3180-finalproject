<script setup>
//Part 2
import Profiles from '@/components/NewProfile.vue';
</script>

<template>
    <!--Part 2 #2-->
    <div class="head-container">
        <h1>Create Profile</h1>
        <Profiles/>
    </div>
</template>

<style scoped>
/* Head Container for Profile Page */
.head-container {
  margin-top: 4rem;
  text-align: center;
  padding: 2rem;
  background: rgba(255, 245, 235, 0.9); /* Soft peach background */
  border-radius: 25px;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
}

/* Heading*/
.head-container h1 {
  font-size: 2.5rem;
  color: #cc6e5c;
  margin-bottom: 2rem;
  font-weight: bold;
  font-family: 'Poppins', sans-serif;
}
</style>