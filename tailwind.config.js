/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    minWidth: {
      "1/2": "50%",
    },
    extend: {
      fontFamily: {
        body: ["Source Sans Pro"],
        logo: ["Quicksand"],
      },
    },
  },
  plugins: [],
};
