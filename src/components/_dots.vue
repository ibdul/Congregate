<template>
	<div class="dots_container">
		<ul class="dots">
				<li
					v-for="dot in [...Array(total).keys()]"
					:key="dot"
					class="dots_item"
					:class="dot==step-1 ? 'dots_item-active' : '' "
					>
				</li>
			</ul>
	</div>
</template>

<script lang="ts">
	import { defineComponent } from 'vue';

	export default defineComponent({
		name:'_dots',
        props:{
            total:{
                type: Number,
                required: true,
            },
            step:{
                type: Number,
                required: true,
            },
        },
	});
</script>


<style lang='scss' scoped>
    .dots_container{
        text-align: center;

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
                border: .2ch solid $c2;
                transition: 1s ease;

                &-active{
                    border: .5ch solid $c2;
                }
            }
        }
    }
</style>