<template>
	<div class="toast" :class="status !==''? `toast-${status}` : '' ">
		<button type="button" class="close"  @click="$emit('close')">
            <span aria-hidden="true">&times;</span>
        </button>
        <div class="toast__body">
            <h4>{{message}}</h4>
            <p>{{extra_info}}</p>
	    </div>
	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_toast',
		emits: [
			'close',
		],
		props:{
		message:{
			type: String,
			required: true,
        },
		extra_info:{
			type: String,
        },
		status:{
			type: String,
        },
	},
	
	});
</script>


<style lang='scss' scoped>
	.toast {
		opacity: 50%;
		display: flex;
		align-items: center;
		flex-direction: row-reverse;
		width: 100%;
		background: $c2;
		color: $c1;
		z-index: 99;

		
		&:hover {
			opacity: 100%;
		}
		&-danger{
			background-color: $cd;
		}
		&-success{
			background-color: $cs;
		}
		.toast__body {
			flex: 1;
			padding: 12px;
		}
	}
   	.close{
		padding: .75rem 1.25rem;
		cursor: pointer;
		font-size: 1.5rem;
		font-weight: 700;
		line-height: 1;
		color: #000;
		text-shadow: 0 1px 0 #fff;
		border: none;
		opacity: .4;
		background-color: transparent;
	}
	.close:hover{
		opacity: 50%;
	}
</style>