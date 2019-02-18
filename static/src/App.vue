<template>
	<div class="fade page-sidebar-fixed page-header-fixed show page-container" v-if="!pageOptions.pageEmpty" v-bind:class="{ 
		'page-sidebar-minified': pageOptions.pageSidebarMinified, 
		'page-content-full-height': pageOptions.pageContentFullHeight, 
		'page-without-sidebar': pageOptions.pageWithoutSidebar, 
		'page-with-wide-sidebar': pageOptions.pageWithWideSidebar,
		'page-with-light-sidebar': pageOptions.pageWithLightSidebar,
		'page-sidebar-toggled': pageOptions.pageMobileSidebarToggled,
		'has-scroll': pageOptions.pageBodyScrollTop
	}">
		<Header />
		<TopMenu v-if="pageOptions.pageWithTopMenu" />
		<Sidebar v-if="!pageOptions.pageWithoutSidebar" />
		<SidebarRight v-if="pageOptions.pageWithTwoSidebar" />
		<div id="content" class="content" v-bind:class="{ 'content-full-width': pageOptions.pageContentFullWidth, 'content-inverse-mode': pageOptions.pageContentInverseMode }">
			<router-view></router-view>
			<vue-ins-progress-bar></vue-ins-progress-bar>
		</div>
		<Footer v-if="pageOptions.pageWithFooter" />
	</div>
	<div v-else>
		<router-view></router-view>
		<vue-ins-progress-bar></vue-ins-progress-bar>
	</div>
</template>

<script>
    import Sidebar from './components/sidebar/Sidebar.vue'
    import Header from './components/header/Header.vue'
    import PageOptions from './config/PageOptions.vue'

    export default {
        name: 'app',
        components: {
            Sidebar,
            Header
        },
        data() {
            return {
                pageOptions: PageOptions
            }
        },
        methods: {
            handleScroll: function() {
                PageOptions.pageBodyScrollTop = window.scrollY;
            }
        },
        mounted () {
            this.$insProgress.finish()
        },
        created() {
            PageOptions.pageBodyScrollTop = window.scrollY;

            window.addEventListener('scroll', this.handleScroll);

            this.$insProgress.start();

            this.$router.beforeEach((to, from, next) => {
                this.$insProgress.start();
                next()
            });
            this.$router.afterEach(() => {
                this.$insProgress.finish()
            })
        }
    }
</script>
