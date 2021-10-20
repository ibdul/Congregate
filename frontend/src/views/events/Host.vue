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
					:totalElements="7"
					>
					<stack size="z">
						<p class="page_suptitle">Host an event</p>
						<h1 class="page_title">{{step}}. Basic Details</h1>
					</stack>
				</fadeFx>
					<stack>
					<form  id='form-1' class="stack_pass" @submit.prevent="validate">
						<fadeFx
							:to="routeDirectionY"
							:delay="2"
							:totalElements="7"
							>
							<field-set
								field="Email" 
								type="email"
								placeholder="What is your email address?"
								help_text="This would be used whenever you need to get back to managing the event"
								:required="true"
								v-model="data.created_by"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="3"
							:totalElements="7"
							>
							<field-set
								field="Event title" 
								placeholder="What is the name of the event"
								:required="true"
								v-model="data.title"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="4"
							:totalElements="7"
							>
							<field-set
								field="Event type" 
								placeholder="What is the type of event"
								:required="true"
								v-model="data.kind"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="5"
							:totalElements="7"
							>
							<field-set
								field="Date/Time" 
								type="datetime-local"
								:required="true"
								v-model="data.start_date"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="6"
							:totalElements="7"
							>
							<field-set
								field="Venue" 
								placeholder="Where would the event hold"
								:required="true"
								v-model="data.venue"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="7"
							:totalElements="7"
							>
							<field-set
								field="Description" 
								placeholder="What other information would you like your guests to know"
								type="textarea"
								:required="true"
								v-model="data.description"
							/>
						</fadeFx>
						
						<input type="submit" hidden=true id="submit-1">
					</form>
					</stack>
			</template>

			<template v-else-if="step==2">
				<fadeFx
					:to="routeDirectionY"
					:totalElements="5"
					>
					<stack size="z">
						<p class="page_suptitle">Host an event</p>
						<h1 class="page_title">{{step}}. Secondary Details</h1>
					</stack>
				</fadeFx>
					<stack>
					<form @submit.prevent="validate" class="stack_pass">
					<stack size="sm">
					<fadeFx
						:to="routeDirectionY"
						:delay="2"
						:totalElements="5"
						>
						<info>
							<p>Would your guests be required to pay any fee?</p>
							<checkbox v-model="collapsibles.fees"/>
						</info>
					</fadeFx>
					<transition name="collapsible">
					<div v-show="collapsibles.fees==true">
						<field-set
								field="account" 
								type="number"
								placeholder="Enter the account number where the payment would be made to"
								:required="collapsibles.fees==true"
								v-model="data.account"
							/>
							<field-set
								field="base cost" 
								type="number"
								:required="collapsibles.fees==true"
								placeholder="What would the regular guest have to pay?"
								v-model="ticket_classes[0].data.cost"
							/>
					</div>
					</transition>
					</stack>

					<stack size="sm">
						<fadeFx
							:to="routeDirectionY"
							:delay="3"
							:totalElements="5"
							>
							<info>
								<p>How long do you expect the event to last?</p>
							</info>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="4"
							:totalElements="5"
							>
							<field-set
								type="datetime-local"
								field="start date" 
								placeholder="When would the event start"
								v-model="data.start_date"
							/>
						</fadeFx>
						<fadeFx
							:to="routeDirectionY"
							:delay="5"
							:totalElements="5"
							>
							<field-set
								type="datetime-local"
								field="end date" 
								placeholder="When would the event end"
								v-model="data.end_date"
							/>
						</fadeFx>
					</stack>

						<input type="submit" hidden=true id="submit-2">

					</form>
					</stack>


			</template>

			<template id='3' v-else-if="step==3">
				<fadeFx
					:to="routeDirectionY"
					:totalElements="4"
					>
					<stack size="z">
						<p class="page_suptitle">Host an event</p>
						<h1 class="page_title">{{step}}. Guest Setup</h1>
					</stack>
				</fadeFx>
				<!--  -->
					<stack>
						<stack size="sm">
							<fadeFx
								:to="routeDirectionY"
								:delay="2"
								:totalElements="4"
								>
								<info>
									<p>Would you like to collect some information about your guests?</p>
									<checkbox v-model="collapsibles.requested_information"/>
								</info>
							</fadeFx>
					<transition name="collapsible">
							<div v-show="collapsibles.requested_information">
								<card-deck>
									<fadeFx
										v-for="info in requested_information"
										:key="info.id"

										:to="routeDirectionY"
										:delay="2+ info.id"
										>
										<card
											
											@click="openModal(info,'requested_information')"
											>
											{{info.data.title}}
										</card>
									</fadeFx>
									<fadeFx
										:to="routeDirectionY"
										:delay="requested_information.length+2"
										:totalElements="requested_information.length+2"
										>
										<card
											class="add"

											@click="addModalData('requested_information')"
											>
											add
										</card>
									</fadeFx>
									
								</card-deck>
							</div>
						</transition>
						</stack>
						<!--  -->
						<stack size="sm">
							<fadeFx
								:to="routeDirectionY"
								:delay="3"
								:totalElements="4"
								>
								<info>
									<p>Would you like to have different classes of guests?</p>
									<checkbox v-model="collapsibles.ticket_classes"/>
								</info>
							</fadeFx>
						<transition name="collapsible">
							<div v-show="collapsibles.ticket_classes">
								<card-deck>
									
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
						</transition>
						</stack>
						
						<fadeFx
							:to="routeDirectionY"
							:delay="4"
							:totalElements="4"
							>
							<field-set
								type="number"
								field="Guests capacity" 
								placeholder="Maximum number of guests"
								v-model="data.max_guests"
							/>
						</fadeFx>
							
					</stack>

			</template>
		</stack>

	<fadeFx>
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
	</fadeFx>
	</div>

	<transition name="modal">
		<modal
			v-if="modal.visible && modal.type=='requested_information' "
			@close="closeModal"
			>
			<template #modal__title>
				<fadeFx  :totalElements="3">
					<h2
						v-if="modal.editing == true"
						>
						{{modal.new ? 'Add a' : 'Edit'}} question for your guests
					</h2>
					<h2
						v-else
						>
						Question
					</h2>
				</fadeFx>
			</template>

			<template #default>
				<stack
					v-if="modal.editing == true"
					>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="3"
						>
						<form @submit.prevent="validateModal" class="stack_pass">
							<field-set
									field="title" 
									placeholder="What would the field be called?"
									:required="true"
									v-model="modal.temp.data.title"
								/>
							<p>
							<label>
								What type of data is expected for this field?
								<br/>
							<select
								:required="true"
								v-model="modal.temp.data.kind"
								>
								<option v-for="(val, readable, index) in input_types" :key="index" :value="val">
									{{readable}}
								</option>
							</select>
							</label>
							</p>

							<info>
								<p>Is this field a required field?</p>
								<checkbox v-model="modal.temp.data.required"/>
							</info>

							<field-set
										type="number"
										:max="200"
										:required="true"
										field="maximum number of characters (maximum of 200)" 
										placeholder="How long should entries to this field be at maximum?"
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
							<input type="submit" hidden=true id="submit-modal-requested_information">
						</form>
					</fadeFx>
				</stack>

				<stack
					v-else
					>
				
					<stack size="xsm">
						<h5>Title</h5>
						<p>{{modal.temp.data.title || '-'}}</p>
					</stack>
					<stack size="xsm">
						<h5>Type</h5>
						<p>{{modal.temp.data.kind || '-'}}</p>
					</stack>
					<stack size="xsm">
						<h5>Required</h5>
						<p>{{modal.temp.data.required || '-'}}</p>
					</stack>
					<stack size="xsm">
						<h5>Max digits</h5>
						<p>{{modal.temp.data.maxlength || '-'}}</p>
					</stack>
					<stack size="xsm">
						<h5>Short Description</h5>
						<p>{{modal.temp.data.short_description || '-'}}</p>
					</stack>
					<stack size="xsm">
						<h5>Description</h5>
						<p>{{modal.temp.data.description || '-'}}</p>
					</stack>
				</stack>

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
			v-else-if="modal.visible && modal.type=='ticket_class' "
			@close="closeModal()"
			>
			<template #modal__title>
				<fadeFx  :totalElements="3">
					<h2
						v-if="modal.editing == true"
						>
						{{modal.new ? 'Add a' : 'Edit'}} ticket class
					</h2>
					<h2
						v-else
						>
						Ticket class
					</h2>
				</fadeFx>
			</template>

			<template #default>
				<stack
					v-if="modal.editing == true"
					>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="3"
						>
						<form @submit.prevent="validateModal" class="stack_pass">
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
					</fadeFx>
				</stack>

				<stack
					v-else
					>
				
					
					<stack
						size="xsm"
						v-for="(val, data, id) in modal.temp.data" :key="id"
						>
						<h5>{{data}}</h5>
						<p>{{val || '-'}}</p>
					</stack>
				</stack>

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
			v-else-if="modal.visible && modal.type=='summary' "
			:striped="true"
			@close="closeModal()"
			>
		
			<template #modal__title>
				<fadeFx  :totalElements="4">
					<h2>Event Summary</h2>
				</fadeFx>
			</template>
			<template #default>
				<stack
					size="lg"
					>

				<fadeFx
					to="top"
					:delay="2"
					:totalElements="4"
					>
					<stack size="sm">
						<h3>Event Details</h3>
						<stack size="xsm">
							<h5>Event title</h5>
							<p>{{data.title || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Type</h5>
							<p>{{data.kind || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Venue</h5>
							<p>{{data.venue || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Description</h5>
							<p>{{data.description || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Date</h5>
							<p>{{data.start_date || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>End Date</h5>
							<p>{{data.end_date || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Maximum number of guests</h5>
							<p>{{data.max_guests || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Account Number</h5>
							<p>{{data.account || '-'}}</p>
						</stack>
						<stack size="xsm">
							<h5>Email</h5>
							<p>{{data.created_by || '-'}}</p>
						</stack>
					</stack>
				</fadeFx>
				
				<fadeFx
					:to="routeDirectionY"
					:delay="3"
					:totalElements="4"
					>
					<stack class="stack_deck">
						<h3>Ticket Classes</h3>
						<stack
							size="sm"
							class="multi"
							v-for="ticket_class in ticket_classes" :key="ticket_class.id"
							>
							<h4 class="count">{{ticket_class.id}}</h4>
							<stack size="xsm">
								<h5>Title</h5>
								<p>{{ticket_class.data.title || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Description</h5>
								<p>{{ticket_class.data.description || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Cost</h5>
								<p>{{ticket_class.data.cost || '-'}}</p>
							</stack>
						</stack>
						<h5 v-if="ticket_classes.length==0">-</h5>
					</stack>
				</fadeFx>
				<fadeFx
					to="top"
					:delay="4"
					:totalElements="4"
					>
					<stack class="stack_deck">
						<h3>Requested Information</h3>
						<stack
							size="sm"
							class="multi"
							v-for="info in requested_information" :key="info.id"
							>
							<h4 class="count">{{info.id}}</h4>
							<stack size="xsm">
								<h5>Title</h5>
								<p>{{info.data.title || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Type</h5>
								<p>{{info.data.kind || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Required</h5>
								<p>{{info.data.required}}</p>
							</stack>
							<stack size="xsm">
								<h5>Maximum number of characters</h5>
								<p>{{info.data.maxlength || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Short Description</h5>
								<p>{{info.data.short_description || '-'}}</p>
							</stack>
							<stack size="xsm">
								<h5>Description</h5>
								<p>{{info.data.description || '-'}}</p>
							</stack>
						</stack>
						<h5 v-if="requested_information.length==0">-</h5>
					</stack>
				</fadeFx>

			</stack>
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
			v-else-if="modal.visible && modal.type=='event-details' "
			:showClose="false"
			icon="&#x2713;"
			>
			<template #modal__title>
				<fadeFx
					to="top"
					:totalElements="4"
					>
					<h2>Success</h2>
				</fadeFx>
			</template>
			
			<template #default>
				<stack>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="3"
						>
						<stack size="xsm">
							<h3>Your Event Details</h3>
							<p>You event was successfully registered. Keep these details safe as you would need them to manage your event.</p>
						</stack>
					</fadeFx>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="3"
						>
						<stack size="xsm">
							<h5>Event code</h5>
							<p>{{modal.temp.event}}</p>
						</stack>
					</fadeFx>
					<fadeFx
						to="top"
						:delay="2"
						:totalElements="3"
						>
						<stack size="xsm">
							<h5>Pass code</h5>
							<p>{{modal.temp.pass}}</p>
						</stack>
					</fadeFx>
				</stack>
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
	type _modalType = "requested_information" | "ticket_class" | "summary" | "event-details"

	
	import axios from 'axios'

	import CONSTANTS from '@/consumables/constants'
	import { requestedInformationType, ticketClassType, routeDirectionType, ResponseObjectType, ResponseErrorObjectType } from '@/consumables/typings'
	import { useToasts } from '@/consumables/plugins'

	import { computed, defineComponent, reactive, ref } from 'vue'

	export default defineComponent({
		name: 'Home',
		props:{},

		setup(props: any){
			let routeDirection = ref<routeDirectionType>('forward')
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
				requested_information: false,
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
			let requested_information=  ref<requestedInformationType[]>([])
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
			
			const next = ()=>{
				if (step.value < totalSteps.value){
					step.value += 1
					routeDirection.value="forward"
				}
				else{
					submit()
				}
			}
			const previous = ()=>{
				if (step.value != 1){
					routeDirection.value="backward"
					step.value -= 1
				}
			}
			const validate = (fromButton=false)=>{
				buttons.footer.primary.status = CONSTANTSX.busy
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
				buttons.footer.primary.status = ''

			}
			const summerize = ()=>{
				openModal("summary", 'summary')
			}

			const submit = async () => {
				modal.state = CONSTANTS.busy
				let encounteredError = false
				let responseData = {}
				let event_code = ""

				await axios
					.post('/api/v1/events/', 
						data)
					.then((response: ResponseObjectType) => {
						responseData = response.data
						event_code = response.data.event
					})
					.catch((error: ResponseErrorObjectType) => {
						encounteredError = true
						$toasts.ErrorToast("Something went wrong", "we weren't able to register your event.")
					})
				
				if (!encounteredError){

					///////////////// SUBMIT THE CLASSES
					for(let index=0; index < ticket_classes.value.length; index++){
						let payload = ticket_classes.value[index].data
						payload.event = event_code
						await axios
							.post(`/api/v1/ticket-classes/`, 
								payload)
							.then((response: ResponseObjectType) => {
							})
							.catch((error: ResponseErrorObjectType) => {
								encounteredError = true
								$toasts.ErrorToast("Something went wrong", 'There seems to be some error in one of your ticket classes.')
							})
					}
					///////////////// SUBMIT THE REQUESTED INFO
					for(let index=0; index < requested_information.value.length; index++){
						let payload = requested_information.value[index].data
						payload.event = event_code
						await axios
						.post(`/api/v1/requested-info/`, 
							payload)
						.then((response: ResponseObjectType) => {
						})
						.catch((error: ResponseErrorObjectType) => {
							encounteredError = true
							$toasts.ErrorToast("Something went wrong", 'There seems to be some error in one of your extra information requests.')
						})
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

			const validateModal = (fromButton=false) => {
				
				let encounteredError= false
				let ext = ""
				if(fromButton==true){
					if (modal.type == 'requested_information'){
						ext = "requested_information"
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
					if (modal.type == "requested_information"){
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
				modal.temp = JSON.parse(JSON.stringify(modal.tracker))
			}
			const resetModalTemp = ()=>{
				if (modal.type == "requested_information"){
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

				modal.type = type
				modal.visible = true
				modal.tracker = data
				copyToModalTemp()
				
			}

			const closeModal = ()=>{

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
				modal.editing = true;
			}
			const deleteModalData = () =>{

				if (modal.type == "requested_information"){
					requested_information.value = requested_information.value.filter((requested_information: requestedInformationType) => requested_information !== modal.tracker)
				}
				else if(modal.type == "ticket_class"  && modal.temp.deletable){
					ticket_classes.value = ticket_classes.value.filter((ticket_class: ticketClassType) => ticket_class !== modal.tracker)
				}

				closeModal()
			}
			
			const saveModalData = async()=>{

				modal.state = CONSTANTS.busy

				let url="ticket-classes"
				if (modal.type == "requested_information"){
					url = "requested-info"
				}
				await axios
					.post(`/api/v1/${url}/verify/`, 
						modal.temp.data)
					.then((response: ResponseObjectType) => {
						if (modal.new){
							modal.new = false
							if (modal.type == "requested_information"){
								requested_information.value.push(modal.temp)
								modal.tracker = requested_information.value[requested_information.value.length - 1]
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
					})
					.catch((error: ResponseErrorObjectType) => {
						$toasts.ErrorToast("Something doesn't seem right")
					})
			}
			const discardModalData = ()=>{


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
			const addModalData = (type: _modalType) =>{
				let payload = {}

				if (type == "requested_information"){
					payload = {
						id: requested_information.value.length+1,
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
			const routeDirectionY = computed(() => {
				return routeDirection.value=='forward'? 'top' : 'bottom'
		})
			

			return{
				CONSTANTSX,

				step,
				totalSteps,
				buttons,
				modal,
				collapsibles,
				data,
				input_types,
				requested_information,
				ticket_classes,
				routeDirectionY,
				
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

</style>