<template>
	<div class="container">

		<stack
			size="lg"
			>

			<stack size="z">
				<p class="page_suptitle">Home</p>
				<h1 class="page_title">Welcome,</h1>
				<p class="page_subtitle">What would you like to do on the app today?</p>
			</stack>


			<stack>
			<info class="info-fluid" v-if="counts.events>0">
				<p><mark>{{counts.events}}</mark> event<template v-if="counts.events>1">s</template> registered </p>
				<p><mark>{{counts.tickets}}</mark> ticket<template v-if="counts.tickets>1">s</template> registered</p>
			</info>

			<card-deck class="card_deck card_deck-fluid">
				<card
					@click="$router.push({name: 'host'})"
					>
					Host an event
				</card>

				<card
				@click="$router.push({name: 'join'})" 
					>
					Join an event
				</card>
			</card-deck>

			<card class="card card-fluid"
				@click="$router.push({name: 'manage'})"
				>
				Manage an event
			</card>
			</stack>

		</stack>


		<footer class="footer footer-center">
            <p><a href="#">About us</a></p>
        </footer>

	</div>
</template>

<script lang="ts">
	interface _SiteStatisticsType {
		events: number,
		tickets: number
	}


	import axios from 'axios'
	import { ResponseObjectType, ResponseErrorObjectType } from '@/consumables/typings'
	import { defineComponent, reactive } from 'vue';

	export default defineComponent({
		name: 'Home',
		setup(){
			let counts = reactive<_SiteStatisticsType>({
				events: 0,
				tickets: 0
			})

		
			const fetchSiteStatistics = async() => {
				await axios
					.get(`api/v1/statistics`)
					.then((response: ResponseObjectType) => {
						Object.assign(counts, response.data)
					})
			}

			// created hook equivalent
			fetchSiteStatistics()

			return {
				counts
			}
		}

	});
</script>

<style lang="scss" scoped>

</style>