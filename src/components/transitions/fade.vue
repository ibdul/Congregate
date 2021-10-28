<template>
    <transition
        appear
        :css="false"
        @before-enter="beforeEnter"
        @enter="enter"
        >
        <slot/>
    </transition>
</template>

<script lang="ts">
type _elementType = any //HTMLElement doesn't work well with the transform reset as of now.
type _directionType = 'top'  | 'bottom' | 'right' | 'left' | null

import { defineComponent, PropType } from 'vue'

export default defineComponent({
    props: {
        duration: {
            type: Number,
            default: 5
        },
        delay: {
            type: Number,
            default: 1
        },
        to: {
            type: String as PropType<_directionType>,
            default: null
        },
        totalElements: {
            type: Number,
            default: 1
        }

    },
    setup (props) {
        const beforeEnter = (element: _elementType) => {
            element.style.opacity = 0
            if(props.to){
                switch(props.to) {
                    case 'bottom': element.style.transform = 'translateY( -100px)';break
                    case 'top' : element.style.transform = 'translateY(100px)'; break
                    case 'right' : element.style.transform = 'translateX(-100px)'; break
                    case 'left' : element.style.transform = 'translateX(100px)'; break
                    // default : element.style.transform =  'initial'
                }

            }
        }
        const enter = (element: _elementType) => {
            let transitions = "opacity ease-in-out"

            if(props.to){
                transitions += ", transform ease-in-out"
            }
            
            getComputedStyle(element)
            element.style.transition = transitions
            element.style.transitionDuration = `${100 * props.duration}ms`
            element.style.transitionDelay = props.to=="top"? `${100 *  props.delay}ms` : `${100 * (props.totalElements - props.delay)}ms`

            setTimeout(() => {
                element.style.opacity = 1
                if(props.to){
                    element.style.transform = 'initial'
                }
                setTimeout(
                    ()=>{

                        element.removeAttribute("style")
                    }, 1000)

            })
        }

        return {
            enter,
            beforeEnter
        }
    }
})
</script>
