<template>
  <div
    class="bg-slate-800 border-b border-violet-700 font-body"
  >
    <nav
      class="flex flex-row gap-6 align-middle text-white px-12 py-4"
    >
      <div class="">
        <h1
          class="font-logo font-bold text-3xl text-orange-400"
        >
          Hero AppliConnect
        </h1>
      </div>
      <div class="ml-64 flex flex-row gap-6 text-slate-300">
        <div class="">
          <NuxtLink to="/">Home</NuxtLink>
        </div>
        <div class="">
          <NuxtLink to="/About">How It Works</NuxtLink>
        </div>
        <div>
          <NuxtLink to="/Coordinate"
            >Care Coordinators</NuxtLink
          >
        </div>
        <div>
          <NuxtLink to="/Colleges"
            >Potential Colleges</NuxtLink
          >
        </div>
        <div>
          <NuxtLink to="/Student">Students</NuxtLink>
        </div>
        <div
          class="border border-violet-500 rounded-lg px-3 py-3 bg-violet-500 text-white hover:shadow-md hover:shadow-violet-500"
        >
          <NuxtLink to="/Student">Students</NuxtLink>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
