<template>
	<div  class="board">
		<div class="board__title">
			<slot name="board__title">
				Test board title
			</slot>
		</div>
		<div class="board__body">
			<section class="entries">
				<slot>
					Base Info text
				</slot>
			</section>
			<section>
				<slot name="board__subtitle">
					<p class="board__subtitle">
						descriptive text
					</p>
				</slot>
			</section>
		</div>
	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_board',
	});
</script>

<style lang='scss'>

.board {
    background: white;
    color: #0b1e26;
    text-align: center;
    padding: 10px 20px;
    border-radius: 12px;

	&__title {
		padding-bottom: 10px;
	}
	&__body {
		background: #182a4e;
		color: white;
		border-radius: 12px;
		padding: 10px;

		.entries {
			display: flex;
			flex-direction: row;
			flex-wrap: nowrap;
			justify-content: space-around;
			align-items: center;

			.count{
				font-size: 40px;
				font-weight: bold;
			}
		}
	}

}

</style>