<script>
    import {push} from "svelte-spa-router";
    import {update_answer, get_answer} from "../lib/api.js" 

    export let params = {}
    let answer_id = params.answer_id
    let answer = {}
    let error = []

    async function fast_get_detail(){
        let result = await get_answer(answer_id)
        answer = result[1]
    }

    fast_get_detail()

    async function fast_update_answer(){

        const _body = {
            "content" : answer.content,
            "answer_id" : answer_id
        }

        const result = await update_answer(_body)

        if (result[0]){
            push('/')
        }else {
            error = result[1]        
        }
    }
</script>


<div class="mb-3">
    <label for="content">내용</label>
    <textarea class="form-control" rows="10" bind:value="{answer.content}"></textarea>
</div>
<div>
    {#each error as er}
        <li>{er}</li>
    {/each}
</div>
<button class="btn btn-sm btn-outline-secondary"
                    on:click={() => fast_update_answer()}>제출</button>

