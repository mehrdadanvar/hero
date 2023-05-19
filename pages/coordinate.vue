<template>
  <div class="bg-slate-200">
    <div class="flex flex-row">
      <CoordinateSidebar :class="{ 'px-4 py-2': true }" />
      <slot />
    </div>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing
      elit. Earum dicta quia ea cum alias ut in incidunt
      minima atque facere, soluta repudiandae officiis a, ex
      numquam pariatur tenetur! In, maxime?
    </p>
  </div>
</template>

<script setup>
definePageMeta({ layout: "coordinatordash" });
</script>

<style lang="scss" scoped></style>
