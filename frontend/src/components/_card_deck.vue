<template>
	<div  class="card_deck full-bleed">

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
		// display: inline-flex;
		// flex-wrap: wrap;
	    // align-items: center;
		// gap: $g-1;

		// &-fluid {
		// 	width: 100%;
		// 	justify-content: space-around;

		// 	.card {
		// 		flex: 1;
		// 		min-width: 40%;
		// 	}
		// }
		position: relative;
		display: flex;
		padding: 1rem .4em;
		flex-grow: 1;
		overflow: auto;
		align-items: stretch;

		.card {
			display: flex;
			position: relative;
			align-items: stretch;
			height: 220px;
			padding: 1.5rem;
			flex: none;
			border-radius: 16px;
			// background: #40394e;
			box-shadow: -1rem 0 3rem rgba(0,0,0,.3);
			transition: .2s;
			justify-content: space-evenly;
			flex-direction: column;

			&:not(:first-child) {
				margin-left: -130px;
			}
			&:hover {
				transform: translateY(-1rem);

				&~.card {
					transform: translateX(130px);
				}
			}
		}
		& .card:hover{
			padding: 1.2rem .4em;
		}
	}
	
</style>