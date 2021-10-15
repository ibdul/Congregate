import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
axios.defaults.baseURL = "http://127.0.0.1:8000"


import plugins from './consumables/plugins'

import _toast from './components/_toast.vue'
import toast_deck from './components/_toast_deck.vue'
import btn from './components/_button.vue'
import _card from './components/_card.vue'
import _card_deck from './components/_card_deck.vue'
import _checkbox from './components/_checkbox.vue'
import dots from './components/_dots.vue'
import field_set from './components/_fieldset.vue'
import _info from './components/_info.vue'
import modal from './components/Modal.vue'


const APP = createApp(App)

APP.component("toast", _toast)
APP.component("toast-deck", toast_deck)
APP.component("btn", btn)
APP.component("card", _card)
APP.component("card-deck", _card_deck)
APP.component("checkbox", _checkbox)
APP.component("dots", dots)
APP.component("field-set", field_set)
APP.component("info", _info)
APP.component("modal", modal)

APP.use(store).use(plugins, store).use(router).mount('#app')
