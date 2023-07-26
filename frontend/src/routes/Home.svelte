<script>

    import {link} from 'svelte-spa-router'
    import { get_question_list } from '../lib/api.js';

    let question_list = []
  
    async function fast_get_list(){
      question_list = await get_question_list()
    }
    
    fast_get_list()
  </script>
  
  <h1>게시판</h1>
  <ul>
    {#each question_list as question, i }
      <tr>
        <td>{i+1}</td>
        <td>
            <a use:link href="/detail/{question.id}">{question.subject}</a>
        </td>
        <td>{question.create_date}</td>
    </tr>
    {/each}
  </ul>

  <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>