import { statusOptionType, toastType } from './typings'
import { App, inject } from 'vue'
export default {
    
    install: (app: App, store: any) => {
        
        function AddToast(message: string, status: statusOptionType = '', extra_info: string = "", persistent: boolean = false) {
            store.dispatch("ADD_TOAST", { 'message':message, 'status':status,  'extra_info': extra_info, 'persistent':persistent })
        };
        app.config.globalProperties.$AddToast = AddToast;
        app.provide("AddToast", AddToast);
        // $ add toast/

        function RemoveToast(toast: toastType){
            store.dispatch("REMOVE_TOAST", toast)
        };
        app.config.globalProperties.$RemoveToast = RemoveToast;
        app.provide("RemoveToast", RemoveToast);
        // $ remove toast/

        ////////////////////////////////////////////////////// specific toasts
        function ErrorToast (message: string, extra_info: string="", persistent: boolean=true) {
            store.dispatch("ADD_TOAST", { 'message':message, 'status':'danger',  'extra_info': extra_info, 'persistent':persistent })
        };
        app.config.globalProperties.$ErrorToast = ErrorToast;
        app.provide("ErrorToast", ErrorToast);
        // $ error/

        
        function SuccessToast (message: string, extra_info: string = "") {
            store.dispatch("ADD_TOAST", { 'message': message, 'status': 'success', 'extra_info': extra_info, 'persistent': false })
        };
        app.config.globalProperties.$SuccessToast = SuccessToast;
        app.provide("SuccessToast", SuccessToast);
        // $ success/

    }// install/
} // export/

export function useToasts(){
    const toast = {
        AddToast: inject('AddToast'),
        RemoveToast:  inject('RemoveToast'),
        ErrorToast:  inject('ErrorToast'),
        SuccessToast:  inject('SuccessToast')
    }
    return toast

}
