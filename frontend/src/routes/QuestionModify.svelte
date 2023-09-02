<script>
    import { push } from "svelte-spa-router";
    import { get_question } from "../lib/api.js";
    import { update_question } from "../lib/api.js";

    export let params = {}
    let question_id = params.question_id
    let question = {}
    let error = []

    async function fast_get_detail() {
        let result = await get_question(question_id)
        question = result[1]
    }

    fast_get_detail()

    async function fast_update_question() {

        const _body = {
            "subject" : question.subject,
            "content" : question.content,
            "question_id" : question_id
        }

        const result = await update_question(_body)

        if (result[0]){
            push('/')
        }else {
            error = result[1]
            //console.log(error)        
        }
    }
   
</script>

<div class="mb-3">
    <label for="subject">제목</label>
    <input type="text" class="form-control" bind:value="{question.subject}">
</div>
<label for="tag">게시판 선택</label>
        <select name="tag" id="tag" bind:value="{question.tag}">
            <option value = "all">자유게시판</option>
            <option value = "cook">요리게시판</option>
            <option value = "book">책추천게시판</option>
            <option value = "good">자랑게시판</option>
        </select>
<div class="mb-3">
    <label for="content">내용</label>
    <textarea class="form-control" rows="10" bind:value="{question.content}"></textarea>
</div>
<div>
    {#each error as er}
        <li>{er}</li>
    {/each}
</div>
<button class="btn btn-sm btn-outline-secondary"
                    on:click={() => fast_update_question()}>제출</button>

