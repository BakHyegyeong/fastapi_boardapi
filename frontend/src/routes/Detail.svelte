<script>
    import { link,push } from "svelte-spa-router";
    import { get_question } from "../lib/api";
    import { delete_question } from "../lib/api";

    export let params = {}
    let question_id = params.question_id
    let question = {}
    
    async function fast_get_detail() {
        question = await get_question(question_id)
    }

    async function fast_delete_question() {
        if(window.confirm('정말로 삭제하시겠습니까?')){
            await delete_question(question_id)
            push('/')
        }
    }

    fast_get_detail()
    
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>

<button class="btn btn-sm btn-outline-secondary"
                    on:click={() => fast_delete_question()}>삭제</button>

<a use:link href="/question-modify/{question.id}" class = "btn btn-sm btn-outline-secondary">수정</a>



