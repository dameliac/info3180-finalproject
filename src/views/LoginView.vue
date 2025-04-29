<script setup>
// Part 2 #2
import Login from '@/components/LoginForm.vue';
</script>


<template>
    <!-- Part 2 #2 -->
    <div class="head-container">
        <h1>Jam-Date</h1>
        <Login/>
    </div>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

:global(body) {
  margin: 0;
  height: 100vh;
  background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
  background-size: 400% 400%;
  animation: gradientMove 15s ease infinite;
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 36px;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}


.head-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

@keyframes gradientMove {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>



