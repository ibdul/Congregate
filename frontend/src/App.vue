<template>
	<div class="bleed">

		<router-view/>
	<toast-deck>
		<toast
			v-for="(toast, id) in store.state.toastsStore.deck"
			@close="$RemoveToast(toast)"
			:key="id"
			:status="toast.status"
			:message="toast.message"
			:extra_info="toast.extra_info"
		/>
	</toast-deck>
		
	</div>
</template>

<script lang="ts">
	import { defineComponent, reactive } from 'vue'
	import { useStore } from  'vuex'
	export default defineComponent({
		setup(){
		
			let store = reactive(useStore())
			return{
				store
			}
		}
	})
</script>

<style lang="scss">
	
	#app {
		font-family: poppins, Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;

		background: $c1;
		// text-align: center;

		min-height: 100vh;
		color: $c2;
		padding: 16px;
	}
	
</style>
