<template>
	<div class="container">
		<fadeFx>
			<h5 class="brand-name">Congregate</h5>
		</fadeFx>

		<stack
			size="lg"
			>

			<fadeFx :to="routeDirectionY">
				<stack size="z">
					<p class="page_suptitle">Home</p>
					<h1 class="page_title">Welcome,</h1>
					<p class="page_subtitle">What would you like to do on the app today?</p>
				</stack>
			</fadeFx>


			<stack>
				<fadeFx
					:to="routeDirectionY"
					:delay="2"
					>
					<board>
						<template  #board__title>
							<h3>
								Site Statistics
							</h3>
						</template>

						<section>
							<p class="count">{{counts.events!==undefined?counts.events:'X'}}</p>
							<p>event<template v-if="counts.events>1  || counts.events===undefined">s</template></p>
						</section>
						<section>
							<p class="count">{{counts.tickets!==undefined?counts.tickets:'Y'}}</p>
							<p>ticket<template v-if="counts.tickets>1 || counts.tickets===undefined">s</template></p>
						</section>

						<template #board__subtitle>
							<p>registered</p>
						</template>
					</board>
				</fadeFx>

				<card-deck class="card_deck-fluid" >
				<fadeFx
					:to="routeDirectionY"
					:delay="3"
					>
					<card
						@click="$router.push({name: 'host'})"
						class="card-fluid"
						>
						Host an event
					</card>
				</fadeFx>

				<fadeFx
					:to="routeDirectionY"
					:delay="4"
					>
					<card
						class="card-fluid"
						@click="$router.push({name: 'join'})" 
						>
						Join an event
					</card>
				</fadeFx>
				</card-deck>

				<fadeFx
					:to="routeDirectionY"
					:delay="5"
					>
					<card class="card card-fluid"
						@click="$router.push({name: 'manage'})"
						>
						Manage an event
					</card>
				</fadeFx>
			</stack>

		</stack>

			<fadeFx
				:to="routeDirectionY"
				:delay="6"
				>

			<footer class="footer footer-center">
				<p><router-link to="about">About us</router-link></p>
			</footer>
		</fadeFx>

	</div>
</template>

<script lang="ts">
	interface _SiteStatisticsType {
		events?: number,
		tickets?: number
	}

	import axios from 'axios'
	import { ResponseObjectType, ResponseErrorObjectType, routeDirectionType } from '@/consumables/typings'
	import { computed, defineComponent, reactive, ref } from 'vue';

	export default defineComponent({
		name: 'Home',
		setup(){
			let routeDirection = ref<routeDirectionType>('forward')
			let counts = reactive<_SiteStatisticsType>({
				events: undefined,
				tickets: undefined
			})

		
			const fetchSiteStatistics = async() => {
				await axios
					.get(`api/v1/statistics`)
					.then((response: ResponseObjectType) => {
						Object.assign(counts, response.data)
					})
			}
			const routeDirectionY = computed(() => {
				return routeDirection.value=='forward'? 'top' : 'bottom'
			})

			// created hook equivalent
			fetchSiteStatistics()

			return {
				counts,
				routeDirectionY
			}
		}

	});
</script>

<style lang="scss" scoped>
.brand-name {
    text-transform: uppercase;
    letter-spacing: .2rem;
    font-weight: 500;
}

</style>