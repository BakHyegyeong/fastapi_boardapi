const Error = (status_code , response) => {

    let valid = true

    if(status_code >= 200 && status_code < 300){

        const _data = response.data

        return {valid,_data}

    }else { 

        if ( response && response.data && response.data.detail) {
            const r_detail = response.data.detail;
        
            //console.log(response.data)

            if (typeof r_detail === 'string'){

                valid = false
                return {valid, r_detail}

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
