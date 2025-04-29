<template>
    <!--Part 2 #2-->
  <div class="head-container">
    <h1>Register</h1>
    <Signup />
  </div>
</template>

<script setup>
//Part 2 #2
import Signup from '@/components/RegisterForm.vue';
</script>

<style>
h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 36px;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}
</style>
