<template>
	<section  class="stack"
		:class="`stack-${size}`">
		<slot>
			Base stack text
		</slot>
	</section>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_stack',
		props: {
			size: {
				type: String,
				default: "md"
			}
		},
	});
</script>

<style lang='scss'>
	.stack {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		
		& > *{
			margin-top: 0;
			margin-bottom: 0;
		}
		&.stack-{
			&z {
			
				& > * + *,
				& > .stack_pass > * + *  {
					margin-top: 0;
				}
			}
			&xsm {
			
				& > * + *,
				& > .stack_pass > * + *  {
					margin-top: $s-xsm;
				}
			}
			&sm {
			
				& > * + *,
				& > .stack_pass > * + *  {
					margin-top: $s-sm;
				}
			}
			&md {
			
				& > * + *,
				& > .stack_pass > * + *  {
					margin-top: $s-md;
				}
			}
			&lg {
				
				& > * + *,
				& > .stack_pass > * + *  {
					margin-top: $s-lg;
				}
			}
		}
	}
</style>