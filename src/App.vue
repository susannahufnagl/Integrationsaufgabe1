<template>
  <div id="app">
    <nav>
      <ul>
      <li><router-link to="/account">AccountErstellen</router-link></li>
      <li><router-link to="/wahlen">WahlFormular</router-link></li>
      <li><router-link to="/auswerten">Wahlergebnisse</router-link></li>
    </ul>
  </nav>
  <router-view/>
</div>
</template>

<script>

export default {
  name: 'App',
  };

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>