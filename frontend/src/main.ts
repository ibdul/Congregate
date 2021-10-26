import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
axios.defaults.baseURL = process.env.VUE_APP_AXIOS_DEFAULT_PREFIX


import plugins from './consumables/plugins'

import _toast from './components/_toast.vue'
import _stack from './components/_stack.vue'
import toast_deck from './components/_toast_deck.vue'
import btn from './components/_button.vue'
import _board from './components/_board.vue'
import _card from './components/_card.vue'
import _card_deck from './components/_card_deck.vue'
import _checkbox from './components/_checkbox.vue'
import dots from './components/_dots.vue'
import field_set from './components/_fieldset.vue'
import _info from './components/_info.vue'
import modal from './components/Modal.vue'

import fadeFx from './components/transitions/fade.vue'


const APP = createApp(App)

APP.component('fadeFx', fadeFx)
APP.component("toast", _toast)
APP.component("stack", _stack)
APP.component("toast-deck", toast_deck)
APP.component("btn", btn)
APP.component("board", _board)
APP.component("card", _card)
APP.component("card-deck", _card_deck)
APP.component("checkbox", _checkbox)
APP.component("dots", dots)
APP.component("field-set", field_set)
APP.component("info", _info)
APP.component("modal", modal)

APP.use(store).use(plugins, store).use(router).mount('#app')
