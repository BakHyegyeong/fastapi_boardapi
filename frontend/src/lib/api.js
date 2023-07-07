import axios from "axios";

const fastapi = async (url, method, body) => {
    let _url = import.meta.env.VITE_SERVER_URL  + url;

    try {
        
        const Response = await axios(_url, {
            method: method,
            data: body
        })
        
        console.log(Response.data)
        
        return Response.data
        
    } catch (e) {
      console.error(e);
    }
  };
  
  export default fastapi;
  
  export const get_question_list = async () => {
    return await fastapi('/list', 'GET');
  };

  export const get_question = async (id) => {
    return await fastapi('/detail/'+id,'GET')
  }

  export const delete_question = async (id) => {
    return await fastapi('/delete/'+id,'DELETE')
  }
  
  export const post_question = async (body) => {
    return await fastapi('/create','POST',body)
  }

  export const update_question = async (body) => {
    return await fastapi('/update','PUT',body)
  }
  