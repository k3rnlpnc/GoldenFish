import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Friends from './views/Friends.vue';
import FulfilledWishes from './views/FulfilledWishes.vue'

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/profile',
      name: 'profile',
      // lazy-loaded
      component: () => import('./views/Profile.vue')
    },
    {
      path: '/mywishes',
      name: 'mywishes',
      // lazy-loaded
      component: () => import('./views/MyWishes.vue')
    },
    {
      path: '/friends',
      name: 'friends',
      // lazy-loaded
      component: Friends
    },
    {
      path: '/filfilled_whishes',
      name: 'filfilled_whishes',
      // lazy-loaded
      component: FulfilledWishes
    }
  ]
});

// router.beforeEach((to, from, next) => {
//   const publicPages = ['/login', '/register', '/home'];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem('user');

//   // trying to access a restricted page + not logged in
//   // redirect to login page
//   if (authRequired && !loggedIn) {
//     next('/login');
//   } else {
//     next();
//   }
// });
