<script>

    const routes = [
        { path: '/', component: () => import(/* webpackChunkName: "global" */'../pages/Login.vue') },
        { path: '/home', component: () => import(/* webpackChunkName: "global" */'../pages/Home.vue') },
    ];

    export default routes;
</script>
