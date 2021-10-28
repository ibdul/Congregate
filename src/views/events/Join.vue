<template>
<div>
<div class="container">
	<fadeFx>
		<header class="header">
			<btn class="btn-primary-clear"
				@click="$router.push({name: 'home'})"
				>
					Home
			</btn>
		</header>
	</fadeFx>


		<stack size="lg">
			<fadeFx
					:to="routeDirectionY"
					:delay="2"
					:totalElements="2"
					>
				<dots
					:step='step'
					:total='totalSteps'
				/>
			</fadeFx>
			<template v-if="step==1">
				<fadeFx
					:to="routeDirectionY"
					:totalElements="2"
					>
					<stack size="z">
						<p class="page_suptitle">Join an event</p>
						<h1 class="page_title">{{step}}. Find event</h1>
						<p class="page_subtitle">Enter a valid event code to proceed.</p>
					</stack>
					</fadeFx>
					<stack>
					<form @submit.prevent="validate" class="stack_pass">
						<fadeFx
							:to="routeDirectionY"
							:delay="2"
							:totalElements="2"
							>
							<field-set
								field="event code" 
								placeholder="What is the code to the event you want to join"
								v-model="payload.event"
								:required="true"
							/>
						</fadeFx>
						<input type="submit" hidden=true id="submit-form">
					</form>
					</stack>
			</template>

			<template v-else-if="step==2">
				<fadeFx
					:to="routeDirectionY"
					>
					<stack size="z">
						<p class="page_suptitle">Join an event</p>
						<h1 class="page_title">{{step}}. Class selection</h1>
						<p class="page_subtitle"> Click on a card to get it's details.</p>
					</stack>
					</fadeFx>
					<stack>
						<card-deck>
						<!-- <template 
							> -->
						<fadeFx
							v-for="card in data.ticket_classes"
							:key="card.id"
							:to="routeDirectionY"
							:delay="2+card.id"
							:totalElements="2+data.ticket_classes.length"
							>
							<card 
								:class="payload.ticket_class == card.data.id ? 'card-active' : '' "
								@click="openModal(card,'class')"
								>
								{{card.data.title}}
							</card>
						</fadeFx>
						<!-- </template> -->
						</card-deck>
					</stack>
			</template>

			<template v-else-if="step==3">
				<fadeFx
					:to="routeDirectionY"
					:totalElements="2"
					>
					<stack size="z">
						<p class="page_suptitle">Join an event</p>
						<h1 class="page_title">{{step}}. Requested Information</h1>
						<p class="page_subtitle">Fill in the information below as requested by the event organizers.</p>
					</stack>
				</fadeFx>

				<stack>
					<form class="stack_pass" @submit.prevent="validate">
						<fadeFx
							v-for="field in data.requested_information"
							:key="field.id"
							:to="routeDirectionY"
							:delay="2"
							:totalElements="2"
							>
							<field-set
								:field="field.data.title" 
								:type="field.data.kind"
								:maxlength="field.data.maxlength"
								:placeholder="field.data.short_description"
								:help_text="field.data.description"
								:required="field.data.required"

								v-model="field.data.data"
							/>
						</fadeFx>
						
					<fadeFx
						:to="routeDirectionY"
						:delay="2"
						:totalElements="2"
						>
						<h4 v-if="data.requested_information.length==0">No requested data. Please click next to proceed</h4>
					</fadeFx>
						<input type="submit" hidden=true id="submit-form">
					</form>
				</stack>
			</template>
			
			<template v-else-if="step==4">
				<fadeFx
					:to="routeDirectionY"
					:totalElements="3"
					>
					<stack size="z">
						<p class="page_suptitle">Join an event</p>
						<h1 class="page_title">{{step}}. Payment Information</h1>
						<template v-if="paymentRequired">
							<p class="page_subtitle">Your Selection requires you to pay a fee.</p>
							<p class="page_subtitle">Fill the information below to proceed.</p>
						</template>
						<template v-else>
							<p class="page_subtitle">Your Selection doesn't require any fee.</p>
							<p class="page_subtitle">Fill the information below and then proceed.</p>
						</template>
					</stack>
				</fadeFx>

					<stack>
						<template v-if="paymentRequired">
							<fadeFx
								:to="routeDirectionY"
								:delay="2"
								:totalElements="3"
								>
								<h3>
									payment funtionality coming soon!
								</h3>
							</fadeFx>
						</template>

						<form class="stack_pass" @submit.prevent="validate">
							<fadeFx
								:to="routeDirectionY"
								:delay="3"
								:totalElements="3"
								>
								<field-set
									field="email" 
									placeholder="Enter  your email"
									type="email"
									:required="true"
									v-model="payload.email"
								/>
							</fadeFx>
							<input type="submit" hidden=true id="submit-form">
						</form>
					</stack>
			</template>
		</stack>

		<fadeFx
			:to="routeDirectionY"
			>
			<footer class="footer">
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
					@click="validate(true)"
					v-if="step == totalSteps"
					:disabled="buttons.footer.tertiary.disabled"
					:class="buttons.footer.tertiary.status==CONSTANTSX.busy ? 'btn-loading' : '' "
					>
						{{buttons.footer.tertiary.text}}
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
	<transition name="modal">
		<modal
			v-if="modal.visible && modal.type=='event' "
			@close="closeModal()"
			>
				<template #modal__title>
					<fadeFx  :totalElements="6">
						<h2>Find an event</h2>
					</fadeFx>
				</template>
				<template #default>
					<stack>
						<fadeFx
							to="top"
							:delay="2"
							:totalElements="6"
							>
							<stack  size="xsm">
								<h5>Title</h5>
								<p>{{modal.temp.title}}</p>
							</stack>
						</fadeFx>
						<fadeFx
							to="top"
							:delay="3"
							:totalElements="6"
							>
							<stack  size="xsm">
								<h5>Type of event</h5>
								<p>{{modal.temp.kind}}</p>
							</stack>
						</fadeFx>
						<fadeFx
							to="top"
							:delay="4"
							:totalElements="6"
							>
							<stack  size="xsm">
								<h5>Date Of Event</h5>
								<p>{{parseDate(modal.temp.start_date)}}</p>
							</stack>
						</fadeFx>
						<fadeFx
							to="top"
							:delay="5"
							:totalElements="6"
							>
							<stack  size="xsm">
								<h5>Venue</h5>
								<p>{{modal.temp.venue}}</p>
							</stack>
						</fadeFx>
						<fadeFx
							to="top"
							:delay="6"
							:totalElements="6"
							>
							<stack  size="xsm">
								<h5>Description</h5>
								<p>{{modal.temp.description}}</p>
							</stack>
						</fadeFx>
					</stack>
				</template>
				<template #modal__footer>
					<btn class="" @click="closeModal">close</btn>
					<btn
						:class="modal.state !== '' ? 'btn-loading' : '' "
						:disabled="modal.state !== ''"
						@click="selectModalData"
						>
						{{ modal.state !== '' ? modal.state : 'select'}}
					</btn>
				</template>
		</modal>
		<modal
			v-else-if="modal.visible && modal.type=='class' "
			@close="closeModal()"
			>
				<template #modal__title>
					<fadeFx  :totalElements="modal.temp.data.length">
						<h2>Select a ticket class</h2>
					</fadeFx>
				</template>
				<template #default>
					<stack
						size="sm"
						v-for="(val, item, id) in modal.temp.data"
						:key="id"
						>
						<fadeFx
							to="top"
							:delay="id+1"
							:totalElements="modal.temp.data.length"
							>
							<stack size="xsm" v-if="item !== 'id'">
								<h5>{{item}}</h5>
								<p>{{val}}</p>
							</stack>
						</fadeFx>
					</stack>
				</template>
				<template #modal__footer>
						<btn class="" @click="closeModal">close</btn>
						<btn
						:class="modal.state !== '' ? 'btn-loading' : '' "
						:disabled="modal.state !== '' "
						@click="selectModalData"
						>
							{{ modal.state !== '' ? modal.state : 'select'}}
						</btn>
				</template>
		</modal>
		<modal
			v-else-if="modal.visible && modal.type=='summary' "
			@close="closeModal()"
			>
				<template #modal__title>
					<fadeFx  :totalElements="4">
						<h2>Summary of your ticket data</h2>
					</fadeFx>
				</template>
				<template #default>
					<stack>
						<fadeFx
							to="top"
							:delay="2"
							:totalElements="4"
							>
							<stack size="sm">
								<h3 class="section__title">Basic ticket information</h3>
								<stack size="xsm">
									<h5>Event Title</h5>
									<p>{{data.event.title}}</p>
								</stack>
								<stack size="xsm">
									<h5>TIcket Class</h5>
									<p>{{data.ticket_class.title}}</p>
								</stack>
								<stack size="xsm">
									<h5>Ticket Cost</h5>
									<p>{{data.ticket_class.cost}}</p>
								</stack>
							</stack>
						</fadeFx>

					<fadeFx
						to="top"
						:delay="3"
						:totalElements="4"
						>
						<stack size="sm">
							<h3 class="section__title">Data requested by event organizers</h3>
							<stack
									size="xsm"
									v-for="field in data.requested_information"
									:key="field.id"
									>
									<h5>{{field.data.title}}</h5>
									<p>{{field.data.data.length!==0? field.data.data : '-'}}</p>
							</stack>
							<h5 v-if="data.requested_information.length==0">No requested data. Please click next to proceed</h5>
						</stack>
					</fadeFx>

					<fadeFx
						to="top"
						:delay="4"
						:totalElements="4"
						>
						<stack size="sm">
							<h3 class="section__title">Required data</h3>
							<stack size="xsm">
								<h5>Email</h5>
								<p>{{payload.email}}</p>
							</stack>
						</stack>
					</fadeFx>
				</stack>
				</template>
				
				<template #modal__footer>
						<btn class="" @click="closeModal">close</btn>
						<btn
						:class="modal.state !== '' ? 'btn-loading' : '' "
						:disabled="modal.state !== '' "
						@click="submit"
						>
							{{ modal.state !== '' ? modal.state : 'confirm'}}
						</btn>
				</template>
		</modal>
		<modal
			v-else-if="modal.visible && modal.type=='ticket-details' "
			:showClose="false"
			icon="&#x2713;"
			>
				<template #modal__title>
					<fadeFx  :totalElements="2">
						<h2>Success</h2>
					</fadeFx>
				</template>
				
				<template #default>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="2"
						>
						<stack size="sm">
							<h3>Your Ticket Details</h3>
							<p>You ticket was successfully registered. Keep the code below safe as you might need it to prove your registration for the event.</p>
							<stack size="xsm">
								<h5>Ticket code</h5>
								<p>{{modal.temp.data.ticket}}</p>
							</stack>
						</stack>
					</fadeFx>
				</template>

				<template #modal__footer>
					<section>
						<btn class="btn-danger" @click="$router.push({name:'home'})">Back to home</btn>
					</section>
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
	type _event = any
	interface _payload {
		event: _event,
		email: string,
		ticket_class?:ticketClassType | number,
		requested_information_answers: requestedInformationAnswerType[]
	}
	interface _data{
		event:_event,
		ticket_classes: ticketClassType[],
		ticket_class?: ticketClassType,
		requested_information: requestedInformationType[]
	}

    export default defineComponent({
		name:"Join",
        props: {},
        setup (props: any) {
			let routeDirection = ref<routeDirectionType>('forward')
			const $toasts: any = useToasts()
			const CONSTANTSX = CONSTANTS
            let step = ref<number>(1)
            let paymentRequired = ref<boolean>(false)
			let totalSteps = ref<number>(4)
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

            let data: _data= reactive({
				event:<_event>"",
				ticket_classes: <ticketClassType[]>[],
				requested_information: <requestedInformationType[]>[]
            })
            let requested_information_answers =  ref<requestedInformationAnswerType[]>([])
			let payload= reactive<_payload>({
				event: <_event>"",
				email: <string>"",
				requested_information_answers: <requestedInformationAnswerType[]>[]
            })
            
			// METHODS
			
		const resetData = ()=> {
			const initial = {
				event:<_event>"",
				ticket_classes: <ticketClassType[]>[],
				requested_information: <requestedInformationType[]>[]
			}
			Object.assign(data, initial)
		}
		const resetPayload = ()=> {
			const initial = {
				event: <_event>"",
				email: <string>"",
				requested_information_answers: <requestedInformationAnswerType[]>[]
            }
			Object.assign(payload, initial)
		}

        const summerize = ()=>{
            openModal("summary", 'summary')
        }
        const validate = async(fromNext=false )=>{
			let encounteredError = false
			if  (fromNext == true && step.value !== 2){
				if ( modal.type == ""){
					let submitBtn: HTMLElement = document.querySelector('#submit-form') as HTMLElement
					submitBtn.click()
				}
			}
			else{
				buttons.footer.primary.status = CONSTANTSX.busy
				buttons.footer.primary.disabled = true
				if (step.value==1){
					encounteredError = payload.event == "" ? true : false
				}
				else if (step.value==2){
					if (payload.ticket_class == undefined ){
						encounteredError  = true
						$toasts.ErrorToast('Error', "You must choose a class to proceed")
					}
				}
				else if (step.value==3){
					if(step.value==3){
						answerQuestions()
						for(let index=0; index < requested_information_answers.value.length; index++){
							let payload = requested_information_answers.value[index]
							await axios
								.post(`/api/v1/requested-information-answers/verify/`, 
									payload)
								.then( (response: ResponseObjectType) => {
								})
								.catch( (error: ResponseErrorObjectType) => {
									encounteredError = true
									$toasts.ErrorToast("Data invalid")
								})
						}
					}
					if (!encounteredError){
						let counter = data.requested_information.filter((x: requestedInformationType) => {
							return x.data.required && x.data.data.length==0
						})
						encounteredError = counter.length !==0 ? true : false
					}
				}
				else if (step.value==4){
					encounteredError = payload.email == "" ? true : false
				}
			
				if(encounteredError == false){

					if(step.value==4){
						summerize()
					}
					else if (step.value==1){
						await axios
						.get(`api/v1/events/${payload.event}`)
						.then(response => {
							openModal(response.data, 'event')
						})
						.catch(error => {
							if (error.response.status==404){
								$toasts.ErrorToast("Error", "Event not found")
							}
							else{
								$toasts.ErrorToast("Something went wrong")
							}
						})
					}
					else{
						next()
					}
				}
				buttons.footer.primary.status = ""
				buttons.footer.primary.disabled = false
			}

        }
        const parseDate = (raw: Date | string)=>{
			let date = new Date(raw)
			return String(date)
        }
        const addTicketClass = (x: responseTicketClassType)=>{
			let ticketClass = <ticketClassType>{} 
			ticketClass.id = data.ticket_classes.length+1
			ticketClass.data = {
				id: x.id,
				title: x.title,
				description: x.description,
				cost: x.cost
			}
			data.ticket_classes.push(ticketClass)
        }
        const addRequestedInfo = (x: reponseRequestedInformationType) => {
			let extraInfo = <requestedInformationType>{}
			extraInfo.id = data.requested_information.length+1
			extraInfo.data = {
				id: x.id,
				title: x.title,
				kind: x.kind,
				required: x.required,
				maxlength: x.maxlength,
				short_description: x.short_description,
				description: x.description,
				data: '',
			}
			data.requested_information.push(extraInfo)
        }
        const submit = async ()=>{
			modal.state = CONSTANTS.busy
			
			let ticket = ""
			let ticketDetails= {}
			let encounteredError = false

			await axios
				.post('/api/v1/tickets/', 
					payload)
				.then((response: ResponseObjectType) => {
					ticketDetails = response
					ticket = response.data.ticket
				})
				.catch((error: ResponseErrorObjectType) => {
					$toasts.ErrorToast("Something went wrong", "we weren't able to register your ticket.")
					encounteredError = true
				})
			
			if (!encounteredError){
				///////////////// submit the requested information answers
				for(let index=0; index < requested_information_answers.value.length; index++){
					let payload:any  = requested_information_answers.value[index]
					payload.ticket = ticket
					await axios
						.post(`/api/v1/requested-information-answers/`, 
							payload)
						.then( response => {

						})
						.catch( error => {
							encounteredError = true
							$toasts.ErrorToast("Something doesn't seem right with your answers to the requested questions")
						})
				}
			}
			if (!encounteredError){
				closeModal()
				$toasts.SuccessToast("Registration successful", "Your ticket was successfully registered")
				openModal(ticketDetails, 'ticket-details')
			}
			// else{
			// 	$toasts.ErrorToast("Something went wrong")
			// }
			

        }
        const answerQuestions = ()=>{
			data.requested_information.map((x: requestedInformationType) => {
				if (x.data.data.length !== 0){
					let data: requestedInformationAnswerType = {
						'requested_information': x.data.id,
						"answer"  :  x.data.data
					}
					requested_information_answers.value.push(data)
				}

			})
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

		const openModal = (data: any, type: any)=>{
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

		const selectModalData = async()=>{
			modal.state = CONSTANTS.busy
			if(modal.type=="event"){

				resetData()
				let event = payload.event
				resetPayload()
				
				payload.event = event
				await axios
					.get(`api/v1/events/${payload.event}/fetch/`)
					.then((response: ResponseObjectType) => {

						data.event  = response.data.event

						let raw_ticket_classes:  responseTicketClassType[] = response.data.ticket_classes
						raw_ticket_classes.map(x => {
							addTicketClass(x)
						})
						let raw_requested_info:  reponseRequestedInformationType[] = response.data.requested_information
						raw_requested_info.map(x => {
							addRequestedInfo(x)
						})
						step.value += 1
					})
					.catch((error: ResponseErrorObjectType) => {
						$toasts.ErrorToast("Something went wrong")
					})
			}
			else{
				payload.ticket_class= modal.temp.data.id
				data.ticket_class= modal.temp.data
				paymentRequired.value = modal.temp.data.cost == 0 ? false : true
			}
			closeModal()
		}
		const routeDirectionY = computed(() => {
				return routeDirection.value=='forward'? 'top' : 'bottom'
		})

            return {
				CONSTANTSX,
				step,
				totalSteps,
				buttons,
				modal,
				data,
				requested_information_answers,
				payload,
				paymentRequired,
				routeDirectionY,

				summerize,
				validate,
				parseDate,
				addTicketClass,
				addRequestedInfo,
				submit,
				answerQuestions,
				next,
				previous,
				openModal,
				closeModal,
				selectModalData
			}
        }
    })
</script>

<style scoped>

</style>