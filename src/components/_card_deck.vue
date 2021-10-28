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
	.card_deck{
		display: grid;
		grid-gap: $s-sm;
		grid-template-columns: 186px;
		grid-auto-flow: column;
		grid-auto-columns: 186px;

		overflow-x: auto;
		overflow-y: hidden;
		scroll-snap-type: x proximity;
		padding-bottom: calc(.75 * $s-sm);
		margin-bottom: calc(.25 *  $s-sm);

		.card{
			scroll-snap-align: center;
			padding: calc(($s-sm/2) *1.5);
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;

		}

		&-fluid {
			display: inline-flex;
			flex-wrap: wrap;
			align-items: center;
			gap: $g-1;

			width: 100%;
			justify-content: space-around;

			.card {
				min-width: 40%;

				&-fluid{
					flex: 1;
				}

				& :hover{
					padding: 1.2rem .4em;
				}
			}
		}

	}
</style>