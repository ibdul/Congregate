<template>
	<div class="toast_deck">
        <slot>
        </slot>
	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
        name:'_toast-deck',
		emits: [
			'close',
		]
	});
</script>

<style lang='scss' scoped>
    .toast_deck {
        position: fixed;
        right: 2%;
        bottom: 2%;
        z-index: 99;

        &_list{
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
    }

</style>