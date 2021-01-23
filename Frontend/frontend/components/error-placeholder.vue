<template>
	<div>
		<content-placeholders>
	      	<content-placeholders-text :lines="2" />
	      	<div class="alert alert-danger alert-dismissable">
	      		<center> {{message}} </center>
	      	</div>
	      	<content-placeholders-text :lines="2" />
	    </content-placeholders>
	</div>
</template>

<script>
	export default {
		props: ['message']
	}
</script>
