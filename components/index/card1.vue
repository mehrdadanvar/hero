<template>
  <div
    class="flex flex-col transform transition duration-500 hover:bg-slate-800 hover:scale-105 hover:shadow-lg hover:shadow-slate-500"
  >
    <div
      class="flex mx-auto translate-y-4 rounded-full z-10"
    >
      <Icon
        name="solar:users-group-two-rounded-line-duotone"
        size="60"
        class=""
      ></Icon>
    </div>
    <div
      class="rounded-xl shadow-md shadow-slate-500 relative bg-slate-700"
    >
      <h3
        class="text-3xl py-3 px-3 text-orange-600 hover:text-orange-500"
      >
        {{ title }}
      </h3>
      <div class="my-2 px-6">
        <h4 class="text-slate-100 text-xl">
          Gain Hands-On Experience While Studying
        </h4>
        <p class="text-slate-200 mt-6">
          Lorem ipsum dolor sit amet consectetur adipisicing
          elit. Numquam, cum. Optio aspernatur minima amet
          quaerat modi dolorum laborum, esse sunt
          dignissimos explicabo debitis placeat nihil
          exercitationem maxime perferendis quidem aperiam
          doloremque quisquam qui veritatis? Saepe a minus
          corporis. Nemo velit pariatur distinctio ducimus
          animi ad voluptate consequuntur, illum tenetur
          minus!
        </p>
      </div>
      <div class="relative overflow-hidden">
        <img
          :src="fullpath"
          class="but object-cover w-full opacity-70 relative rounded-b-md"
        />
        <div class="flex flex-row gap-2 items-center">
          <button class="rounded-lg px-2 py-2 text-white">
            Learn More
          </button>
          <Icon
            name="solar:map-arrow-right-bold-duotone"
          ></Icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { isContinueStatement } from "@babel/types";

const some = defineProps({ title: String, img: String });
let path = some.img;
let fullpath = `/_nuxt/assets/${path}`;
console.log(fullpath);

// console.log(fullpath);
</script>

<style scoped>
.but {
  height: 70px;
}
button {
  text-shadow: 0 10px 10px white;
}
</style>
