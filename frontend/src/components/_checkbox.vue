<template>
	<div>
				<span class="check"
                        @click='toggle'
                        :class="state? 'check-active' : '' "
                    >
                        <span class="check__circle"></span>
				</span>
		</div>
</template>


<script lang="ts">
	import { defineComponent, ref } from 'vue';

	export default defineComponent({
        name:'_checkbox',
        props: {
            required: {
                type: Boolean,
                default: false,
                required: false,
            },
            modelValue: {
                required: false,
                type: Boolean,
                default: false,
            },
        },
        setup(props, context){
            let state =  ref(props.modelValue)
            const toggle = () => {
                state.value = !state.value
                context.emit('update:modelValue', state.value)
            }
            return {
                state,
                toggle
            }
        }
	});
</script>


<style lang='scss' scoped>
    .check {
        // display: flex;
        cursor: pointer;
        display: inline-block;
        position: relative;
        border-radius: 999999px;

        height: 32px;
        width: 64px;
        padding: 6px;
        
        background: $c1;

        // background: transparent;
        border: 1px solid rgba(0,0,0,.3);
        transition: .5s ease;

        &__circle {
            position: absolute;
            display:block;
            height: 60%;

            border-radius: 50%;
            width: 20px;
            background-color: $c2;
            transition: .5s ease;
        }
        &-active{
            border: 1px solid $c1;
            // justify-content: flex-end;

            .check__circle{
                transform: translateX(150%);
                background: $c2-1;
                border: 1px solid rgba(0,0,0,.3);
            }

        }
    }
</style>