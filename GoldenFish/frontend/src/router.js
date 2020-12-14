import Vue from 'vue';
import VueRouter from 'vue-router';
import Main from './views/Main.vue';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Main
    },
    {
      path: '/home',
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
      component: () => import('./views/Profile.vue')
    },
    {
      path: '/mywishes',
      name: 'mywishes',
      component: () => import('./views/Wishes/MyWishes.vue')
    },
    {
      path: '/friends',
      name: 'friends',
      component: () => import('./views/Friends/Friends.vue')
    },
    {
      path: '/fulfilled_wishes',
      name: 'fulfilled_wishes',
      component: () => import('./views/Wishes/FulfilledWishes.vue')
    },
    {
      path: '/planned_gifts',
      name: 'planned_gifts',
      component: () => import('./views/Gifts/PlannedGifts.vue')
    },
    {
      path: '/friends_search/:username',
      name: 'friends_search',
      component: () => import('./views/Friends/FriendsSearch.vue')
    },
    {
      path: '/friends_list',
      name: 'friends_list',
      component: () => import('./views/Friends/FriendsList.vue')
    },
    {
      path: '/friends_requests',
      name: 'friends_requests',
      component: () => import('./views/Friends/FriendsRequests.vue')
    },
    {
      path: '/friend/:id',
      name: 'friend',
      component: () => import('./views/Friends/Friend.vue')
    },
    {
      path: '*',
      component: Main
    }
  ]
});

router.beforeEach((to, from, next) => {
    const publicPages = ['/login', '/register', '/home'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
        next('/home');
    } 
    else {
        next();
    }
});

router.beforeEach((to, from, next) => {
    const publicPages = ['/login', '/register', '/home'];
    const loginPages = publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    if (loginPages && loggedIn) {
        next('/');
    } 
    else {
        next();
    }
})
