<template>
	<fieldset class="fieldset">
				<label :for="field">
					{{field}} {{ required ? "(required)" : '' }}
				</label>
				
				<slot name="icon"></slot>
					<!-- ref="textField"
					:value="data"
					@input="process()" -->
				
				<textarea
					v-if="type == 'textarea'"
					
					:value="modelValue"
					@input="$emit('update:modelValue', $event.target.value)"

					:placeholder="placeholder"
					:max="max"
					:required="required"
					:name="field"

					class="input textarea"
				>

				</textarea>

				<input
					v-else
					
					:value="modelValue"
					@input="$emit('update:modelValue', $event.target.value)"

					:type="type"
					:max="max"
					:name="field"
					:placeholder="placeholder"
					:maxlength="maxlength"
					:required="required"
					
					class="input"
					>


				<slot name="left_addon">
				</slot>
				<slot name="button"></slot>

				<template v-if="help_text">
					<p class="help_text">{{help_text}}</p>
				</template>

				<template v-else-if="help_texts">
					<ul class="fieldset_list">
						<li v-for="(item,index) in help_texts" :key="index">
							<p class="help_text">{{item}}</p>
						</li>
					</ul>
				</template>
				
		</fieldset>
</template>


<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_fieldset',
		props:{
			field:{
				type: String,
				required: true,
			},
			placeholder:{
				type: String,
				required: false,
				default: '',
			},
			help_text:{
				// type: String,
				required: false,
				default: false,
			},
			help_texts:{
				// type: Array,
				required: false,
				default: false,
			},
			required:{
				type: Boolean,
				required: false,
				default: false,
			},
			type:{
				type: String,
				required: false,
				default: 'text',
			},
			modelValue:{
				required: false
			},
			maxlength: {
				type: Number,
				required: false
			},
			max: {
				type: Number,
				required: false
			},
		},
	});
</script>


<style lang='scss' scoped>
	
	.help_text {
		font-style: italic;
		font-size: 12px;
		margin-top: 4px;
		margin-left: 8px;
	}
	.fieldset_list {
    	list-style: none;
	}
	
	.fieldset {
		border: none;
		&-error{
			label, .help_text{
				color: $cd;
			}
			.input, .textarea{
				background: $cd;
			}
		}
	}
	.input, .textarea{
		border: none;
		background: $c1-2;
		width:100%;
		
		/* magic nums */
		border-radius: 16px;
		padding: $g0;
	}

	.textarea {
		min-height: 80px;
	}
</style>