<script>

    import {link} from 'svelte-spa-router'
    import { get_question_list } from '../lib/api.js';
    import {page} from "../lib/store.js"
    import { access_token, user_name, is_login } from "../lib/store.js"


    let question_list = []
    let tag = ["all","cook","book","good"]
    let tag_list = [[],[],[],[]]
    let size = 5
    let total = 0
    $: total_page = Math.ceil(total/size)
  
    async function fast_get_list(_page,_tag){

      let query = {
        tag : _tag,
        page : _page,
        size : size,
      }

      const result = await get_question_list(query)
      question_list = result[1].question_list
      $page = _page
      total = result[1].total
      //console.log(result[1].question_list)

      return question_list
    }
    
    (async () => {
      for (let i in tag){
        tag_list[i] = await fast_get_list($page,tag[i])
        //console.log(tag_list[i])
    }
    })()
    
    //console.log(tag_list)
    
  </script>
  
  <h1>자유게시판</h1>
  
  <ul>
    {#each tag_list[0] as question, i }
      <tr>
        <td>{ total - ($page * size) - i }</td>
        <td>
            <a use:link href="/detail/{question.id}">{question.subject}</a>
            {#if question.answers.length > 0 }
            <span>{question.answers.length}</span>
            {/if}
        </td>
        <td>{ question.user ? question.user.username : "" }</td>
        <td>
          {#if question.modify_date}
              <div>{question.modify_date}</div>
          {:else}
              <div>{question.create_date}</div>
          {/if}
        </td>
    </tr>
    {/each}

    <!-- 페이징처리 시작 -->
      <!-- 이전페이지 -->
      <li class="page-item {$page <= 0 && 'disabled'}">
          <button class="page-link" on:click="{() => fast_get_list($page-1)}">이전</button>
      </li>
      <!-- 페이지번호 -->
      {#each Array(total_page) as _, loop_page}
      <li class="page-item {loop_page === $page && 'active'}">
          <button on:click="{() => fast_get_list(loop_page)}" class="page-link">{loop_page+1}</button>
      </li>
      {/each}
      <!-- 다음페이지 -->
      <li class="page-item {$page >= total_page-1 && 'disabled'}">
          <button class="page-link" on:click="{() => fast_get_list($page+1)}">다음</button>
      </li>
    <!-- 페이징처리 끝 -->
  </ul>


  <h1>요리게시판</h1>
  <ul>
    {#each tag_list[1] as question, i }
      <tr>
        <td>{ total - ($page * size) - i }</td>
        <td>
            <a use:link href="/detail/{question.id}">{question.subject}</a>
            {#if question.answers.length > 0 }
            <span>{question.answers.length}</span>
            {/if}
        </td>
        <td>{ question.user ? question.user.username : "" }</td>
        <td>
          {#if question.modify_date}
              <div>{question.modify_date}</div>
          {:else}
              <div>{question.create_date}</div>
          {/if}
        </td>
    </tr>
    {/each}
 </ul> 

 <h1>책추천게시판</h1>
  <ul>
    {#each tag_list[2] as question, i }
      <tr>
        <td>{ total - ($page * size) - i }</td>
        <td>
            <a use:link href="/detail/{question.id}">{question.subject}</a>
            {#if question.answers.length > 0 }
            <span>{question.answers.length}</span>
            {/if}
        </td>
        <td>{ question.user ? question.user.username : "" }</td>
        <td>
          {#if question.modify_date}
              <div>{question.modify_date}</div>
          {:else}
              <div>{question.create_date}</div>
          {/if}
        </td>
    </tr>
    {/each}
 </ul> 

 <h1>자랑게시판</h1>
  <ul>
    {#each tag_list[3] as question, i }
      <tr>
        <td>{ total - ($page * size) - i }</td>
        <td>
            <a use:link href="/detail/{question.id}">{question.subject}</a>
            {#if question.answers.length > 0 }
            <span>{question.answers.length}</span>
            {/if}
        </td>
        <td>{ question.user ? question.user.username : "" }</td>
        <td>
          {#if question.modify_date}
              <div>{question.modify_date}</div>
          {:else}
              <div>{question.create_date}</div>
          {/if}
        </td>
    </tr>
    {/each}
 </ul> 

    {#if $is_login}
      <div>
        {"어서오세요, " + $user_name} <br>
        <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
        <a use:link href="/sympton-home" class="btn btn-primary">증상 등록하기</a>
      </div>
    {/if}

  
  
  <a use:link href="/user-create" class="btn btn-primary">회원가입하기</a>
  <a use:link href="/user-login" class="btn btn-primary">로그인하기</a>
<button on:click={() => {
  $access_token = ''
  $user_name = ''
  $is_login = false
}}>로그아웃</button>