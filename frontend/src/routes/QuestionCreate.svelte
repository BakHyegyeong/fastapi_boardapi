<script>
    import {push} from 'svelte-spa-router'
    import Error_sc from "../components/errorfun.js"
    import { post_question } from '../lib/api.js';

    let _subject = ''
    let _content = ''
    let error = {subject : '', content : ''}
    
    async function fast_post_question(event){
        event.preventDefault()

        const _body = {
            "subject" : _subject,
            "content" : _content
        }
        
        await post_question(_body)
        push('/')

    }

    function errors_check(event) {
        event.preventDefault();  
        
        const { valid, errors_check } = Error_sc(_subject,_content)
        
        if (valid.subject || valid.content ) {
            error.subject = errors_check.subject
            error.content = errors_check.content
            
        } else {
            fast_post_question(event)
        }
    }

    
    
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" class="form-control" bind:value="{_subject}">
            <div>{error.subject}</div>
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{_content}"></textarea>
            <div>{error.content}</div>
        </div>
        <button class="btn btn-primary" on:click={(response) => errors_check(response)}>저장하기</button>
    </form>
</div>