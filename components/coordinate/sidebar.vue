<template>
  <aside
    class="bg-gradient-to-r from-slate-950 from-10% via-slate-800 via-85% to-slate-700 to-99% text-white rounded-tr-xl rounded-br-lg font-body h-screen overflow-hidden transition-all transform ease-out border border-slate-500 shadow-xl shadow-slate-100"
    :class="{ 'w-8': !isopen, 'w-1/6': isopen }"
  >
    <div>
      <button
        @click="toggle_button"
        class="bg-slate-950 text-white"
      >
        <Icon name="mdi:chevron-double-right"></Icon>
      </button>
      <div class="flex flex-row items-center">
        <img
          src="../../assets/person2.webp"
          alt=""
          width="75"
          class="rounded-full border border-slate-800 mx-3 my-3"
        />
        <div class="flex flex-col">
          <span>Dorothy White</span>
          <span class="text-sm text-slate-500"
            >Coordnator</span
          >
          <button
            class="rounded-lg text-sm text-violet-500"
          >
            Sign Out
          </button>
        </div>
      </div>
      <hr />
    </div>
    <!-- <div
      class="border border-slate-600 rounded-lg mt-6 px-2 py-2"
    >
      <Icon
        name="solar:user-hand-up-bold-duotone"
        size="25"
      >
      </Icon>
      <span class="ml-3">Applicants</span>
    </div>
    <div
      class="border border-slate-600 rounded-lg mt-6 px-2 py-2 transform transition-all hover:translate-x-1"
    >
      <Icon
        name="solar:buildings-2-bold-duotone"
        size="25"
      ></Icon>
      <span>Colleges</span>
    </div>
    <div
      class="border border-slate-600 rounded-lg mt-6 px-2 py-2 hover:translate-x-1"
    >
      <Icon
        name="solar:inbox-unread-bold-duotone"
        size="25"
      ></Icon>
      <span>Inbox</span>
    </div>
    <div class="mt-6 px-2 py-2 bg-slate-700 rounded-lg">
      <Icon
        name="solar:mask-sad-bold-duotone"
        size="25"
      ></Icon>
      <span>Patinets</span>
    </div>
    <div class="mt-6 px-2 py-2 bg-slate-700 rounded-lg">
      <Icon
        name="solar:settings-bold-duotone"
        size="25"
      ></Icon>
      <span> Account Settings</span>
    </div> -->
  </aside>
</template>

<script setup>
let isopen = ref(true);
function toggle_button() {
  isopen.value = !isopen.value;
}
let mehrdad = { sample: {} };
</script>

<style scoped></style>
