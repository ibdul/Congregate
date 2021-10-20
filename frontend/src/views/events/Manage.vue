<template>
<div>
	<div class="container">
		<fadeFx  :totalElements="6">
			<header class="header">
				<btn class="btn-primary-clear"
					@click="$router.push({name: 'home'})"
					>
						Home
				</btn>
				<btn class="btn-primary-clear"
					v-if="step == totalSteps"
					@click="downloadCsv"
					>
						Download
				</btn>
			</header>
		</fadeFx>
	
		<stack size="lg">
			<fadeFx
				:to="routeDirectionY"
				:delay="2"
				:totalElements="6"
				>
				<dots
					:step='step'
					:total='totalSteps'
				/>
			</fadeFx>
		
			<template v-if="step==1">
				<fadeFx
					:to="routeDirectionY"
					:delay="3"
					:totalElements="6"
					>
					<stack size="z">
						<p class="page_suptitle">Manage event</p>
						<h1 class="page_title">{{step}}. Find event</h1>
					</stack>
				</fadeFx>

					<stack>
						<form  id='form-1' class="stack_pass" @submit.prevent="validate()">
							<fadeFx
								:to="routeDirectionY"
								:delay="4"
								:totalElements="6"
								>
								<field-set
									field="event code" 
									placeholder="What is the code to your event?"
									v-model="payload.event"
									:required="true"
								/>
							</fadeFx>

							<fadeFx
								:to="routeDirectionY"
								:delay="5"
								:totalElements="6"
								>
								<field-set
									field="event pass code" 
									placeholder="What is the pass code of the event?"
									v-model="payload.pass"
									:required="true"
								/>
							</fadeFx>
						
							<fadeFx
								:to="routeDirectionY"
								:delay="6"
								:totalElements="6"
								>
								<input type="submit" hidden=true id="submit-form">
							</fadeFx>

						</form>
					</stack>
			</template>
			
			<template v-else-if="step==2">
				<fadeFx
					:to="routeDirectionY"
					:delay="4"
					:totalElements="6"
					>
					<stack size="z">
						<p class="page_suptitle">Manage event</p>
						<h1 class="page_title">{{step}}. Guests list</h1>
						<p class="page_subtitle" v-if="data.tickets.length">Click on a guest to see more details.</p>
					</stack>
				</fadeFx>
				
				<fadeFx
					:to="routeDirectionY"
					:delay="5"
					:totalElements="6"
					>
					<stack>
						<table v-if="data.tickets.length">
							<thead>
								<tr>
									<th>S/N</th>
									<th>Ticket class</th>
									<th>Email</th>
									<th>Ticket code</th>
								</tr>
							</thead>
							<tbody>
								<tr
								v-for="(ticket, id) in data.tickets"
								:key="ticket.code"
								@click="openModal(ticket, 'ticket')"
								>
									<td>{{id+1}}</td>
									<td>{{ticket.ticket_class}}</td>
									<td>{{ticket.email}}</td>
									<td>{{ticket.code}}</td>
								</tr>
							</tbody>
						</table>
					</stack>
				</fadeFx>
			
			</template>
		</stack>

		<fadeFx
			:totalElements="6"
			>
			<footer class="footer">
				<p v-if="step == totalSteps">
					<i>{{data.tickets.length}} ticket<template v-if="data.tickets.length>1">s</template> registered.</i>
				</p>
				<btn
					class="btn-primary-clear"
					@click="validate(true)"
					v-if="(buttons.footer.primary.visible && step !== totalSteps)"
					:disabled="buttons.footer.primary.disabled"
					:class="buttons.footer.primary.status==CONSTANTSX.busy ? 'btn-loading' : '' "
					>
						{{buttons.footer.primary.status || buttons.footer.primary.text}}
				</btn>
				<btn
					class="btn-primary-clear"
					@click="previous"
					v-if="buttons.footer.secondary.visible && step !== 1"
					:disabled="buttons.footer.secondary.disabled"
					>
						{{buttons.footer.secondary.text}}
				</btn>
				
			</footer>
		</fadeFx>
	</div>

	<transition name='modal'>
			<modal
				v-if="modal.visible && modal.type=='ticket' "
				:striped="true"
				@close="closeModal()"
				>
					<template #modal__title>
							<h2>Ticket</h2>
					</template>
					<template #default>
						<stack>
						<stack size="sm">
							<h3 class="section__title">Basic ticket information</h3>
							<stack size="z">
								<h5>Ticket Code</h5>
								<p>{{modal.temp.code}}</p>
							</stack>
							<stack size="z">
								<h5>TIcket Class</h5>
								<p>{{modal.temp.ticket_class}}</p>
							</stack>
							<stack size="z">
								<h5>Email</h5>
								<p>{{modal.temp.email}}</p>
							</stack>
						</stack>

						<stack size="sm">
							<h3 class="section__title">Requested data</h3>
							<stack
									size="z"
									v-for="(field, id) in modal.temp.requested_information_answers"
									:key="id"
									>
									<h5>{{field.requested_information}}</h5>
									<p>{{field.answer}}</p>
							</stack>
							<p v-if="modal.temp.requested_information_answers.length==0">No data to display</p>
						</stack>
						
						<!-- <stack>
							<h3 class="section__title">Required data</h3>
							<stack>
								<h5>Email</h5>
								<p>{{payload.email}}</p>
							</stack>
						</stack> -->

						</stack>
					</template>
					
					<template #modal__footer>
							<btn class="" @click="closeModal">close</btn>
					</template>
			</modal>
	</transition>

