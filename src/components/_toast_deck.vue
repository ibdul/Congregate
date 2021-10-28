<template>
	<div class="toast_deck">
        <transition-group name="toast" tag="div" class="toast_deck_list">
            <slot>
            </slot>
	    </transition-group>
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
        bottom: 8%;
        z-index: 99;
        max-width: 60vw;

        &_list{
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
    }

</style>