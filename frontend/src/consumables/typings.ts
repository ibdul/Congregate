export interface toastType {
    message: string,
    extra_info?: string,
    status?: string,
    id?: number,
    persistent?: boolean
}
export type statusOptionType = "danger" | "info" | "success" | "warning" | ""


export interface requestedInformationType{
    id?: number,
    data :  {
        id?: number,
        title: string,
        kind: string,
        required: boolean,
        maxlength: number,
        short_description: string,
        description: string,
        data: any,
    }
}

export interface ticketClassType {
    id?: number,
    data: {
        id?: number,
        title: string,
        description: string,
        cost: number
    }
}

