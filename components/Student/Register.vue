<template>
  <main class="register">
    <div class="">
      <h1 class="text-2xl mb-12">Student Registration Form</h1>
      <form class="flex flex-col gap-6" @submit.prevent="upload">
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="text"
              v-model="firstname"
              placeholder="First Name"
              class="w-full text-violet-800 pl-3 focus:border-none"
            />
          </div>
        </div>
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="text"
              v-model="lastname"
              placeholder="Last Name"
              class="w-full text-slate-800 pl-3"
            />
          </div>
        </div>
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-mail" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="text"
              v-model="email"
              placeholder="mail@provider.com"
              autocomplete="off"
              class="w-full text-slate-500 pl-3"
            />
          </div>
        </div>
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="solar:user-id-bold" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="text"
              v-model="student_id"
              placeholder="Student ID Number"
              class="w-full text-slate-500 pl-3"
              autocomplete="off"
            />
          </div>
        </div>
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="solar:key-bold" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="password"
              placeholder="more than 6 characters"
              v-model="password"
              class="w-full text-slate-500 pl-3"
              autocomplete="off"
            />
          </div>
        </div>
        <div class="">
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="solar:key-bold" size="30" class="text-slate-500 mx-3"></Icon>
            <input
              type="password"
              placeholder="Confirm Your Password"
              v-model="repeat_password"
              class="w-full text-slate-500 pl-3"
            />
          </div>
        </div>
        <div class="foot flex flex-row gap-12 mt-6">
          <button
            class="bg-purple-100 text-violet-500 rounded-lg w-36 h-12 shadow-md shadow-violet-400 hover:bg-purple-800 hover:text-white"
          >
            Create Account
          </button>
          <button
            class="bg-purple-100 text-purple-600 rounded-lg w-36 h-12 shadow-md shadow-violet-400 hover:bg-purple-800 hover:text-white"
          >
            <NuxtLink to="/">Login</NuxtLink>
          </button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
let firstname = ref("");
let lastname = ref("");
let email = ref("");
let student_id = ref("");
let password = ref("");
let repeat_password = ref("");

function validate() {
  if (password.value !== repeat_password.value) {
    console.log("Passwords don't match");
  }
}

let identifier = ref("password");
function toggle() {
  if (identifier.value === "password") {
    identifier.value = "text";
  } else {
    identifier.value = "password";
  }
}

async function upload() {
  validate();
  let body = { first_name: firstname.value };
  console.log(body);
  const api_response = await $fetch("http://localhost:8000/students", {
    method: "POST",
    body: {
      firstname: firstname.value,
      lastname: lastname.value,
      email: email.value,
      password: password.value,
    },
  });
  console.log(api_response);
}
</script>
