<template>
  <main class="register">
    <div class="image"></div>
    <div class="">
      <form class="flex flex-col gap-6">
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Fist Name</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-300 mx-3"></Icon>
            <input type="text" value="John" class="w-full text-slate-300 pl-3" />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Last Name</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-person-3" size="30" class="text-slate-300 mx-3"></Icon>
            <input type="text" value="John" class="w-full text-slate-300 pl-3" />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Email Address</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="ic:round-mail" size="30" class="text-slate-300 mx-3"></Icon>
            <input type="text" value="John" class="w-full text-slate-300 pl-3" />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Password</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="carbon:password" size="30" class="text-slate-300 mx-3"></Icon>
            <input type="password" value="John" class="w-full text-slate-300 pl-3" />
          </div>
        </div>
        <div class="">
          <label for="" class="text-slate-500 w-24 pl-3">Confirm PassWord</label>
          <div class="border border-1 flex flex-row rounded-lg w-3/4">
            <Icon name="carbon:password" size="30" class="text-slate-300 mx-3"></Icon>
            <input type="password" value="John" class="w-full text-slate-300 pl-3" />
          </div>
        </div>
        <div class="foot">
          <button>Create Account</button>
          <button><NuxtLink to="/">I have an Account</NuxtLink></button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
let identifier = ref("password");
function toggle() {
  if (identifier.value === "password") {
    identifier.value = "text";
  } else {
    identifier.value = "password";
  }
}
</script>
