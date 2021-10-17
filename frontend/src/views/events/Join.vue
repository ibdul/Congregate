<template>
<div class="container">

    <header class="header">
            <btn class="btn-primary-clear"
				@click="$router.push({name: 'home'})"
				>
                    Home
            </btn>
        </header>

		<dots
			:step='step'
			:total='totalSteps'
		/>

        <template v-if="step==1">

			<main class="main ">
				<div class="main_header">
					<p class="main__suptitle">Join an event</p>
					<h1 class="main__title">{{step}}. Find event</h1>
					<p class="main__subtitle">Enter a valid event code to proceed.</p>
				</div>
				<form class="" @submit.prevent="validate">
					
					<field-set
						field="event code" 
						placeholder="What is the code to the event you want to join"
						v-model="payload.event"
						:required="true"
					/>
					<input type="submit" hidden=true id="submit-form">
				</form>
			</main>
		</template>

        <template v-if="step==2">

			<main class="main ">
				<div class="main_header">
					<p class="main__suptitle">Join an event</p>
					<h1 class="main__title">{{step}}. Class selection</h1>
					<p class="main__subtitle"> Click on a card to get it's details.</p>

				</div>
					<card-deck class="card_deck">
						<card v-for="card in data.ticket_classes" :key="card.id"
							:class="payload.ticket_class == card.data.id ? 'card-active' : '' "
							@click="openModal(card,'class')"
							>
							{{card.data.title}}
						</card>
					</card-deck>
			</main>
		</template>

        <template v-if="step==3">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptitle">Join an event</p>
					<h1 class="main__title">{{step}}. Requested Information</h1>
					<p class="main__subtitle">Fill in the information below as requested by the event organizers.</p>
				</div>
				<form class="L2" @submit.prevent="validate">
					<field-set
						v-for="field in data.requested_info"
						:key="field.id"
						:field="field.data.title" 
						:type="field.data.kind"
						:maxlength="field.data.maxlength"
						:placeholder="field.data.short_description"
						:help_text="field.data.description"
						:required="field.data.required"

						v-model="field.data.data"
					/>
					<h4 v-if="data.requested_info.length==0">No requested data. Please click next to proceed</h4>

					<input type="submit" hidden=true id="submit-form">
				</form>
			</main>

		</template>
		
		<template v-if="step==4">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptitle">Join an event</p>
					<h1 class="main__title">{{step}}. Payment Information</h1>
					<template v-if="paymentRequired">
						<p class="main__subtitle">Your Selection requires you to pay a fee.</p>
						<p class="main__subtitle">Fill the information below to proceed.</p>
					</template>
					<template v-else>
						<p class="main__subtitle">Your Selection doesn't require any fee.</p>
						<p class="main__subtitle">Fill the information below and then proceed.</p>
					</template>
				</div>

					<template v-if="paymentRequired">
						<h3>
							payment funtionality coming soon!
						</h3>
					</template>

				<form class="L2" @submit.prevent="validate">
					<field-set
						field="email" 
						placeholder="Enter  your email"
						type="email"
						:required="true"
						v-model="payload.email"
					/>
					<input type="submit" hidden=true id="submit-form">
				</form>
			</main>

		</template>

		<footer class="footer">
			<btn
				class="btn-primary-clear"
				@click="validate(true)"
				v-if="(buttons.footer.primary.visible && step !== totalSteps)"
				:disabled="buttons.footer.primary.disabled"
				:class="buttons.footer.primary.status==CONSTANTSX.busy ? 'btn-loading' : '' "
				>
                    {{buttons.footer.primary.text}}
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

        <modal
            v-if="modal.visible && modal.type=='event' "
            @close="closeModal()"
            >
                <template #modal__title>
                        <h4>Find an event</h4>
                </template>
                <template #default>
                    <section>
                        <section>
                            <h4>Title</h4>
                            <p>{{modal.temp.title}}</p>
                        </section>
                        <section>
                            <h4>Type of event</h4>
                            <p>{{modal.temp.kind}}</p>
                        </section>
                        <section>
                            <h4>Date Of Event</h4>
                            <p>{{parseDate(modal.temp.start_date)}}</p>
                        </section>
                        <section>
                            <h4>Venue</h4>
                            <p>{{modal.temp.venue}}</p>
                        </section>
                        <section>
                            <h4>Description</h4>
                            <p>{{modal.temp.description}}</p>
                        </section>
                    </section>
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
                        <h4>Select a ticket class</h4>
                </template>
                <template #default>
                    <section
                        v-for="(val, item, id) in modal.temp.data"
                        :key="id"
                        >
                        <section v-if="item !== 'id'">
                            <h4>{{item}}</h4>
                            <p>{{val}}</p>
                        </section>
                    </section>
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
                        <h4>Summary of your ticket data</h4>
                </template>
                <template #default>
                    <section>
                        <h3 class="section__title">Basic ticket information</h3>
                        <section>
                            <h4>Event Title</h4>
                            <p>{{data.event.title}}</p>
                        </section>
                        <section>
                            <h4>TIcket Class</h4>
                            <p>{{data.ticket_class.title}}</p>
                        </section>
                        <section>
                            <h4>Ticket Cost</h4>
                            <p>{{data.ticket_class.cost}}</p>
                        </section>
                    </section>

                    <section>
                        <h3 class="section__title">Data requested by event organizers</h3>
                        <section
                                v-for="field in data.requested_info"
                                :key="field.id"
                                >
                                <h4>{{field.data.title}}</h4>
                                <p>{{field.data.data.length!==0? field.data.data : '-'}}</p>
                        </section>
                        <h4 v-if="data.requested_info.length==0">No requested data. Please click next to proceed</h4>
                    </section>
                    
                    <section>
                        <h3 class="section__title">Required data</h3>
                        <section>
                            <h4>Email</h4>
                            <p>{{payload.email}}</p>
                        </section>
                    </section>
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
                    <h4>Success</h4>
                </template>
                
                <template #default>
                    <section>
                        <h3>Your Ticket Details</h3>
                        <p>You ticket was successfully registered. Keep the code below safe as you might need it to prove your registration for the event.</p>
                        <section>
                            <h4>Ticket code</h4>
                            <p>{{modal.temp.ticket}}</p>
                        </section>
                    </section>
                </template>

                <template #modal__footer>
                    <section>
                        <btn class="btn-danger" @click="$router.push({name:'home'})">Back to home</btn>
                    </section>
                </template>

        </modal>

