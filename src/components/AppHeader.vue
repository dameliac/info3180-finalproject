<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Jam-Date</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
            <!-- Show login and signup links only on specific routes -->
            <li class="nav-item" v-if="currentRoute == '/'">
              <RouterLink to="/login" class="nav-link">Login</RouterLink>
            </li>
            <li class="nav-item" v-if="currentRoute == '/'">
              <RouterLink to="/register" class="nav-link">Sign Up</RouterLink>
            </li>
            <li class="nav-item" v-if="currentRoute == '/'">
              <RouterLink to="/profiles/favourites" class="nav-link">View Reports</RouterLink>
            </li>

            <!-- Other common nav items -->
            <li class="nav-item" v-if="isLoggedIn== true ">
              <RouterLink to="/logout" class="nav-link">Logout</RouterLink>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink, useRoute } from 'vue-router';
import { computed } from "vue";
// Get the current route using useRoute()
const route = useRoute();
const currentRoute = route.path;

//check if user is logged in
const isLoggedIn= computed(()=>{
    return !!localStorage.getItem('token');
  })

</script>


<style scoped>
/* Navbar container */
.navbar {
    background: rgba(255, 120, 150, 0.7); /* Light pinkish, 70% opacity */
    backdrop-filter: blur(10px); /* Soft blur behind the navbar */
    border-bottom: 2px solid rgba(255, 120, 150, 0.3); /* Light border */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.navbar-brand {
    font-family: 'Poppins', sans-serif;
    font-size: 1.5rem;
    font-weight: bold;
    color: #fff !important;
    transition: transform 0.3s ease;
}

.navbar-brand:hover {
    transform: scale(1.1);
    text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.6);
}

.nav-link {
    font-size: 1rem;
    font-weight: 500;
    color: #ffffff !important;
    padding: 8px 15px;
    border-radius: 8px;
    transition: background-color 0.3s ease, color 0.3s ease;
   
}

.nav-link:hover {
    background: rgba(255, 255, 255, 0.2);
    color: #ff7eb3 !important;
}

/* Navbar toggler */
.navbar-toggler {
    border: none;
    background: rgba(255, 255, 255, 0.4);
    border-radius: 4px;
}

.navbar-toggler-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3E%3Cpath stroke='rgba(255,255,255,0.85)' stroke-width='2' stroke-linecap='round' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

@media (max-width: 992px) {
    .navbar-nav .nav-link {
        margin-bottom: 10px;
        text-align: center;
    }
}

body {
    padding-top: 70px;
}
</style>
