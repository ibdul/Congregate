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
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptile">Host an event</p>
					<h1 class="main__title">{{step}}. Basic Details</h1>
				</div>
				<form  id='form-1' class="L2" @submit.prevent="validate">
					<field-set
						field="Email" 
						type="email"
						placeholder="What is your email address?"
						help_text="This would be used whenever you need to get back to managing the event"
						:required="true"
						v-model="data.created_by"
					/>
					<field-set
						field="Event title" 
						placeholder="What is the name of the event"
						:required="true"
						v-model="data.title"
					/>
					<field-set
						field="Event type" 
						placeholder="What is the type of event"
						:required="true"
						v-model="data.kind"
					/>
					<field-set
						field="Date/Time" 
						type="datetime-local"
						:required="true"
						v-model="data.start_date"
					/>
					<field-set
						field="Venue" 
						placeholder="Where would the event hold"
						:required="true"
						v-model="data.venue"
					/>
					<field-set
						field="Description" 
						placeholder="What other information would you like your guests to know"
						type="textarea"
						:required="true"
						v-model="data.description"
					/>
					
					<input type="submit" hidden=true id="submit-1">
				</form>
			</main>

		</template>

		<template v-if="step==2">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptile">Host an event</p>
					<h1 class="main__title">{{step}}. Secondary Details</h1>
				</div>

				<form @submit.prevent="validate">
				<section class="L2">
				<info>
					<p>Would your guests be required to pay any fee?</p>
					<checkbox v-model="collapsibles.fees"/>
				</info>
				<transition name="collapsible">
				<div v-show="collapsibles.fees==true">
					<field-set
							field="account" 
							placeholder="Enter the account number where the payment would be made to"
							:required="collapsibles.fees==true"
							v-model="data.account"
						/>
						<!-- <field-set
							field="base cost" 
							:required="collapsibles.fees==true"
							placeholder="What would the regular guest have to pay?"
							v-model="data.base_cost"
						/> -->
				</div>
				</transition>
				</section>

				<section class="L2">
					<info>
						<p>How long do you expect the event to last?</p>
					</info>

					<field-set
						type="datetime-local"
						field="start date" 
						placeholder="When would the event start"
						v-model="data.start_date"
					/>
					<field-set
						type="datetime-local"
						field="end date" 
						placeholder="When would the event end"
						v-model="data.end_date"
					/>
				</section>

					<input type="submit" hidden=true id="submit-2">

				</form>

			</main>
		</template>

		<template id='3' v-if="step==3">
			<main class="main L1">
				<div class="main_header">
					<p class="main__suptile">Host an event</p>
					<h1 class="main__title">{{step}}. Guest Setup</h1>
				</div>
			<!--  -->
					<section class="L2">
						<info>
							<p>Would you like to collect some information about your guests?</p>
							<checkbox v-model="collapsibles.requested_info"/>
						</info>
						<div v-show="collapsibles.requested_info">
							<card-deck  class="card_deck-fluid L0">
								<card
									v-for="info in requested_info"
									:key="info.id"
									
									@click="openModal(info,'requested_info')"
									>
									{{info.data.title}}
								</card>

								<card
									class="add"

									@click="addModalData('requested_info')"
									>
									add
								</card>
								
							</card-deck>
						</div>
					</section>
					<!--  -->
					<section class="L2">
						<info>
							<p>Would you like to have different classes of guests?</p>
							<checkbox v-model="collapsibles.ticket_classes"/>
						</info>
						<div v-show="collapsibles.ticket_classes">
							<card-deck class="card_deck-fluid L0" >
								<card
									v-for="ticket_class in ticket_classes"
									:key="ticket_class.id"
									
									@click="openModal(ticket_class,'ticket_class')"
									>
									{{ticket_class.data.title}}
								</card>

								<card
									class="add"

									@click="addModalData('ticket_class')"
									>
									add
								</card>

							</card-deck>
						</div>
					</section>
					<!--  -->
					<!-- <form @submit.prevent="validate"> -->
					<field-set
						type="number"
						field="Guests capacity" 
						placeholder="Maximum number of guests"
						v-model="data.max_guests"
					/>
						<!-- <input type="submit" hidden=true id="submit-modal"> -->
					<!-- </form> -->
					<!--  -->
					
					<!-- <section class="L2">
							<info>
								<p>Do you wish to allow refunds?</p>
								<checkbox v-model="collapsibles.fees"/>
							</info>
							<div v-show="collapsibles.refundable">
							<form @submit.prevent="validate">

								<field-set
									type="date"
									field="deadline" 
									placeholder="up untill when?"
									:required="data.refundable==true"
									v-model="data.refund_deadline"
								/>
							<input type="submit" hidden=true id="submit-modal">
						</form>
							</div>
					</section> -->
			</main>
		</template>


		<footer class="footer">
			<btn
				class="btn-primary-clear"
				@click="validate(true)"
				v-if="(buttons.footer.primary.visible && step !== 3)"
				:disabled="buttons.footer.primary.disabled"
				:class="buttons.footer.primary.status==CONSTANTSX.busy ? 'btn-loading' : '' "
				>
                    {{buttons.footer.primary.text}}
            </btn>
            <btn
				class="btn-primary-clear"
				@click="summerize"
				v-if="step == 3"
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
			v-if="modal.visible && modal.type=='requested_info' "
			@close="closeModal"
			>
				<template #modal__title>
					<h4
						v-if="modal.editing == true"
						>
						{{modal.new ? 'Add a' : 'Edit'}} question for your guests
					</h4>
					<h4
						v-else
						>
						Question
					</h4>
				</template>
				<template #default>
					<section
						v-if="modal.editing == true"
						>
						<form @submit.prevent="validateModal">
							<field-set
									field="title" 
									placeholder="What would the field be called?"
									:required="true"
									v-model="modal.temp.data.title"
								/>
							<select
								placeholder="What type of data is expected for this field?"
								:required="true"
								v-model="modal.temp.data.kind"
								>
								<option v-for="(val, readable, index) in input_types" :key="index" :value="val">
									{{readable}}
								</option>
							</select>
							<field-set
										type="checkbox"
										field="required field ?" 
										placeholder="is this field a required field?"
										v-model="modal.temp.data.required"
								/>
							<field-set
										type="number"
										:max="200"
										field="maximum number of characters" 
										placeholder="How long should entries to this field be at maximum ( shouldn't exceed 123 characters ) ?"
										v-model="modal.temp.data.maxlength"
								/>
							<field-set
										type="textarea"
										field="short description" 
										:required="true"
										placeholder="Give a short description of what is expected in this field ?"
										v-model="modal.temp.data.short_description"
								/>
							<field-set
										type="textarea"
										field="description" 
										:required="true"
										placeholder="Give a description of why you need the info in this field ?"
										v-model="modal.temp.data.description"
								/>
							<input type="submit" hidden=true id="submit-modal-requested_info">
						</form>
					</section>
					<section
						v-else
						>
						<section>
							<h4>Title</h4>
							<p>{{modal.temp.data.title || '-'}}</p>
						</section>
						<section>
							<h4>Type</h4>
							<p>{{modal.temp.data.kind || '-'}}</p>
						</section>
						<section>
							<h4>Required</h4>
							<p>{{modal.temp.data.required || '-'}}</p>
						</section>
						<section>
							<h4>Max digits</h4>
							<p>{{modal.temp.data.maxlength || '-'}}</p>
						</section>
						<section>
							<h4>Short Description</h4>
							<p>{{modal.temp.data.short_description || '-'}}</p>
						</section>
						<section>
							<h4>Description</h4>
							<p>{{modal.temp.data.description || '-'}}</p>
						</section>
					</section>
				</template>
				<template #modal__footer>
					<section
						v-if="modal.editing == true"
						>
						<btn class="btn-danger" @click="discardModalData">discard</btn>
						<btn
						  :class="modal.state !== '' ? 'btn-loading' : '' "
						  :disabled="modal.state !== '' "
						  @click="validateModal(true)"
						  >
						  {{ modal.state !== '' ? modal.state : 'save'}}
						</btn>
					</section>
					<section
						v-else-if="modal.editing == false"
						>
						<btn class="btn-danger" @click="deleteModalData">delete</btn>
						<btn class="" @click="editModalData">edit</btn>
					</section>

				</template>
		</modal>
		<modal
			v-if="modal.visible && modal.type=='ticket_class' "
			@close="closeModal()"
			>
				<template #modal__title>
					<h4
						v-if="modal.editing == true"
						>
						{{modal.new ? 'Add a' : 'Edit'}} ticket class
					</h4>
					<h4
						v-else
						>
						Ticket class
					</h4>
				</template>
				<template #default>
					<section
						v-if="modal.editing == true"
						>
						<form @submit.prevent="validateModal">
									<field-set
											field="title" 
											placeholder="What would the class be called?"
											:required="true"
											v-model="modal.temp.data.title"
											
										/>
									<field-set
												type="number"
												:required="true"
												field="cost" 
												placeholder="how much would a ticket of this class cost?"
												v-model="modal.temp.data.cost"
										/>
									<field-set
										type="textarea"
										:required="true"
										field="description" 
										placeholder="Give a description of what the guests on the class would benefit ?"
										v-model="modal.temp.data.description"
								/>
								<input type="submit" hidden=true id="submit-modal-ticket_class">
							</form>
					</section>
					<section
						v-else
						>
						
						<section
							v-for="(val, data, id) in modal.temp.data" :key="id"
							>
							<h4>{{data}}</h4>
							<p>{{val || '-'}}</p>
						</section>
					</section>
							
				</template>
				<template #modal__footer>
					<section
						v-if="modal.editing == true"
						>
						<btn class="btn-danger" @click="discardModalData">discard</btn>
						<btn
						  :class="modal.state !== '' ? 'btn-loading' : '' "
						  :disabled="modal.state !== '' "
						  @click="validateModal(true)"
						  >
						  {{ modal.state !== '' ? modal.state : 'save'}}
						</btn>
					</section>
					<section
						v-else-if="modal.editing == false"
						>
						<btn
							class="btn-danger"
							v-if="modal.temp.deletable"
							@click="deleteModalData"
							>
							delete
							</btn>
						<btn class="" @click="editModalData">edit</btn>
					</section>

				</template>
		</modal>
		<modal
			v-if="modal.visible && modal.type=='summary' "
			@close="closeModal()"
			>
				<template #modal__title>
					<h4>Event Summary</h4>
				</template>
				<template #default>
					<section>
						<h3>Event Details</h3>
						<section>
							<h4>Event title</h4>
							<p>{{data.title || '-'}}</p>
						</section>
						<section>
							<h4>Type</h4>
							<p>{{data.kind || '-'}}</p>
						</section>
						<section>
							<h4>Venue</h4>
							<p>{{data.venue || '-'}}</p>
						</section>
						<section>
							<h4>Description</h4>
							<p>{{data.description || '-'}}</p>
						</section>
						<section>
							<h4>Date</h4>
							<p>{{data.start_date || '-'}}</p>
						</section>
						<section>
							<h4>End Date</h4>
							<p>{{data.end_date || '-'}}</p>
						</section>
						<section>
							<h4>Maximum number of guests</h4>
							<p>{{data.max_guests || '-'}}</p>
						</section>
						<section>
							<h4>Account Number</h4>
							<p>{{data.account || '-'}}</p>
						</section>
						<section>
							<h4>Email</h4>
							<p>{{data.created_by || '-'}}</p>
						</section>
					</section>

					<section>
						<h3>Ticket Classes</h3>
						<section
							v-for="ticket_class in ticket_classes" :key="ticket_class.id"
							>
							<section>
								<h4>Title</h4>
								<p>{{ticket_class.data.title || '-'}}</p>
								<h4>Description</h4>
								<p>{{ticket_class.data.description || '-'}}</p>
								<h4>Cost</h4>
								<p>{{ticket_class.data.cost || '-'}}</p>
							</section>
						</section>
						<h4 v-if="ticket_classes.length==0">-</h4>
					</section>

					<section>
						<h3>Extra Info</h3>
						<section
							v-for="info in requested_info" :key="info.id"
							>
							<h4>Title</h4>
							<p>{{info.data.title || '-'}}</p>
							<h4>Type</h4>
							<p>{{info.data.kind || '-'}}</p>
							<h4>Required</h4>
							<p>{{info.data.required}}</p>
							<h4>Maximum number of characters</h4>
							<p>{{info.data.maxlength || '-'}}</p>
							<h4>Short Description</h4>
							<p>{{info.data.short_description || '-'}}</p>
							<h4>Description</h4>
							<p>{{info.data.description || '-'}}</p>
						</section>
						<h4 v-if="requested_info.length==0">-</h4>
					</section>
							
				</template>
				<template #modal__footer>
					<section>
						<btn class="btn-danger" @click="discardModalData">back</btn>
						<btn
						  :class="modal.state !== '' ? 'btn-loading' : '' "
						  :disabled="modal.state !== '' "
						  @click="submit"
						  >
						  {{ modal.state !== '' ? modal.state : 'submit'}}
						</btn>
					</section>
				</template>
		</modal>
		<modal
			v-if="modal.visible && modal.type=='event-details' "
			:showClose="false"
			icon="&#x2713;"
			>
				<template #modal__title>
					<h4>Success</h4>
				</template>
				
				<template #default>
					<section>
						<h3>Your Event Details</h3>
						<p>You event was successfully registered. Keep these details safe as you would need them to manage your event.</p>
						<section>
							<h4>Event code</h4>
							<p>{{modal.temp.event}}</p>
						</section>
						<section>
							<h4>Pass code</h4>
							<p>{{modal.temp.pass}}</p>
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
	type modalType = "requested_info" | "ticket_class" | "summary" | "event-details"
	interface requestedInformationType {
		id: number,
		data:{
			event?: string,
			title: string,
			kind: string,
			required: boolean,
			maxlength?: string,
			short_description: string,
			description: string,
		}
	}
	interface ticketClassType {
		id: number,
		deletable?: boolean,
		data:{
			event?: string,
			title: string,
			description: string,
			cost: number,
		}
	}
	

	import CONSTANTS from '@/consumables/constants'
	import { useToasts } from '@/consumables/plugins'

	import { defineComponent, reactive, ref } from 'vue'

	export default defineComponent({
		name: 'Home',
		props:{},

		setup(props: any){
			const $toasts: any = useToasts()
			let step= ref(1)
			const CONSTANTSX = CONSTANTS
			let totalSteps= ref(3)
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
			let modal= reactive({
				type:"",
				state: "",
				visible: false,
				editing: false,
				tracker: Array as any,
				new: false,
				temp: Array as any,
			})
			let collapsibles= reactive({
				fees: false,
				requested_info: false,
				ticket_classes: false,
				refundable: false,
			})
			let data = reactive({
				title: "",
				kind: "",
				venue: "",
				description: "",
				start_date: null,
				end_date: null,
				max_guests: null,
				account: null,
				// "base_cost": null,
				refundable: false,
				refund_deadline: null,
				created_by: ""
			})
			let input_types = reactive({
				text: "text",
				number: "number",
				email: "email",
				'phone number': "tel",
				date: "date",
				time: "time",
				'date and time': "datetime-local",
				password: "password",
				'website link': "url",
			})
			let requested_info=  ref<requestedInformationType[]>([])
			let ticket_classes = ref<ticketClassType[]>([
				{
					id: 1,
					deletable: false,
					data:{
						title: 'regular',
						description: 'Generic class',
						cost: 0,
					}
				},
			])

		// METHODS
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
			const next = ()=>{
				if (step.value < totalSteps.value){
					step.value += 1
				}
				else{
					submit()
				}
			}
			const previous = ()=>{
				if (step.value != 1){
					step.value -= 1
				}
			}
			const validate = (fromButton=false)=>{
				let encounteredError = false
				if (fromButton==true){
					let submitBtn: HTMLElement = document.querySelector(`#submit-${step.value}`) as HTMLElement
					submitBtn.click()
				}
				else{
					// custom field checks
					if (!encounteredError){
						next()
					}
				}
			}
			const summerize = ()=>{
				openModal("summary", 'summary')
			}

			const submit = async () => {
				modal.state = CONSTANTS.busy
				let encounteredError = false
				let responseData = {}
				let event_code = ""

				let response = fakeRequest('/api/v1/events/', data)
					if(response) {
						const receivedResponseData = {
							'event' : 'someRandomToken',
							'pass' : 'someRandomPasswordToken'
						}
						responseData = receivedResponseData
						event_code = receivedResponseData.event
					}
					else {
						encounteredError = true
						$toasts.ErrorToast("Something went wrong", "we weren't able to register your event.")
					}
				
				if (!encounteredError){

					///////////////// SUBMIT THE CLASSES
					for(let index=0; index < ticket_classes.value.length; index++){
						let payload = ticket_classes.value[index].data
						payload.event = event_code
						let response = fakeRequest(`/api/v1/ticket-classes/`, payload)
							if (response) {
							}
							else{
								encounteredError = true
								$toasts.ErrorToast("Something went wrong", 'There seems to be some error in one of your ticket classes.')
							}
					}
					///////////////// SUBMIT THE REQUESTED INFO
					for(let index=0; index < requested_info.value.length; index++){
						let payload = requested_info.value[index].data
						payload.event = event_code
						let response = fakeRequest(`/api/v1/requested-info/`, payload)
						if(response) {
						}
						else {
							encounteredError = true
							$toasts.ErrorToast("Something went wrong", 'There seems to be some error in one of your extra information requests.')
						}
					}

				}
				if (!encounteredError){
					modal.state = "idle"
					closeModal()
					$toasts.SuccessToast("Registration successful", "Your event was successfully registered")
					openModal(responseData, 'event-details')
				}
				else{
					$toasts.ErrorToast("Something went wrong")
				}
			}

			/////////////////////////// EXTRA INFO RELATED METHODS

			const validateModal = (fromButton=false) => {
				
				let encounteredError= false
				let ext = ""
				if(fromButton==true){
					if (modal.type == 'requested_info'){
						ext = "requested_info"
					}
					else if (modal.type == 'ticket_class'){
						ext = "ticket_class"
					}
					let submitBtn: HTMLElement = document.querySelector(`#submit-modal-${ext}`) as HTMLElement
					submitBtn.click()
				}
				else{
					if (modal.temp.data.title == ""){
							$toasts.ErrorToast("You must include a title")
							encounteredError =  true
					}
					if (modal.type == "requested_info"){
						if (modal.temp.data.kind == "" || modal.temp.data.kind == null ){
							$toasts.ErrorToast("You must choose a type of question")
							encounteredError =  true
						}
						if (modal.temp.data.short_description == ""){
							$toasts.ErrorToast("Your question must have a short description", "it would serve as the actual question the guest sees.")
							encounteredError =  true
						}
					}
					if (!encounteredError){
						saveModalData()
					}
				}
			}

			const copyToModalTemp = ()=>{
				// this makes a deep copy of tango from the tracker to the temporary space
				modal.temp = JSON.parse(JSON.stringify(modal.tracker))
			}
			const resetModalTemp = ()=>{
				// resets the temporary space back to an empty guest class
				if (modal.type == "requested_info"){
					modal.temp =  {
						id: '',
						data:{
							title: '',
							kind: '',
							required: true,
							maxlength:'',
							short_description: '',
							description: '',
						}
					}
				}
				else if(modal.type == "ticket_class"){
					modal.temp =  {
						id:'',
						data:{
							title: '',
							description: '',
							cost: ''
						}
					}
				}
			}
			const openModal = (data: any, type: string) => {
				// opens the modal used for displaying the guest classes
				
				/* 

				it works by setting the visibility to true 
				then it makes a shallow copy of tango into the tracker
				and finallly makes use of the previous method to make a shallow copy into the temporary space

				*/

				modal.type = type
				modal.visible = true
				modal.tracker = data
				copyToModalTemp()
				
			}

			const closeModal = ()=>{
				// closes the modal

				/* 
				
				works in recursively
				if editing hasnt been explicitely closed;
					* it closes it
					* it also sets the flag for tracking if tango is a new entry to false

				else;
					* it resets the temporary space
					* and then resets the tracker
					* it then closes the modal
				
				*/

				if (modal.editing){
					modal.new = false
					modal.editing = false
					closeModal()
				}
				else{
					resetModalTemp()
					modal.tracker = ''
					modal.visible = false
				}
				modal.state = ''
				modal.type = ""
			}
			const editModalData = ()=>{
				// sets the editing flag on
				modal.editing = true;
			}
			const deleteModalData = () =>{
				// deletes tango from the array using a filter 
				// it checks through the array, adding all elements except where the element is  tango
				// it then closes the modal 
				if (modal.type == "requested_info"){
					requested_info.value = requested_info.value.filter((requested_info: requestedInformationType) => requested_info !== modal.tracker)
				}
				else if(modal.type == "ticket_class"  && modal.temp.deletable){
					ticket_classes.value = ticket_classes.value.filter((ticket_class: ticketClassType) => ticket_class !== modal.tracker)
				}

				closeModal()
			}
			
			const saveModalData = async()=>{
				// saves tango
				/* 
				
				if tango is a new entry;
					* it appends it to the list of guest clases
					* then sets the tracker to tango (as in the last entry of the guest classes list)
					* then calls the discard methods that takes us back to a read mode tango

				else;
					* set the title and amount on the tracker to what is contained in the temporary space (as that is the new edit)
					* this affects tango as the tracker is essentially a pointer to the same storage space as the original tango
					* then it calls discard method 
				
				*/
				// document.querySelector(`#submit-modal-${this.modal.type}`).click()
				modal.state = CONSTANTS.busy

				// let valid = this.validateModal()

				let url="ticket-classes"
				if (modal.type == "requested_info"){
					url = "requested-info"
				}
				let response = fakeRequest(`/api/v1/${url}/verify/`, modal.temp.data)
					if(response) {
						if (modal.new){
							modal.new = false
							if (modal.type == "requested_info"){
								requested_info.value.push(modal.temp)
								modal.tracker = requested_info.value[requested_info.value.length - 1]
							}
							else if(modal.type == "ticket_class"){
								ticket_classes.value.push(modal.temp)
								modal.tracker = ticket_classes.value[ticket_classes.value.length - 1]
							}
						}
						else {
							modal.tracker.data = modal.temp.data
						}
						discardModalData()
					}
					else {
						$toasts.ErrorToast("Something doesn't seem right")
					}
			}
			const discardModalData = ()=>{
				/*
				
				if tango is a new entry;
					then it means changes are discarded and a new entry shouldnt be added
					in this case, the function just closes the modal all together

				else;
					* it runs the copy to temp function to reset the temp storage back to the whats held in the tracker
						this means any unsaved changes made to tango would be discarded as the tracker would still contain the exact values it got from tango initially
						if changes were already saved then the temp space would reflect the new values
					* then it sets the editing flag to false.
						that makes the modal go back to the read only mode

				*/

				if (modal.new){
					closeModal()
				}
				else{
					copyToModalTemp()
					modal.editing = false
				}
				// this.closeExtraInfoModal()
				// todo
				// use confirmation
			}
			const addModalData = (type: modalType) =>{
				// used to add a new tango

				/* 
				
				* it initializes a new tango with empty values
					and an id that equals the length of the guest classes list
				* then it opens a modal with this new empty tango 
				* then it sets the new flag to true to keep track that we're making a new entry
				* then it opens the modal in editing mode
				
				*/
				let payload = {}

				if (type == "requested_info"){
					payload = {
						id: requested_info.value.length+1,
						data:{
							title: '',
							kind: '',
							required: false,
							maxlength:'',
							short_description: '',
							description: '',
						}
					};
				}
				else if(type == "ticket_class"){
					payload = {
						id: ticket_classes.value.length+1,
						deletable: true,
						data:{
							title: '',
							description: '',
							cost: ''
						}
					};
				}
				modal.new = true
				openModal(payload, type)
				editModalData()

			}
			

			return{
				CONSTANTSX,

				step,
				totalSteps,
				buttons,
				modal,
				collapsibles,
				data,
				input_types,
				requested_info,
				ticket_classes,
				
				
				next,
				previous,
				validate,
				summerize,
				submit,

				validateModal,
				copyToModalTemp,
				resetModalTemp,
				openModal,
				closeModal,
				editModalData,
				deleteModalData,
				saveModalData,
				discardModalData,
				addModalData

			}
		}
	})

</script>

<style lang="scss">
	.dots{
		list-style-type: none;
		margin: 0;
		padding: 0;
		display: inline-flex;

		&>*+*{
			margin-left: 4px;
		}

		&_item{
			border-radius: 50%;
			height: 1ch;
			width: 1ch;
			background-color: transparent;
			border: .5ch solid $c2-1;
			transition: 1s ease;

			&-active{
				transform: translateY(-4px);
				border-color: $c2;
			}
		}

	}

</style>