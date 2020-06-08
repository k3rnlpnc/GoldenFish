import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Friends from './views/Friends.vue';
import FulfilledWishes from './views/FulfilledWishes.vue'
import MyWishes from './views/MyWishes.vue'
import PlannedGifts from './views/PlannedGifts.vue'
import FriendsSearch from './views/FriendsSearch.vue'

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
      component: MyWishes
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
    },
    {
      path: '/planned_gifts',
      name: 'planned_gifts',
      component: PlannedGifts
    },
    {
      path: '/friends_search',
      name: 'friends_search',
      component: FriendsSearch
    },
    {
      path: '/friends_list',
      name: 'friends_list',
      component: () => import('./views/FriendsList.vue')
    },
    {
      path: '/friends_requests',
      name: 'friends_requests',
      component: () => import('./views/FriendsRequests.vue')
    },
    {
      path: '/friend/:id',
      name: 'friend',
      component: () => import('./views/Friend.vue')
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
