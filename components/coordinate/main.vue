<template>
  <div>
    <main class="font-body">
      <section
        class="bg-white mt-6 px-6 mx-6 border max-w-xs rounded-lg"
      >
        <div>
          <h1 class="text-xl mx-2 my-2">Hi</h1>
          <hr />
          <p class="text-slate-500 px-2 py-2">
            Lorem ipsum dolor sit amet consectetur,
            adipisicing elit. Ipsa, cupiditate ratione ab ea
            libero laudantium quibusdam aliquid impedit quia
            atque aut incidunt facilis. Distinctio, iure
            odio eveniet consequatur voluptate ad.
          </p>
        </div>
      </section>
      <section
        class="bg-white mt-6 px-6 mx-6 border border-slate-300 max-w-xs rounded-lg shadow-md"
      >
        <div>
          <h1>Hi</h1>
          <p class="my-3">
            Lorem ipsum dolor sit amet consectetur,
            adipisicing elit. Ipsa, cupiditate ratione ab ea
            libero laudantium quibusdam aliquid impedit quia
            atque aut incidunt facilis. Distinctio, iure
            odio eveniet consequatur voluptate ad.
          </p>
          <div class="flex flex-row items-center gap-3">
            <img
              src="../../assets/Touch.jpg"
              alt=""
              class="rounded-full w-12 my-6"
            />
            <span class="italic text-sm text-slate-400"
              >John Doe</span
            >
          </div>
        </div>
      </section>
      <slot />
      <section
        class="bg-white mt-6 px-6 mx-6 border max-w-xs rounded-lg"
      >
        <div>
          <h1>Hi</h1>
          <p>
            Lorem ipsum dolor sit amet consectetur,
            adipisicing elit. Ipsa, cupiditate ratione ab ea
            libero laudantium quibusdam aliquid impedit quia
            atque aut incidunt facilis. Distinctio, iure
            odio eveniet consequatur voluptate ad.
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