</div>
</template>

<script lang="ts">

	import CONSTANTS from '@/consumables/constants'
	import { useToasts } from '@/consumables/plugins'
    import { 
		requestedInformationType,
		requestedInformationAnswerType,
		ticketClassType,
		} from '@/consumables/typings'

	import { defineComponent, reactive, ref } from 'vue'
	type _event = any
	interface _payload {
		event: _event,
		email: string,
		ticket_class?:ticketClassType | number,
		requested_info_answers: requestedInformationAnswerType[]
	}
	interface _data{
		event:_event,
		ticket_classes: ticketClassType[],
		ticket_class?: ticketClassType,
		requested_info: requestedInformationType[]
	}

    export default defineComponent({
		name:"Join",
        props: {},
        setup (props: any) {
			const $toasts: any = useToasts()
			const fakeEvent = {
				id: 234,
				event: 234,
				title: "Moon meet",
				kind: "Raving",
				start_date: "12-08-2019",
				description: "Let's Rave on the actual Moon",
				venue: "The Moon",
				ticket_classes: [
					{
						id: 12,
						title: "Space monkey",
						description: "Get your suits and supplies at the meet",
						cost: 123
					},
					{
						id: 13,
						title: "Space Shark",
						description: "You bring all your supplies",
						cost: 23
					},
					{
						id: 15,
						title: "Space Worm",
						description: "Your stay with a friend of a higher ticket class",
						cost: 5
					},
				],
				requested_information:[
					{
						id: 12,
						title: 'name',
						kind: 'text',
						required: true,
						maxlength: 123,
						short_description: 'Please tell us your name',
						description: 'this would be necessary to allot seats',
						data: {},
					},
					{
						id: 5,
						title: 'phone',
						kind: 'tel',
						required: false,
						maxlength: 20,
						short_description: 'Provide a phone number',
						description: 'this would be useful in case we need to make calls to you back on earth',
						data: {},
					}
				]
			}
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
				requested_info: <requestedInformationType[]>[]
            })
            let requested_info_answers =  ref<requestedInformationAnswerType[]>([])
			let payload= reactive<_payload>({
				event: <_event>"",
				email: <string>"",
				requested_info_answers: <requestedInformationAnswerType[]>[]
            })
            
			// METHODS

		const fakeRequest = (fakeAddress: string, data:any) => {
			let milliseconds = 500
			const date = Date.now()
			let currentDate = null
			do {
				currentDate = Date.now()
			}
			while (currentDate - date < milliseconds)
			return true
		}
		const resetData = ()=> {
			const initial = {
				event:<_event>"",
				ticket_classes: <ticketClassType[]>[],
				requested_info: <requestedInformationType[]>[]
			}
			Object.assign(data, initial)
		}
		const resetPayload = ()=> {
			const initial = {
				event: <_event>"",
				email: <string>"",
				requested_info_answers: <requestedInformationAnswerType[]>[]
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
						for(let index=0; index < requested_info_answers.value.length; index++){
							let payload = requested_info_answers.value[index]
							let fakeResponse = fakeRequest(`/api/v1/requested-info-answers/verify/`, payload)
								if(fakeResponse){
								}
								else{
									encounteredError = true
									$toasts.ErrorToast("Data invalid")
								}
						}
					}
					if (!encounteredError){
						let counter = data.requested_info.filter((x: requestedInformationType) => {
							return x.data.required && x.data.data.length==0
						})
						encounteredError = counter.length !==0 ? true : false
					}
				}
				else if (step.value==4){
					encounteredError = payload.email == "" ? true : false
				}
			
				if(encounteredError == false){
					buttons.footer.primary.text = CONSTANTS.busy
					buttons.footer.primary.disabled = true

					if(step.value==4){
						summerize()
					}
					else if (step.value==1){
					let fakeResponse = fakeRequest(`api/v1/events/${payload.event}`, {})
						if (fakeResponse){
							openModal(fakeEvent, 'event')
						}
						else{
								$toasts.ErrorToast("Something went wrong")
						}
						buttons.footer.primary.text = "next"
						buttons.footer.primary.disabled = false
					}
					else{
						next()
					}
				}
			}
        }
        const parseDate = (raw: Date | string)=>{
			let date = new Date(raw)
			return String(date)
        }
        const addTicketClass = (x: any)=>{
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
        const addRequestedInfo = (x: any) => {
			let extraInfo = <requestedInformationType>{}
			extraInfo.id = data.requested_info.length+1
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
			data.requested_info.push(extraInfo)
        }
        const submit = async ()=>{
			modal.state = CONSTANTS.busy
			
			let ticket = ""
			let ticketDetails= {}
			let encounteredError = false

			let fakeResponse = fakeRequest('/api/v1/tickets/', payload)
				if(fakeResponse){
					const fakeResponseObj = {
						ticket: "someRandomTicketToken"
					}
					ticketDetails = fakeResponseObj
					ticket = fakeResponseObj.ticket
				}
				else{
					$toasts.ErrorToast("Something went wrong", "we weren't able to register your ticket.")
					encounteredError = true
				}
			
			if (!encounteredError){
				///////////////// submit the requested information answers
				for(let index=0; index < requested_info_answers.value.length; index++){
					let payload:any  = requested_info_answers.value[index]
					payload.ticket = ticket
					let fakeResponse = fakeRequest(`/api/v1/requested-info-answers/`, payload)
						if(fakeResponse){

						}
						else{
							encounteredError = true
							$toasts.ErrorToast("Something doesn't seem right with your answers to the requested questions")
						}
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
			data.requested_info.map((x: requestedInformationType) => {
				if (x.data.data.length !== 0){
					let data: requestedInformationAnswerType = {
						'requested_info': x.data.id,
						"answer"  :  x.data.data
					}
					requested_info_answers.value.push(data)
				}

			})
        }
        const next = ()=>{

			buttons.footer.primary.text = "next"
			buttons.footer.primary.disabled = false
			step.value += 1
		}
		const previous = () =>{
			if (step.value > 1){
				step.value -= 1
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
					let fakeResponse = fakeRequest(`api/v1/events/${payload.event}/fetch/`, {})
					if(fakeResponse){


						data.event  = fakeEvent.event

						let raw_ticket_classes:  any[] = fakeEvent.ticket_classes
						raw_ticket_classes.map(x => {
							addTicketClass(x)
						})
						let raw_requested_info:  any[] = fakeEvent.requested_information
						raw_requested_info.map(x => {
							addRequestedInfo(x)
						})
						step.value += 1
					}
					else{
						$toasts.ErrorToast("Something went wrong")
					}
			}
			else{
				payload.ticket_class= modal.temp.data.id
				data.ticket_class= modal.temp.data
				paymentRequired.value = modal.temp.data.cost == 0 ? false : true
			}
			closeModal()
		}

            return {
				CONSTANTSX,
				step,
				totalSteps,
				buttons,
				modal,
				data,
				requested_info_answers,
				payload,
				paymentRequired,

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