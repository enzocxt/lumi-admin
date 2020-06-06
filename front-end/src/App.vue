<template>
  <div id="app" class="global">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
.global {
  position: relative;
  min-width: 1280px;
  height: 100%;
	margin:0;
	padding:0;
  background: linear-gradient(to bottom,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2);
  background-repeat:no-repeat;
}

</style>
