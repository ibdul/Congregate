<template>
    <button  class="btn" @click="$emit('click')">
        <slot>
            Button text
        </slot>
    </button>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
    	emits: ['click'],
		name:'_button',
	});
</script>

<style lang="scss" scoped>
    .btn {
        padding: 8px 16px;
        cursor: pointer;
        border-radius: 8px;
        border: none;

        /* magic */
        background: $c1;
        color: $c2;
        margin:4px;

        &:hover:not(:disabled) {
            background: $c1-2;
            box-shadow: 0 0 11px #0000007a;
        }

        &-fluid {
            width: 100%
        }
        &-primary {

            /* magic */
            color: $c1;
            background: $c2;
         
             &:hover {
                background: $c1-2;
                box-shadow: 0 0 11px #0000007a;
            }
        }
        &-loading{
            display: inline-flex;
            align-items: center;
            cursor: progress;
            // &::after{
            //     content: '';
            //     width: 0px;
            //     height: 0px;
            //     top: 50%;
            //     right: 6px;
            //     box-shadow: 0 0 0 1px $c1-2;
            //     border-radius: 50%;
            //     animation: rotate360 .5s infinite linear, exist .1s forwards ease;
            // }

            &::after{
                content: '';
                width: 0px;
                height: 0px;
                margin-left: 4px;
                top: 6px;
                right: 50%;
                border: 2px solid $c2-1;
                border-right: 3px solid rgba(0,0,0,0%);
                border-radius: 50%;
                animation: rotate360 .5s infinite linear, exist .1s forwards ease;
            }
        }
        &-danger {
                color: $c2;
                background: $cd;
        }
        &-right {
            float: right;
        }
        &-clear {
            color: $c1;
            background: transparent;

            &-danger:hover {
                color: $c2;
                background: $cd;
            }
        }
        &-primary-clear {
            color: $c2;
            background: transparent;
        }
    }

    @keyframes rotate360{
        100%{
            transform: rotate(360deg)
        }
    }
    @keyframes exist{
        100%{
            width: 1ex;
            height: 1ex;
            // margin: -8px 5px 4px 0 ;
        }
    }
    
</style>