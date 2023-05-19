<template>
  <main class="register">
    <div class="flex flex-col gap-3">
      <h1>Welcome to Student Login</h1>
      <Icon name="solar:login-2-bold" size="30"></Icon>
      <form class="flex flex-col gap-6" @submit.prevent="login">
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Email Address</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-mail" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="text"
              v-model="email"
              placeholder="mail@provider.com"
              autocomplete="off"
              class="w-full text-slate-300 pl-3"
            />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Password</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="carbon:password" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="password"
              placeholder="more than 6 characters"
              v-model="password"
              class="w-full text-slate-300 pl-3"
            />
          </div>
        </div>
        <div class="foot flex flex-row gap-12">
          <button
            class="bg-purple-700 text-slate-300 rounded-lg w-36 h-9 shadow-md shadow-slate-500 hover:bg-purple-800 hover:text-white"
          >
            Log In
          </button>
          <button
            class="bg-purple-700 text-white rounded-lg w-36 h-9 shadow-md shadow-slate-500 hover:bg-purple-800 hover:text-lg hover:trans"
          >
            <NuxtLink to="/">Forgot Password</NuxtLink>
          </button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
let email = ref("");
let password = ref("");

function validate() {
  if (!password.value | !email.value) {
    return [false, "username or password missing"];
  } else {
    return [true, "credentails present trying to login"];
  }
}

async function studentlogin() {
  let response = await $fetch("http://localhost:8000/studentlogin", {
    method: "POST",
    body: {
      email: email.value,
      password: password.value,
    },
  });
  console.log(response);
  if (response.status === "sucess") {
    navigateTo("/Dashboard");
  }
}

async function login() {
  console.log("login requested");
  let validated = validate();
  if (validated[0]) {
    studentlogin();
  } else {
    console.log("credentails not present");
  }
}
</script>
