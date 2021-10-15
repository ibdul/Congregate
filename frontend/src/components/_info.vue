<template>
	<div  class="info">
		<slot>
			Base Info text
		</slot>
	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_info',
	});
</script>

<style lang='scss' scoped>
	.info {
		text-align: center;
		
		/* magic */
		padding: 50px;
		background: $c1-2;
		border-radius: 16px;
		&-fluid {
			width: 100%
		}
		&-float{
			position: fixed;
			z-index:99;
			top: 0;
			right: 0;
			left: 0;
			box-shadow: 0 0 12px rgba(0,0,0,.4);
		}
	}
</style>