<script>
    import { link,push } from "svelte-spa-router";
    import { create_answer, get_question } from "../lib/api.js";
    import { delete_question } from "../lib/api.js";
    import {Error_c} from "../components/errorfun.js";

    export let params = {}
    let question_id = params.question_id
    let question = {answers:[]}

    let _content = ""
    let error = {content : ''}
    
    async function fast_get_detail() {
        question = await get_question(question_id)
    }

    async function fast_delete_question() {
        if(window.confirm('정말로 삭제하시겠습니까?')){
            await delete_question(question_id)
            push('/')
        }
    }

    function errors_check(event) {
        event.preventDefault();  
        
        const { valid, errors_check } = Error_c(_content)
        if (valid.content) {
            error.content = errors_check.content    
        } else {
            fast_create_answer(event)
        }
    }

    async function fast_create_answer(event) {
        event.preventDefault();  

        const _body = {
            "content" : _content
        }

        await create_answer(question_id,_body)
        location.reload();
    }

    fast_get_detail()
    
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>

<button class="btn btn-sm btn-outline-secondary"
                    on:click={() => fast_delete_question()}>삭제</button>

<a use:link href="/question-modify/{question.id}" class = "btn btn-sm btn-outline-secondary">수정</a>


<form method="post">
    <textarea rows="15" bind:value={_content}></textarea>
    <div>{error.content}</div>
    <input type = "submit" value = "답변등록" on:click={(response) => errors_check(response)}>
</form>



