<script setup>
import { ref } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>

<template>
    <div class="container">
      <div class="text-center">

          <h1>{{ message }}</h1>

       
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>