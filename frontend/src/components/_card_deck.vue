<template>
	<div  class="card_deck">

		<slot>
		</slot>

	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name: '_card_deck',
	})
</script>

<style lang="scss">
	.card_deck {
		display: inline-flex;
		flex-wrap: wrap;
	    align-items: center;
		gap: $g-1;

		&-fluid {
			width: 100%;
			justify-content: space-around;

			.card {
				flex: 1;
				min-width: 40%;
			}
		}
	}
	
</style>