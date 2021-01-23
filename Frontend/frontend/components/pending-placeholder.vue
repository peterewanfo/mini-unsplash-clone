<template>
	<div>
		<content-placeholders
	      	v-for="p in 3"
	      	:key="p"
	      	rounded
	      	class="article-card-block"
	    >
	      	<content-placeholders-img />
	      	<content-placeholders-text :lines="3" />
	    </content-placeholders>
	</div>
</template>

<style>
	.vue-content-placeholders-img,
	.vue-content-placeholders-text__line {
		background: #C0C0C0;
	}
</style>

<script>
	export default {

	}
</script>