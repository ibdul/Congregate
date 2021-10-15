<template>
	<div>
		<div class="overlay"  @click="$emit('close')" ></div>

		<div  class="modal L0">
				<div class="modal__head">
					<button type="button" class="close"  @click="$emit('close')" v-if="showClose">
						<span aria-hidden="true">&times;</span>
					</button>
					<button type="button" class="icon"  v-else-if="icon">
						<span aria-hidden="true">{{ icon }}</span>
					</button>

					<slot name="modal__title">
						modal title
					</slot>
				</div>

				<div class="modal__body">
					<slot>
						modal body
					</slot>
				</div>
				<div class="modal__action_group">
					<slot name="modal__footer">
						<btn class="" @click="$emit('close')">close</btn>
						<btn class="" @click="$emit('select')">select</btn>
					</slot>
				</div>
		</div>

	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';
	import btn from './_button.vue'

	export default defineComponent({
		name:'Modal',
		emits: [
			'close',
			'select',
			],

		components:{
			btn
		},
		props: {
			icon: {
				required: false,
				type: String
			},
			showClose: {
				default: true,
				type: Boolean
			}
		}
	})
</script>

<style lang='scss'>
	
	.modal__action_group {
		display: flex;
    	justify-content: flex-end;
	}

	
	.overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background-color: rgba(0, 0, 0, 0.8);
		z-index: 97;
	}
	.modal__head {
		display: flex;
		justify-content: space-between;
		flex-direction: row-reverse;
		width: 100%;
		align-items: center;
	}
	.close, .icon{
		// position: absolute;
		// top: 0;
		// right: 0;
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
		color: red;
	}
	.icon{
		color: $cs;
	}
	.modal {
		position: fixed;
		background: white;
		color: $c1;

		width: 70%;
		padding: 20px;
		z-index: 98;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);

		overflow-y: auto;
    	max-height: 80vh;
		
		h4, h3, h2 {
			text-transform: capitalize;
		}

		&__body {

			& > section + section {
				margin-top: 23px;
			}

			& > section > *:not(h3) {
				margin-left: 12px;
				background: aliceblue;
    			margin-top: 12px;
			}

		}
	}
	.right{
		float: right;
	}

	.L0 > * + * {
		margin-top: 16px;
	}

</style>