<template>
  <div class="page bg-slate-800 text-white font-body">
    <section class="hero mx-48 mb-72">
      <div class="pt-36">
        <div class="h-3/4 relative">
          <h1
            class="title text-5xl text-slate-400 py-12 px-12 -top-14"
          >
            Student-Homecare Collaboration
          </h1>
          <div class="flex max-w-2xl relative">
            <img
              src="../assets/Touch.jpg"
              alt=""
              class="rounded-full opacity-40"
            />
          </div>
          <div class="absolute -translate-y-96">
            <p class="text-4xl text-slate-200 px-14">
              Linking Students with In-Home Care Providers
            </p>
            <p class="text-4xl text-slate-300 px-14">
              Transforming Lives
            </p>
            <p class="my-36 text-2xl">
              Academic Institution-Industry Collaboration:
              The program fosters collaboration between
              universities/colleges and in-home care
              providers, strengthening the ties between
              academia and industry. This collaboration can
              lead to further research opportunities, joint
              initiatives, and mutually beneficial
              partnerships.
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="mt-36 pt-12 mx-36">
      <div
        class="lg:grid lg:grid-cols-3 lg:gap-12 md:grid-cols-1 md:gap-6"
      >
        <IndexCard1 title="Students" img="ai.jpg" />
        <IndexCard1 title="Schools" img="ai2.jpg" />
        <IndexCard1
          title="Care Organizations"
          img="ai4.jpg"
        />
      </div>
    </section>
    <section class="my-12">
      <div class="flex flex-row text-2xl mx-48 gap-12">
        <h2>Rgister Your Colledge</h2>
        <div class="border border-violet-500 rounded-lg">
          <input class="bg-slate-900" type="text" />
          <button class="px-9 py-3">
            <Icon
              name="solar:alt-arrow-right-broken"
              size="50"
            ></Icon>
          </button>
        </div>
      </div>
    </section>
    <section class="bg-white">
      <section class="container mx-auto mt-36 pt-12 mb-36">
        <div
          class="md:grid md:grid-cols-3 md:gap-6 sm:grid sm:grid-cols-1 sm:gap-6"
        >
          <div class="flex flex-col">
            <div
              class="flex mx-auto translate-y-4 rounded-full z-100 bg-slate-700"
            >
              <Icon
                name="solar:users-group-two-rounded-line-duotone"
                size="60"
                class=""
              ></Icon>
            </div>
            <div
              class="rounded-xl shadow-lg shadow-slate-600 relative"
            >
              <h3
                class="text-3xl py-3 px-3 text-orange-600 hover:text-orange-500"
              >
                Students
              </h3>
              <div>
                <h4 class="">
                  Gain Hands-On Experience While Studying
                </h4>
                <p class="text-white">
                  Lorem ipsum dolor sit amet consectetur
                  adipisicing elit. Numquam, cum. Optio
                  aspernatur minima amet quaerat modi
                  dolorum laborum, esse sunt dignissimos
                  explicabo debitis placeat nihil
                  exercitationem maxime perferendis quidem
                  aperiam doloremque quisquam qui veritatis?
                  Saepe a minus corporis. Nemo velit
                  pariatur distinctio ducimus animi ad
                  voluptate consequuntur, illum tenetur
                  minus!
                </p>
              </div>
              <div class="">
                <div class="h-fit">
                  <img
                    src="../assets/ai2.jpg"
                    alt=""
                    class="but object-cover w-full h-1/2"
                  />
                </div>
              </div>
            </div>
          </div>

          <div
            class="border border-violet-500 rounded-xl bg-gradient-to-tl from-slate-900 to-slate-700"
          >
            <Icon
              name="solar:buildings-bold-duotone"
              size="60"
              class="rounded-full text-violet-500"
            ></Icon>
            <h3 class="text-3xl py-3 px-3 text-violet-500">
              Schools
            </h3>
            <h4>
              Collaborate with Industry for Your Fuure
              Graduates
            </h4>
          </div>
          <div
            class="border border-violet-500 rounded-xl bg-gradient-to-tl from-slate-900 to-slate-700"
          >
            <Icon
              name="solar:hospital-bold-duotone"
              size="60"
              class="rounded-full"
            ></Icon>
            <h3 class="text-3xl py-3 px-3 text-pink-700">
              Care Organization
            </h3>
            <h4>
              Quickly Fill Your Vacant Positions with
              Talented students with Healthcare Backgrounds
            </h4>
          </div>
        </div>
      </section>
    </section>
    <Navbar />
  </div>
</template>

<script setup>
definePageMeta({ layout: "default" });
let students = ref([]);
async function test() {
  let data = await fetch("http://localhost:8000/students");
  let json = await data.json();
  students.value = json.students;
  console.log(json);
}
</script>

<style scoped>
.title {
  color: white;
  text-shadow: 0 0 1px #ffffff, 0 0 5px #ffffff;
}
.heroic {
  background-image: url("../assets/Touch.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  border-radius: 50%;
  background-position: inherit;
}
</style>
