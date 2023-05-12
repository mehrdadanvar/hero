<template>
  <main class="register">
    <div class="image"></div>
    <div class="container">
      <form>
        <div class="border boder-1">
          <label for="">Name</label>
          <div class="border boder-1">
            <Icon name="ic:round-person-3"></Icon>
            <input type="text" />
          </div>
        </div>
        <div class="input-item">
          <label for="">Last Name</label>
          <input type="text" />
        </div>
        <div class="input-item">
          <Icon name="ic:round-mail"></Icon>
          <label for="">Email Address</label>
          <input type="text" />
        </div>
        <div class="input-item-icon">
          <label for="">Password</label>
          <span>
            <input :type="identifier" class="special" />
            <i @click.prevent="toggle" class="icon">
              <img src="../assets/eye.svg" alt="" />
            </i>
          </span>
        </div>
        <div class="input-item-icon">
          <label for=""> confirm Password</label>
          <span>
            <input :type="identifier" class="special" />
            <i @click.prevent="toggle" class="icon">
              <img src="../assets/eye.svg" alt="" />
            </i>
          </span>
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

<style scoped>
.register {
  display: flex;
  flex-direction: row;
  gap: 0rem;
  border-radius: 1rem;
}
.container {
  display: flex;
  border-radius: 1rem;
  padding-left: 2rem;
}
.image {
  width: 20rem;
  height: 40rem;
  background: linear-gradient(45deg, #4361ee, #f72585);
  border-radius: 1rem;
}
.input-item {
  max-width: 30rem;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  color: #4361ee;
  gap: 1rem;
}
.input-item-icon {
  max-width: 30rem;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  color: #4361ee;
  gap: 1rem;
}
.special {
  max-width: 29rem;
}
input {
  border-radius: 0.25rem;
  height: 2rem;
  border: 1px solid grey;
  padding-left: 0.5rem;
  font-size: 18px;
}
input:focus {
  background-color: #ffffff;
  border: none;
}
button {
  background-color: #f72585;
  color: white;
  width: 10rem;
  height: 3rem;
  border-radius: 1rem;
  border: none;
}
button:hover {
  box-shadow: 0 0 20px #f72585;
}
.foot {
  display: flex;
  gap: 1rem;
}
.icon {
  position: absolute;
  transform: translate(-3rem, 0.3rem);
}
</style>
