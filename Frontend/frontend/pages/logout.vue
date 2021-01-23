<template>
	<div>
		
	</div>
</template>

<script>
	export default {
		mounted() {
			this.logout();
		},

		methods: {
			async logout() {
                await this.$auth.logout();
				this.$router.push('/login')
			}
		}
	}
</script>