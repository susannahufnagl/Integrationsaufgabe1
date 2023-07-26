import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router';
import  App  from './App.vue';
import store from './store';

import AccountErstellen from './components/AccountErstellen.vue';

import WahlFormular from './components/WahlFormular.vue';
import AuswertungWahl from './components/AuswertungWahl.vue';



const routes = [
  {
    path: '/account',
    name: 'AccountErstellen',
    component: AccountErstellen,
  },
  { 
    path: '/wahlen',
    name: 'Wahl',
    component: WahlFormular,
  },
  {
    path: '/auswerten',
    name: 'AuswertungWahl',
    component: AuswertungWahl,
  } 
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});


const app= createApp(App);
app.use(router);
app.use(store);
app.mount('#app');

console.log(router)
console.log(store)

export default router;