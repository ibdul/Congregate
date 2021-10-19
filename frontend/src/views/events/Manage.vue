<template>
	<div class="container">
		
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
	
	<dots
		:step='step'
		:total='totalSteps'
	/>

		<template v-if="step==1">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptitle">Manage event</p>
					<h1 class="main__title">{{step}}. Find event</h1>
				</div>
				<form  id='form-1' class="L2" @submit.prevent="validate()">
					<field-set
						field="event code" 
						placeholder="What is the code to your event?"
						v-model="payload.event"
						:required="true"
					/>
					<field-set
						field="event pass code" 
						placeholder="What is the pass code of the event?"
						v-model="payload.pass"
						:required="true"
					/>
					
					<input type="submit" hidden=true id="submit-form">
				</form>
			</main>
		</template>
		
		<template v-if="step==2">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptitle">Manage event</p>
					<h1 class="main__title">{{step}}. Guests list</h1>
					<p class="main__subtitle" v-if="data.tickets.length">Click on a guest to see more details.</p>
				</div>
				<div>

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
								<td>{{id}}</td>
								<td>{{ticket.ticket_class}}</td>
								<td>{{ticket.email}}</td>
								<td>{{ticket.code}}</td>
							</tr>
						</tbody>
					</table>
				</div>
			</main>
		</template>

		<footer class="footer">

			<p v-if="step == totalSteps">
				{{data.tickets.length}} ticket<template v-if="data.tickets.length>1">s</template> registered.
			</p>
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
				@click="previous"
				v-if="buttons.footer.secondary.visible && step !== 1"
				:disabled="buttons.footer.secondary.disabled"
				>
                    {{buttons.footer.secondary.text}}
            </btn>
			
        </footer>

		<modal
			v-if="modal.visible && modal.type=='ticket' "
			@close="closeModal()"
			>
				<template #modal__title>
						<h4>Ticket</h4>
				</template>
				<template #default>
					<section>
						<h3 class="section__title">Basic ticket information</h3>
						<section>
							<h4>Ticket Code</h4>
							<p>{{modal.temp.code}}</p>
						</section>
						<section>
							<h4>TIcket Class</h4>
							<p>{{modal.temp.ticket_class}}</p>
						</section>
						<section>
							<h4>Email</h4>
							<p>{{modal.temp.email}}</p>
						</section>
					</section>

					<section>
						<h3 class="section__title">Requested data</h3>
						<section
								v-for="(field, id) in modal.temp.requested_information_answers"
								:key="id"
								>
								<h4>{{field.requested_information}}</h4>
								<p>{{field.answer}}</p>
						</section>
						<h4 v-if="modal.temp.requested_information_answers.length==0">No data to display</h4>
					</section>
					
					<!-- <section>
						<h3 class="section__title">Required data</h3>
						<section>
							<h4>Email</h4>
							<p>{{payload.email}}</p>
						</section>
					</section> -->
				</template>
				
				<template #modal__footer>
						<btn class="" @click="closeModal">close</btn>
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
		responseTicketClassType,
		ticketClassType,
		reponseRequestedInformationType,
		ResponseObjectType,
		ResponseErrorObjectType
		} from '@/consumables/typings'

	import { defineComponent, reactive, ref } from 'vue'
	
	interface _payloadType{
		event: string,
		pass: string,
	}
	type _modalTypes = 'ticket'

    export default defineComponent({

        setup (props: any, context: any) {
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
			const fakeData: any = {
				event: {
					account: null,
					code: "lyvr3ind",
					created_by: "ibdul1999@gmail.com",
					description: "farmers hangout",
					end_date: null,
					kind: "party",
					max_guests: null,
					refund_deadline: null,
					refundable: false,
					start_date: "2021-10-17T00:14:00Z",
					title: "Cultiv8",
					venue: "Zero's farm yard",
				},
				requested_information: [
					{
						description: "We need this info in order to keep our records clean",
						event: "lyvr3ind",
						id: 1,
						kind: "text",
						maxlength: 123,
						required: false,
						short_description: "please tell us your nickname",
						title: "nickname",
					}
				],
				ticket_classes: [
					{
						cost: "0.00",
						description: "Generic class",
						event: "lyvr3ind",
						id: 1,
						title: "regular"
					},
					{
						cost: "123.00",
						description: "asdf",
						event: "lyvr3ind",
						id: 2,
						title: "Shark",
					},
				],
				tickets: [
					{
						code: "ecs8hfqb8",
						email: "ibdul1999@gmail.com",
						event: "lyvr3ind",
						requested_information_answers: [
							{
								requested_information: "nickname",
								answer: "ibdul"
							}
						],
						ticket_class: "regular",
					},
					{
						code: "91g9luh72",
						email: "someRandomemail@gmail.com",
						event: "lyvr3ind",
						requested_information_answers: [],
						ticket_class: "regular",
					}
				]
			}

			/////// METHODS

			const fakeRequest = (fakeAddress: string, data:any) => {
				let milliseconds = 200
				const date = Date.now()
				let currentDate = null
				do {
					currentDate = Date.now()
				}
				while (currentDate - date < milliseconds)
				return true
			}

			const validate =async(fromNext=false)=>{

				buttons.footer.primary.status = CONSTANTS.busy
				buttons.footer.primary.disabled = true

				let encounteredError = false
				if(fromNext){
					let submitBtn: HTMLElement = document.querySelector('#submit-form') as HTMLElement
					submitBtn.click()
				}
				else{
					if(step.value == 1){

						let fakeResponse = fakeRequest(`/api/v1/events/manage/`, payload)
							if (fakeResponse){
								$toasts.SuccessToast("Event matched")
								Object.assign(data, fakeData)
							}
							else{
								$toasts.ErrorToast("Something went wrong")
							}
					}
					if(encounteredError==false){
						next()
					}
				}
					buttons.footer.primary.status = ""
					buttons.footer.primary.disabled = false
			}
			const next = ()=>{
				if (step.value < totalSteps.value){
					step.value += 1
				}
			}
			const previous = ()=>{
				if (step.value != 1){
					step.value -= 1
				}
			}
			const openModal = (data: any, type: _modalTypes)=>{
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
				$toasts.ErrorToast("functionality requires some backend magic")
			}

		return{
			CONSTANTSX,
			step,
			totalSteps,
			buttons,
			modal,
			payload,
			data,

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
			max-width: 20ch;
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