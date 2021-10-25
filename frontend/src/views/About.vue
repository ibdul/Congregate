<template>
	<div class="container">
		<fadeFx  :totalElements="4">
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
				:delay="2"
				to="top"
				:totalElements="4"
				>
				<stack size="z">
					<p class="page_suptitle">About us</p>
					<h1 class="page_title">CONGREGATE</h1>
				</stack>
			</fadeFx>

			<stack>
				<fadeFx
					:delay="3"
					to="top"
					:totalElements="4"
					>
					<stack size="xsm">
						<h4>MISSION</h4>
						<p>We're here to to help managing events less hectic</p>
						<p>By offering the right tools and funtionalities needed to super-charge your event management, we give you the powers to make your event management activities a breeze.</p>
						<p>Let's build that beautiful dream event together.</p>
					</stack>
				</fadeFx>
			</stack>
					
			<fadeFx
				:delay="4"
				to="top"
				:totalElements="4"
				>
				<stack size="sm">
					<h4>Leave us a message</h4>
					<form class="stack_pass" @submit.prevent="validate">
						<stack size="xsm">
							<field-set
								type="email"
								field="Your email" 
								placeholder="Please provide an email so we can get back to you"
								v-model="payload.email"
							/>
						</stack>
						<stack size="xsm">
							<field-set
								type="textarea"
								field="message"
								:required="true"
								placeholder="What would you like us to know?"
								v-model="payload.message"
							/>	
						</stack>
						<btn
							class="btn-primary btn-right"
							:disabled="buttons.primary.status == CONSTANTSX.busy "
							:class="buttons.primary.status==CONSTANTSX.busy ? 'btn-loading' : '' "
							>
							{{buttons.primary.status||'Submit'}}
						</btn>
					</form>
				</stack>
			</fadeFx>
				
		</stack>

			<footer class="footer">
			</footer>
	</div>
</template>

<script lang="ts">
import axios from 'axios'
import CONSTANTS from '@/consumables/constants'
import { ResponseObjectType, ResponseErrorObjectType } from '@/consumables/typings'
import { defineComponent, reactive } from 'vue'
import { useToasts } from '@/consumables/plugins'

interface _payload{
	email?: string,
	message: string
}
export default defineComponent({
	setup () {
		const $toasts: any = useToasts()
		const CONSTANTSX = CONSTANTS
		let payload = reactive<_payload>({
			email: "",
			message: ""
		})
		let buttons = reactive({
			primary: {
				status: ''
			}
		})
		const validate = (fromButton=false)=>{
		
			let encounteredError = false
			if (payload.message == ""){
				encounteredError = true
				$toasts.ErrorToast("Error", "You cannot send an empty message")
			}
			else if (payload.message.length < 10) {
				encounteredError = true
				$toasts.ErrorToast("Error", "Your message has to be longer than 10 characters")
			}
			if(encounteredError == false){
				submit()
			}
		}
		const submit = async()=>{
			buttons.primary.status = CONSTANTS.busy
			await axios
			.post('/api/v1/feedback/messages/', 
			payload)
			.then((response: ResponseObjectType) => {
				$toasts.SuccessToast("Your message has been successfully sent.")
			})
			.catch((error: ResponseErrorObjectType) => {
				$toasts.ErrorToast("Something went wrong", "we weren't able to send your message.")
			})
			buttons.primary.status = ''

		}

		return {
			CONSTANTSX,
			buttons,
			payload,
			
			validate
		}
	}
})
</script>
