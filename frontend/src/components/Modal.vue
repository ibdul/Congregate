<template>
	<div>
		<div class="overlay"  @click="$emit('close')" ></div>

		<div
			class="modal"
			:class="striped?'modal-striped':''"
			>
				<div class="modal__head">
					<button type="button" class="close"  @click="$emit('close')" v-if="showClose">
						<span aria-hidden="true">&times;</span>
					</button>
					<button type="button" class="icon"  v-else-if="icon">
						<span aria-hidden="true">{{ icon }}</span>
					</button>

					<section class="modal__title">
							<slot name="modal__title">
								modal title
							</slot>
					</section>
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
			},
			striped: {
				type: Boolean,
				default: false,
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
		opacity: .85;
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

		width: 80vw;
		max-width: 600px;
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
		&__title {
			h2 {
			font-weight: normal;
			font-size: 1em;
			letter-spacing: .2em;
			}
		}
		&__body {
			margin: $g1 0 $g1 0;

			.stack_deck > .multi + .multi {
				border-top: 2px solid $c1-2;
			}
			.multi {
				position: relative;
				.count {
					position: absolute;
					font-size: 4rem;
					margin: auto;
					color: $c1-2;
					opacity:.2;
					top: 50%;
					transform: translateY(-50%);
					right: 0;
				}
			}
		}
		&-striped {
			.modal__body{

				//  > *:nth-child(even),
				//  > .stack > *:nth-child(even){
				// 	background: $c1-2;
				// 	// opacity:.2;
				// }

				& ,
				& > .stack {
					&> *+* {
						border-top: solid;
					}
				}
			}
		}

	}
	.right{
		float: right;
	}

</style>