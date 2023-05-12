<template>
  <main class="register">
    <div class="">
      <h1>Student Registration Form</h1>
      <form class="" @submit.prevent="upload">
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Fist Name</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="text"
              v-model="firstname"
              placeholder="First Name"
              class="w-full text-slate-300 pl-3"
            />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Last Name</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="text"
              v-model="lastname"
              placeholder="Last Name"
              class="w-full text-slate-300 pl-3"
            />
          </div>
        </div>
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
          <label for="" class="text-slate-500 w-24 pl-3">Student ID</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="solar:user-id-bold" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="text"
              v-model="student_id"
              placeholder="Student ID Number"
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
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Confirm PassWord</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="carbon:password" size="30" class="text-slate-300 mx-3"></Icon>
            <input
              type="password"
              placeholder="Please make sure your passwords matche"
              v-model="repeat_password"
              class="w-full text-slate-300 pl-3"
            />
          </div>
        </div>
        <div class="foot border boder-1 flex flex-row gap-12">
          <button
            class="bg-purple-700 text-slate-300 rounded-lg w-36 h-12 shadow-md shadow-slate-500 hover:bg-purple-800 hover:text-white"
          >
            Create Account
          </button>
          <button
            class="bg-purple-700 text-white rounded-lg w-36 h-12 shadow-md shadow-slate-500 hover:bg-purple-800"
          >
            <NuxtLink to="/">Already have one ? Login</NuxtLink>
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
function upload() {
  validate();
  console.log(firstname.value);
}
</script>