</div>
</template>

<script lang="ts">
	import axios from 'axios'

	import CONSTANTS from '@/consumables/constants'
	import { useToasts } from '@/consumables/plugins'
    import { 
		requestedInformationType,
		requestedInformationAnswerType,
		responseTicketClassType,
		ticketClassType,
		reponseRequestedInformationType,
		ResponseObjectType,
		ResponseErrorObjectType,
		routeDirectionType,
		} from '@/consumables/typings'

	import { computed, defineComponent, reactive, ref } from 'vue'
	
	interface _payloadType{
		event: string,
		pass: string,
	}
	type _modalType = 'ticket'

    export default defineComponent({

        setup (props: any, context: any) {
			let routeDirection = ref<routeDirectionType>('forward')
			const $toasts: any = useToasts()
			const CONSTANTSX = CONSTANTS
			let step= ref<number>(1)
			let totalSteps= ref<number>(2)
			let buttons= reactive({
				footer: {
					primary: {
						disabled: false,
						visible: true,
						text: 'next',
						status: ""
					},
					secondary: {
						disabled: false,
						visible: true,
						text: 'back',
						status: ""
					},
					tertiary: {
						disabled: false,
						text: 'finalize',
						status: ""
					},
				},
			})
			let modal = reactive({
				visible: false,
				type:"",
				state: "",
				temp: <any>{},
			})
			let payload = reactive<_payloadType>({
				'event': '',
				"pass": "",
			})
			let data= reactive<any>({})
			

			/////// METHODS

			const validate = async(fromNext=false)=>{

				let encounteredError = false
				if(fromNext){
					let submitBtn: HTMLElement = document.querySelector('#submit-form') as HTMLElement
					submitBtn.click()
				}
				else{
					buttons.footer.primary.status = CONSTANTS.busy
					buttons.footer.primary.disabled = true

					if(step.value == 1){
						await axios
							.post(`/api/v1/events/manage/`, 
								payload)
							.then( (response: ResponseObjectType) => {
								$toasts.SuccessToast("Event matched")
								Object.assign(data, response.data)
							})
							.catch((error: ResponseErrorObjectType) => {
								encounteredError = true
								if (error.response.status==404){
									$toasts.ErrorToast("Error", "Event not found")
								}
								else{
									$toasts.ErrorToast("Something went wrong")
								}
							})
					}
					if(encounteredError==false){
						next()
					}
				buttons.footer.primary.status = ""
				buttons.footer.primary.disabled = false
				}
			}
			const next = ()=>{
				if (step.value < totalSteps.value){
					step.value += 1
					routeDirection.value="forward"
				}
			}
			const previous = ()=>{
				if (step.value != 1){
					step.value -= 1
					routeDirection.value="backward"
				}
			}
			const openModal = (data: any, type: _modalType)=>{
				modal.temp = data
				modal.visible = true
				modal.type = type
			}
			const closeModal = ()=>{
				if (modal.type == 'event'){
					buttons.footer.primary.text = "next"
					buttons.footer.primary.disabled = false
				}
				modal.temp = {}
				modal.visible = false
				modal.type = ''
				modal.state = ''
			}
			const downloadCsv = async()=>{
				await axios
					.post(`/api/v1/events/downloadCSV/`, 
						payload)
					.then( (response: any) => {
						const blob = new Blob([response.data], {type:"text/csv"})
						const link = document.createElement('a')
						link.href = URL.createObjectURL(blob)
						link.download = `event-${payload.event}.csv`
						link.click()
						URL.revokeObjectURL(link.href)
					})
					.catch( error => {
						$toasts.ErrorToast("Something went wrong")
					})
			}
			const routeDirectionY = computed(() => {
				return routeDirection.value=='forward'? 'top' : 'bottom'
			})
			// const routeDirectionX = computed(() => {
			// 	return routeDirection.value == 'forward'? 'right':'left'
			// })

		return{
			CONSTANTSX,
			step,
			totalSteps,
			buttons,
			modal,
			payload,
			data,
			routeDirectionY, //routeDirectionX,

			validate,
			next,
			previous,
			openModal,
			closeModal,
			downloadCsv,
		}
		}
	})
</script>

<style lang="scss" scoped>
	table{

		width: 100%;
		
		thead {
			background-color: $c2;
			color: $c1;
		}
		tbody{
			tr{
				background: transparent;
				color: $c2;
				
				&:nth-child(even) {
					background: $c1-2;
					color: $c2;
				}

				&:hover {
					background: $c2;
					color: $c1;
					cursor: pointer;
				}
			}
		}
		td {
			max-width: 12ch;
			overflow: hidden;
			white-space: nowrap;
			text-overflow: ellipsis;
		}
		td, th {
			padding: 4px;
			text-align: center;

		}
	}
</style>