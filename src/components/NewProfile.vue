<template>
    <!--Part 2 #1-->
    <form @submit.prevent="Profiles" id="ProfileForm">

      <div>
        <label for="description" class="form-label">Description:</label>
        <textarea type="text" name="description" class="form-control"></textarea>
      </div>
      <div>
        <label for="parish" class="form-label">Parish:</label>
        <input type="text" name="parish" class="form-control"  />
      </div>
      <div>
        <label for="biography" class="form-label">Biography:</label>
        <textarea type="text" name="biography" class="form-control"> </textarea>
      </div>
      <div>
        <label for="sex" class="form-label">Sex:</label>
        <input type="text" name="sex" class="form-control" />
      </div>
      <div>
        <label for=" race" class="form-label"> Race:</label>
        <input type="text" name=" race" class="form-control" />
      </div>
      <div>
        <label for="birth_year" class="form-label">Birth Year:</label>
        <input type="text" name="birth_year" class="form-control"  maxlength="4" pattern="\d{4}" inputmode="numeric"/>
      </div>
      <div>
        <label for="height" class="form-label">Height:</label>
        <input type="number" name="height" class="form-control"  />
      </div>
      <div>
        <label for="fav_cuisine" class="form-label">Favourite Cuisine:</label>
        <input type="text" name="fav_cuisine" class="form-control" />
      </div>
      <div>
        <label for="fav_colour" class="form-label">Favourite Colour:</label>
        <input type="text" name="fav_colour" class="form-control" />
      </div>
      <div>
        <label for="fav_school_subject" class="form-label">Favourite School Subject:</label>
        <input type="text" name="fav_school_subject" class="form-control" />
      </div>
      <div>
        <input type="checkbox" name="political"   />
        <label for="political" class="form-label">Political:</label>
        <input type="checkbox" name="religious"  />
        <label for="religious" class="form-label">Religious:</label>
        <input type="checkbox" name="family_oriented" />
        <label for="family_oriented" class="form-label">Family Oriented:</label>
      </div>
    
    

      <button type="submit">Create Profile</button>
    </form>
</template>

<script setup>
import {ref} from "vue";
const successMessage = ref('');
const errorMessages = ref([]);

function Profiles(){
  const profileForm = document.getElementById('ProfileForm');
  let form_data = new FormData(profileForm);

  fetch ('/api/profiles', {method: 'POST', body: form_data})
  .then ((response)=> response.json())
  .then ((data)=> {
      //display success
      console.log ('Login successful', data)
      //check if the response has a success message
      if(data.message){
          successMessage.value = data.message;
      }
      if (data.errors){
          errorMessages.value = data.errors;
      }
  })
  .catch ((error)=>{
      errorMessages.value = ["An unexpected error occurred. Please try again."];
      console.log(error)
  });
};

</script>