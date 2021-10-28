import { toastType } from '@/consumables/typings'

import { Module } from 'vuex'
const toastsModule: Module<any, any> = {
	state: {
				deck: Array<toastType>()
			},
			mutations: {
				ADD_TOAST(state: any, { message, status,  extra_info, persistent }:toastType){
					let toast: toastType = {
						'message': message,
						'extra_info': extra_info,
						'status': status,
						'id': state.deck.length ? (state.deck[state.deck.length - 1].id + 1) : 0
					}
					state.deck.push(toast)
					if (!persistent){
						setTimeout(()=>{state.deck = state.deck.filter((toastInstance: toastType) => toastInstance.id !== toast.id)}, 10000)
					}
		
				},
				REMOVE_TOAST(state: any, toast: toastType){
					state.deck = state.deck.filter((toastInstance: toastType) => toastInstance.id !== toast.id)
				}, 
			},
			actions: {
				ADD_TOAST({ commit }: any, { message, status,  extra_info, persistent }: toastType){
					commit('ADD_TOAST', { message, status,  extra_info, persistent })
				},
				REMOVE_TOAST({ commit }: any, toast: toastType){
					commit('REMOVE_TOAST', toast)
				},
			},
}

export default toastsModule