<template>
	<div  class="card" @click="$emit('click')">
		
		<div class="card__main">
			<slot>
				Main Card Text
			</slot>
		</div>

	</div>
</template>


<script lang="ts">
	import { defineComponent } from 'vue';
	import btn from './_button.vue'

	export default defineComponent({
		name:'_card',
		emits: ['click'],
		components:{
			btn
		},
        props:{
			action: {
				type: Boolean,
				required: false,
				default: false,
			}
		}
	});
</script>

<style lang='scss' scoped>
	.card {
		color: $c1;
		background: $c2;
		display: grid;
		place-content: center;
		cursor: pointer;
		position: relative;
		transition: .2s;

		/* magic nums */
		width: 186px;
		padding: 16px;
		height: 186px;
		// margin: 12px;
	    border-radius: 16px;

		&__main {
			font-size: x-large;
			font-weight: bold;
			text-align: center;
			
			text-overflow: clip;
			overflow: hidden;
		}
		&__action_group {
			width: 100%;
			position: absolute;
			display: flex;
			justify-content: space-between;
			
			/* magic nums */
			/* padding: 16px; */
			}

		&__footer {
			bottom: 0;
		}

		&-fluid{
				width: 100%;

				/* magic nums */
				height: 186px;
		}
		&:hover, &-active, &:focus, &:active {
			transform: translateY(-2px);
			background: $c1-2;
			color: $c2;
			box-shadow: -6px -4px 19px #00000059, 3px 6px 19px 1px #00000059;
		}

	}

	
	

	
</style>