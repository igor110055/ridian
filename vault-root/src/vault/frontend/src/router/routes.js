import Vue from 'vue';
import VueRouter from 'vue-router';
// import Frontview from '../components/Frontview.vue';
import ftx from '../components/ftx.vue';
import withdrawal from '../components/withdrawal.vue';
import convert from '../components/convert.vue';


Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        // {
        //     path:'/',
        //     name:'Frontview',
        //     component: Frontview,
        // },
        {
            path:'/',
            name:'ftx',
            component: ftx,
        },
        {
            path:'/withdrawals',
            name:'withdrawal',
            component: withdrawal,
        },
        {
            path:'/convert',
            name:'convert',
            component: convert,
        },


            
    ],
})