import { push } from "svelte-spa-router"
import { access_token, user_name, is_login } from "../lib/store.js"

const Error = (status_code , response) => {

    let valid = true

    if(status_code === 401){
        access_token.set('')
        user_name.set('')
        is_login.set(false)

        alert("로그인이 필요합니다.")
        push('/')
    }

    if(status_code >= 200 && status_code < 300){

        const _data = response.data

        return {valid,_data}

    }else { 

        if ( response && response.data && response.data.detail) {
            const r_detail = response.data.detail;
        
            //console.log(typeof response.data.detail)

            if (typeof r_detail === 'string'){

                console.log(r_detail)
                valid = false
                return {valid, detail : [r_detail]}

            }else if (typeof r_detail === 'object'){
           
                valid = false
                let detail = []

                //console.log(r_detail)

                for ( let i=0 ; i < r_detail.length ; i ++){
                    detail[i] = r_detail[i].loc[1] + " : " + r_detail[i].msg
                    //console.log(detail[i])
                }

                //console.log(detail[0])

                return {valid, detail}
            }
        }else {
            console.log("response.data.detail is not defined.");
            return { valid: false, detail: "데이터 오류가 발생했습니다." };
        }
    }
}

export default Error;
