<script>
    import {push} from 'svelte-spa-router'
    import { post_question } from '../lib/api.js';
    import {access_token} from "../lib/store.js"

    let _subject = ''
    let _content = ''
    let _tag = ''
    let error = []
    
    //console.log($access_token)

    async function fast_post_question(event){
        event.preventDefault()

        const _body = {
            "subject" : _subject,
            "content" : _content,
            "tag" : _tag
        }
        
        const result = await post_question(_body)
        //console.log(result)

        if (result[0]){
            push('/')
        }else {

            error = result[1]
            //console.log(error)        
        }
        
    }    
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" class="form-control" bind:value="{_subject}">
        </div>
        <label for="tag">게시판 선택</label>
        <select name="tag" id="tag" bind:value="{_tag}">
            <option value = "all">자유게시판</option>
            <option value = "cook">요리게시판</option>
            <option value = "book">책추천게시판</option>
            <option value = "good">자랑게시판</option>
        </select>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{_content}"></textarea>
        </div>
        <div>
            {#each error as er}
                <li>{er}</li>
            {/each}
        </div>
        <button class="btn btn-primary" on:click={(response) => fast_post_question(response)}>저장하기</button>
    </form>
</div>