<script>
    import { link,push } from "svelte-spa-router";
    import { create_answer, get_question } from "../lib/api.js";
    import { delete_question } from "../lib/api.js";

    export let params = {}
    let question_id = params.question_id
    let question = {answers:[]}

    let _content = ""
    let error = []
    
    async function fast_get_detail() {
        const result = await get_question(question_id)
        question = result[1]        
    }

    async function fast_delete_question() {
        if(window.confirm('정말로 삭제하시겠습니까?')){
            await delete_question(question_id)
            push('/')
        }
    }

    async function fast_create_answer(event) {
        event.preventDefault();  

        const _body = {
            "content" : _content
        }

        const result = await create_answer(question_id,_body)
        
        if (result[0]){
            location.reload();
        }else {
            error = result[1]
            //console.log(error)        
        }
        
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
    <div>
        {#each error as er}
            <li>{er}</li>
        {/each}
    </div>
    <input type = "submit" value = "답변등록" on:click={(response) => fast_create_answer(response)}>
</form>



