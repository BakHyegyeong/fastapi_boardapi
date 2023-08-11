import axios from "axios";
import Error from "../components/Error";
import { access_token} from "./store.js"
import { get } from 'svelte/store'
import qs from "qs"

const fastapi = async (url, method, body, option) => {

    let _url = import.meta.env.VITE_SERVER_URL  + url;

      let request = {
        method: method,
        headers : {
          
        },
        data: body
      }

      if(option === 'login'){
          request.headers.content_type = 'application/x-www-form-urlencoded',
          request.data = qs.stringify(body)
      }  

      if(option === 'get_query'){
        request.params = body      
      }

      const _access_token = get(access_token)
      if (_access_token){
        request.headers.Authorization = "Bearer " + _access_token     
      }

      //console.log(request)

      try {

        const response = await axios(_url, request);
  
        const { valid: _valid, _data: _data } = Error(response.status, response);
        let result = [_valid,_data]

        return result

      } catch (error) {

        if (error.response) {

          const status_code = error.response.status;

          const { valid: _valid, detail: _detail } = Error(status_code, error.response);
          const result = [_valid,_detail]

          console.log(_detail)
          return result

        } else {

          console.log("Error while making request:", error);
          return { valid: false, detail: "요청 중 오류가 발생했습니다." };
        
        }
      }
        
  };
  
  export default fastapi;
  
  export const get_question_list = async (query) => {
    return await fastapi('/question/list', 'GET',query,'get_query');
  };

  export const get_question = async (id) => {
    return await fastapi('/question/detail/'+id,'GET')
  }

  export const delete_question = async (id) => {
    return await fastapi('/question/delete/'+id,'DELETE')
  }
  
  export const post_question = async (body) => {
    return await fastapi('/question/create','POST',body)
  }

  export const update_question = async (body) => {
    return await fastapi('/question/update','PUT',body)
  }

  export const create_answer = async (id, body) => {
    return await fastapi('/answer/create/'+id,'POST',body)
  }

  export const get_answer = async (id) => {
    return await fastapi('/answer/detail/'+id, 'GET')
  }

  export const update_answer = async (body) =>{
    return await fastapi('/answer/update','PUT',body)
  }

  export const delete_answer = async (id) => {
    return await fastapi('/answer/delete/'+id,'DELETE')
  }

  export const create_user = async (body) => {
    return await fastapi('/user/create','POST',body)
  }

  export const login_user = async (body) => {
    return await fastapi('/user/login','POST',body,'login')
  }

  export const create_sympton = async(body) => {
    return await fastapi('/sympton/create','POST',body)
  }
  