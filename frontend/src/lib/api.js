import axios from "axios";
import Error from "../components/Error";

const fastapi = async (url, method, body) => {

    let _url = import.meta.env.VITE_SERVER_URL  + url;

      try {

        const response = await axios(_url, {
          method: method,
          data: body
        });
  
        const { valid: _valid, _data: _data } = Error(response.status, response);
        let result = [_valid,_data]

        return result

      } catch (error) {

        if (error.response) {

          const status_code = error.response.status;

          const { valid: _valid, detail: _detail } = Error(status_code, error.response);
          const result = [_valid,_detail]

          //console.log(result)
          return result

        } else {

          console.log("Error while making request:", error);
          return { valid: false, detail: "요청 중 오류가 발생했습니다." };
        
        }
      }
        
  };
  
  export default fastapi;
  
  export const get_question_list = async (query) => {
    //return await fastapi('/question/list', 'GET',query);

    const response = await axios(import.meta.env.VITE_SERVER_URL + '/question/list'
    , {params : query});

    const { valid: _valid, _data: _data } = Error(response.status, response);
    let result = [_valid,_data]

    return result
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

  export const create_user = async (body) => {
    return await fastapi('/user/create','POST',body)
  }

  export const login_user = async (body) => {
    return await fastapi('/user/login','POST',body)
  }
  