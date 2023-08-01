<script>

    import {link} from 'svelte-spa-router'
    import { get_question_list } from '../lib/api.js';

    let question_list = []
    let size = 5
    let page = 0
    let total = 0
    $: total_page = Math.ceil(total/size)
  
    async function fast_get_list(_page){

      let query = {
        page : _page,
        size : size,
      }

      const result = await get_question_list(query)
      question_list = result[1].question_list
      page = _page
      total = result[1].total
      console.log(result[1])
    }
    
    fast_get_list(0)

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

    <!-- 페이징처리 시작 -->
      <!-- 이전페이지 -->
      <li class="page-item {page <= 0 && 'disabled'}">
          <button class="page-link" on:click="{() => fast_get_list(page-1)}">이전</button>
      </li>
      <!-- 페이지번호 -->
      {#each Array(total_page) as _, loop_page}
      <li class="page-item {loop_page === page && 'active'}">
          <button on:click="{() => fast_get_list(loop_page)}" class="page-link">{loop_page+1}</button>
      </li>
      {/each}
      <!-- 다음페이지 -->
      <li class="page-item {page >= total_page-1 && 'disabled'}">
          <button class="page-link" on:click="{() => fast_get_list(page+1)}">다음</button>
      </li>
    <!-- 페이징처리 끝 -->
  </ul>

  <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
  <a use:link href="/user-create" class="btn btn-primary">회원가입하기</a>
  <a use:link href="/user-login" class="btn btn-primary">로그인하기</a>